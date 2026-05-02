# Claude Skills

個人 skill 倉庫。儲存與目錄規則請見 [`SKILL_STORAGE_RULES.md`](./SKILL_STORAGE_RULES.md)。

## 目前 skills

### 內容產出型
| Skill | 用途 | 入口 |
|-------|------|------|
| `alphaxiv-paper-lookup/` | 透過 alphaxiv.org 查 arxiv 論文，比讀 PDF 更快 | [SKILL.md](./alphaxiv-paper-lookup/SKILL.md) |
| `startup-pitch-investor/` | 對外募資/投資人 pitch deck（Markdown 大綱） | [SKILL.md](./startup-pitch-investor/SKILL.md) |
| `startup-pitch-internal/` | 對內 board / all-hands / team / department deck | [SKILL.md](./startup-pitch-internal/SKILL.md) |
| `biomedical-lit-search/` | 生醫文獻搜尋（PubMed / 多源整合 + 驗證） | [SKILL.md](./biomedical-lit-search/SKILL.md) |
| `nhird-hwdc-feasibility/` | 健保資料庫 / HWDC 可行性評估 | [SKILL.md](./nhird-hwdc-feasibility/SKILL.md) |
| `clinical-research-ideation/` | 臨床研究題目發想 | [SKILL.md](./clinical-research-ideation/SKILL.md) |
| `pocus-em-domain/` | 急診 POCUS 領域 skill | [SKILL.md](./pocus-em-domain/SKILL.md) |

### 投資審查型
| Skill | 用途 | 入口 |
|-------|------|------|
| `investor-diligence-review/` | 模擬 tier-1 VC partner 寫 IC memo；對 pitch / 資料室做投資人視角的盡職調查 | [SKILL.md](./investor-diligence-review/SKILL.md) |

### 監督稽核型
| Skill | 用途 | 入口 |
|-------|------|------|
| `skill-governance/` | 對整個 skills repo 跑 SKILL_STORAGE_RULES §10 違規檢查 | [SKILL.md](./skill-governance/SKILL.md) |
| `output-supervisor/` | 對任一 skill 產出物做第二雙眼稽核（讀 source skill 的 audit_checklist.md） | [SKILL.md](./output-supervisor/SKILL.md) |

### 維運型（Bedridden Library 系統）
| Skill | 用途 | 入口 |
|-------|------|------|
| `vault-curator/` | 多源同步 + git push：把 Obsidian vault 與 skills repo 中的選定內容 mirror 到 D:\Bedridden Library\ 並 push 到 GitHub | [SKILL.md](./vault-curator/SKILL.md) |
| `vault-cataloger/` | Bedridden Library 端公開編目：維護 00-MOC.md 與 CHANGELOG.md（GitHub-renderable 相對路徑連結） | [SKILL.md](./vault-cataloger/SKILL.md) |
| `internal-cataloger/` | Obsidian 全 vault 本地編目：含狀態、Next Actions、引用負債、字數完成度的儀表板，永不上 git | [SKILL.md](./internal-cataloger/SKILL.md) |
| `longform-architect/` | 長文章架構規劃：多輪迭代直到使用者明確同意，落地 structures/<slug>.md | [SKILL.md](./longform-architect/SKILL.md) |
| `longform-writer/` | 長文撰寫：依 architect 鎖定的 structure 三段式產出（樣本 → 全文 → 自檢） | [SKILL.md](./longform-writer/SKILL.md) |

**Chain A**（每日 07:00 排程）：vault-curator → vault-cataloger → internal-cataloger
**Chain B**（人為觸發）：longform-architect → longform-writer → output-supervisor

## 根目錄結構

```
D:\Claude skills\
├── README.md                       ← 本檔
├── SKILL_STORAGE_RULES.md          ← 新增/整理 skill 前必讀
├── <skill-name>/                   ← 每支 skill 一個資料夾（見上方表格）
└── _meta/                          ← 所有非 skill 檔案
    ├── templates/                  ← startup_pitch_skill_template.md
    ├── stress-tests/               ← stress_test_archbase*.md
    ├── eval-tools/                 ← eval_viewer_*.html, grade_outputs.py
    ├── backlog/                    ← v0.4_backlog.md
    ├── workspaces/                 ← skill-creator 產出的 *-workspace/
    └── audits/                     ← 稽核 skill 的報告
        ├── repo/                   ← skill-governance 報告
        └── output/<skill>/         ← output-supervisor 報告
```

## 新增 skill 的步驟

1. 讀 [`SKILL_STORAGE_RULES.md`](./SKILL_STORAGE_RULES.md)
2. 呼叫 `anthropic-skills:skill-creator`，要求把資料夾建在這個目錄下
3. skill-creator 跑完後，把 `*-workspace/` 與其他非 skill 產出搬到 `_meta/` 對應子目錄
4. 在本 README 的「目前 skills」表格新增一列
5. 呼叫 `skill-governance` 對整個 repo 跑稽核，確認新 skill 沒有違反儲存規則
