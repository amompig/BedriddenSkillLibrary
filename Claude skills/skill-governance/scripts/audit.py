#!/usr/bin/env python3
"""
skill-governance audit script.

Runs deterministic rules 1-6, 8 from SKILL_STORAGE_RULES.md §10 against the
skills repository root and emits a JSON report on stdout.

Rule 7 (description quality) is LLM-judged and handled by SKILL.md after this
script returns. The JSON includes a `descriptions` map for that purpose.

Usage:
    python audit.py --root "D:\\Claude skills"

Exit codes:
    0  script ran successfully (the JSON itself reports any violations)
    2  invalid arguments / root not found
"""

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path


# Allowed top-level entries in the skills root
ROOT_ALLOWED_FILES = {"README.md", "SKILL_STORAGE_RULES.md"}
ROOT_ALLOWED_DIRS = {"_meta"}

# Allowed _meta/ subdirectories
META_ALLOWED_SUBDIRS = {
    "templates", "stress-tests", "eval-tools", "backlog", "workspaces", "audits"
}

# Indicators that a path inside a skill folder is workspace/eval residue
RESIDUE_DIR_NAMES = {"workspace"}
RESIDUE_DIR_PREFIXES = ("iteration-",)
RESIDUE_DIR_SUFFIXES = ("-workspace",)
RESIDUE_FILE_NAMES = {
    "eval_metadata.json", "grading.json", "benchmark.json", "benchmark.md",
    "timing.json"
}

KEBAB_CASE_RE = re.compile(r'^[a-z][a-z0-9]*(-[a-z0-9]+)*$')
VERSION_SUFFIX_RE = re.compile(r'-v\d+$|_v\d+$')

# A relative cross-reference that escapes a skill folder
CROSS_SKILL_REF_RE = re.compile(r'\.\./[A-Za-z0-9_\-.]+')


# ---------------- frontmatter parsing (regex, no PyYAML) ----------------

def parse_frontmatter(skill_md: Path):
    """Return (frontmatter_dict_or_None, line_count). Handles simple key: value
    pairs and multi-line scalar values (subsequent indented or non-key lines fold)."""
    try:
        text = skill_md.read_text(encoding="utf-8")
    except OSError:
        return None, 0
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, len(lines)
    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break
    if end_idx is None:
        return None, len(lines)

    fm = {}
    current_key = None
    current_parts = []
    key_re = re.compile(r'^([A-Za-z_][A-Za-z0-9_\-]*):\s?(.*)$')

    def flush():
        if current_key is not None:
            fm[current_key] = "\n".join(current_parts).strip()

    for raw in lines[1:end_idx]:
        if not raw.strip():
            continue
        m = key_re.match(raw)
        # Treat a line as a new key only if it starts at column 0 and matches key: pattern
        if m and not raw.startswith((" ", "\t")):
            flush()
            current_key = m.group(1)
            current_parts = [m.group(2)] if m.group(2) else []
        else:
            current_parts.append(raw.strip())
    flush()
    return fm, len(lines)


# ---------------- helpers ----------------

def is_skill_folder(p: Path) -> bool:
    return p.is_dir() and (p / "SKILL.md").is_file()


def list_skill_folders(root: Path):
    return sorted([p for p in root.iterdir() if is_skill_folder(p)],
                  key=lambda p: p.name.lower())


# ---------------- rule checks ----------------

def check_rule_1_root_structure(root: Path):
    violations = []
    for entry in root.iterdir():
        if entry.name.startswith("."):
            continue
        if entry.is_file():
            if entry.name not in ROOT_ALLOWED_FILES:
                violations.append(
                    f"Root file `{entry.name}` not allowed "
                    f"(only {sorted(ROOT_ALLOWED_FILES)} or skill folders or `_meta/`)"
                )
        elif entry.is_dir():
            if entry.name in ROOT_ALLOWED_DIRS:
                continue
            if is_skill_folder(entry):
                continue
            violations.append(
                f"Root dir `{entry.name}/` is neither a skill folder (no SKILL.md) "
                f"nor `_meta/`"
            )
    return violations


def check_rule_2_skill_md(skill_dir: Path):
    """SKILL.md uppercase + valid frontmatter."""
    violations = []
    skill_md = skill_dir / "SKILL.md"
    # Case-insensitive lookup to detect bad casing on Windows
    md_files = [p for p in skill_dir.iterdir()
                if p.is_file() and p.name.lower() == "skill.md"]
    if not md_files:
        violations.append(f"`{skill_dir.name}`: missing SKILL.md")
        return violations
    actual = md_files[0]
    if actual.name != "SKILL.md":
        violations.append(
            f"`{skill_dir.name}`: file is `{actual.name}` — must be `SKILL.md` (uppercase)"
        )
    fm, _ = parse_frontmatter(skill_md if skill_md.exists() else actual)
    if fm is None:
        violations.append(f"`{skill_dir.name}`: SKILL.md missing or has invalid YAML frontmatter")
        return violations
    if not fm.get("name"):
        violations.append(f"`{skill_dir.name}`: frontmatter missing `name`")
    elif fm["name"] != skill_dir.name:
        violations.append(
            f"`{skill_dir.name}`: frontmatter `name` ({fm['name']!r}) "
            f"does not match folder name"
        )
    if not fm.get("description"):
        violations.append(f"`{skill_dir.name}`: frontmatter missing `description`")
    return violations


def check_rule_3_kebab(skill_dir: Path):
    violations = []
    name = skill_dir.name
    if not KEBAB_CASE_RE.match(name):
        violations.append(f"`{name}`: not kebab-case (lowercase, hyphen-separated)")
    if VERSION_SUFFIX_RE.search(name):
        violations.append(f"`{name}`: has version suffix (`-vN`/`_vN`) — use semantic suffix")
    return violations


def check_rule_4_line_count(skill_dir: Path):
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        return []
    lc = sum(1 for _ in skill_md.open(encoding="utf-8"))
    if lc > 150:
        return [f"`{skill_dir.name}`: SKILL.md is {lc} lines (>150). Move details to references/"]
    return []


def check_rule_5_residue(skill_dir: Path):
    violations = []
    seen = set()
    for path in skill_dir.rglob("*"):
        rel = path.relative_to(skill_dir)
        # Check directory components
        for part in rel.parts:
            if part in RESIDUE_DIR_NAMES \
               or any(part.startswith(p) for p in RESIDUE_DIR_PREFIXES) \
               or any(part.endswith(s) for s in RESIDUE_DIR_SUFFIXES):
                key = (skill_dir.name, "dir", part)
                if key not in seen:
                    seen.add(key)
                    violations.append(
                        f"`{skill_dir.name}`: workspace/eval residue dir component `{part}` in `{rel}`"
                    )
                break
        if path.is_file() and path.name in RESIDUE_FILE_NAMES:
            violations.append(
                f"`{skill_dir.name}`: eval residue file `{rel}`"
            )
    return violations


def check_rule_6_cross_refs(skill_dir: Path):
    violations = []
    for path in skill_dir.rglob("*.md"):
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        for m in CROSS_SKILL_REF_RE.finditer(text):
            ref = m.group(0)
            # Allow `..//` rare case? Just flag all `../X` matches.
            rel = path.relative_to(skill_dir)
            violations.append(
                f"`{skill_dir.name}`: `{rel}` contains relative ref `{ref}`"
            )
    return violations


def check_rule_8_meta(root: Path):
    violations = []
    meta = root / "_meta"
    if not meta.is_dir():
        return []
    for entry in meta.iterdir():
        if entry.name.startswith("."):
            continue
        if entry.is_dir():
            if entry.name not in META_ALLOWED_SUBDIRS:
                violations.append(
                    f"`_meta/{entry.name}/` not in approved categories "
                    f"({sorted(META_ALLOWED_SUBDIRS)})"
                )
        elif entry.is_file():
            violations.append(
                f"`_meta/{entry.name}` is a loose file — should live under a subcategory"
            )
    return violations


# ---------------- main ----------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True, help="Path to skills repo root")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    if not root.is_dir():
        print(f"Root not found: {root}", file=sys.stderr)
        sys.exit(2)

    skill_dirs = list_skill_folders(root)

    rule_results = []
    descriptions = {}

    # Rule 1
    rule_results.append({
        "id": 1,
        "name": "Root only contains skills + README + RULES + _meta/",
        "severity": "CRITICAL",
        "violations": check_rule_1_root_structure(root),
    })

    # Rule 2 (per skill, aggregated)
    rule2 = []
    for sd in skill_dirs:
        rule2.extend(check_rule_2_skill_md(sd))
        # Capture description for rule 7 (LLM)
        skill_md = sd / "SKILL.md"
        if skill_md.is_file():
            fm, _ = parse_frontmatter(skill_md)
            if fm and fm.get("description"):
                descriptions[sd.name] = fm["description"]
    rule_results.append({
        "id": 2,
        "name": "Each skill has SKILL.md (uppercase) + valid frontmatter (name, description)",
        "severity": "CRITICAL",
        "violations": rule2,
    })

    # Rule 3
    rule3 = []
    for sd in skill_dirs:
        rule3.extend(check_rule_3_kebab(sd))
    rule_results.append({
        "id": 3,
        "name": "Skill folder name is kebab-case (no vN suffix)",
        "severity": "CRITICAL",
        "violations": rule3,
    })

    # Rule 4
    rule4 = []
    for sd in skill_dirs:
        rule4.extend(check_rule_4_line_count(sd))
    rule_results.append({
        "id": 4,
        "name": "SKILL.md ≤ 150 lines",
        "severity": "WARN",
        "violations": rule4,
    })

    # Rule 5
    rule5 = []
    for sd in skill_dirs:
        rule5.extend(check_rule_5_residue(sd))
    rule_results.append({
        "id": 5,
        "name": "No workspace/eval residue inside skill folder",
        "severity": "CRITICAL",
        "violations": rule5,
    })

    # Rule 6
    rule6 = []
    for sd in skill_dirs:
        rule6.extend(check_rule_6_cross_refs(sd))
    rule_results.append({
        "id": 6,
        "name": "No relative cross-skill references",
        "severity": "CRITICAL",
        "violations": rule6,
    })

    # Rule 8
    rule_results.append({
        "id": 8,
        "name": "_meta/ subdirectories match approved categories",
        "severity": "WARN",
        "violations": check_rule_8_meta(root),
    })

    out = {
        "root": str(root),
        "timestamp": dt.datetime.now().strftime("%Y%m%dT%H%M%S"),
        "skills_scanned": [sd.name for sd in skill_dirs],
        "rules": rule_results,
        "descriptions": descriptions,
    }

    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
