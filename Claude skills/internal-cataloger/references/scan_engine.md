# Vault 掃描演算法

internal-cataloger Step 2 的核心。對整個 Obsidian vault 走訪每個檔案，提取 metadata。

## 輸入

- `vault_root`: `D:\Obsidian\TorchBase\TorchBased\Claude workspace`

## 輸出

- `files_metadata`: dict，key 是相對路徑，value 是 metadata 物件

## 演算法

```python
files_metadata = {}

for filepath in walk(vault_root):
    rel_path = relative(filepath, vault_root)
    
    # 排除規則
    if rel_path starts with ".obsidian/": continue
    if rel_path starts with ".trash/": continue
    if rel_path starts with ".recycle/": continue
    if rel_path starts with "_internal-catalog/": continue   # 自我索引
    if filename starts with ".": continue                     # 隱藏檔
    
    # 處理檔案
    metadata = extract_metadata(filepath, rel_path)
    files_metadata[rel_path] = metadata
```

## metadata 物件結構

```python
{
    "rel_path": "Basic/articles/2026-04/foo.md",
    "absolute_path": "D:\\Obsidian\\...\\foo.md",
    "title": "<從 frontmatter 或 H1 取>",
    "filename": "foo.md",
    "mtime": <epoch>,
    "ctime": <epoch>,
    "size_bytes": <int>,
    "extension": ".md",
    
    # frontmatter 欄位（可能缺）
    "status": "wip",                         # 預設 untagged
    "category": "文章",                      # 預設用路徑退回
    "target_word_count": 5000,
    "next_action": "補第三章引用",
    "priority": 2,
    "blocked_by": null,
    "abandoned_at": null,
    "hide_from_dashboard": false,
    "description": "量子生物學論文回顧",
    
    # 計算欄位
    "actual_word_count": 3247,
    "completion_pct": 65,                    # if target_word_count present
    "first_level_folder": "Basic",
    
    # 引用負債（list of dict）
    "citation_debts": [
        {"type": "TODO", "line": 42, "context": "..."},
        ...
    ]
}
```

## extract_metadata 流程

```python
def extract_metadata(filepath, rel_path):
    md = {
        "rel_path": rel_path,
        "absolute_path": filepath,
        "filename": basename(filepath),
        "mtime": os.path.getmtime(filepath),
        "ctime": os.path.getctime(filepath),
        "size_bytes": os.path.getsize(filepath),
        "extension": splitext(filepath)[1],
        "first_level_folder": rel_path.split('/')[0] if '/' in rel_path else "(root)",
    }
    
    # 預設值
    md["status"] = "untagged"
    md["category"] = None
    md["target_word_count"] = None
    md["next_action"] = None
    md["priority"] = 999
    md["blocked_by"] = None
    md["abandoned_at"] = None
    md["hide_from_dashboard"] = False
    md["description"] = None
    md["title"] = None
    md["citation_debts"] = []
    md["actual_word_count"] = 0
    md["completion_pct"] = None
    
    # 只解析 markdown
    if md["extension"].lower() == ".md":
        try:
            content = read_file(filepath)
            md["actual_word_count"] = count_words(content)
            
            # frontmatter
            fm = parse_frontmatter(content)
            if fm:
                md["status"] = fm.get("status", "untagged").lower()
                md["category"] = fm.get("category")
                md["target_word_count"] = fm.get("target_word_count")
                md["next_action"] = fm.get("next_action")
                md["priority"] = fm.get("priority", 999)
                md["blocked_by"] = fm.get("blocked_by")
                md["abandoned_at"] = fm.get("abandoned_at")
                md["hide_from_dashboard"] = fm.get("hide_from_dashboard", False)
                md["description"] = fm.get("description")
                md["title"] = fm.get("title")
            
            # title 退回
            if not md["title"]:
                md["title"] = extract_first_h1(content) or md["filename"]
            
            # description 退回
            if not md["description"]:
                md["description"] = extract_first_paragraph(content, max_chars=80)
            
            # 完成度
            if md["target_word_count"] and md["actual_word_count"]:
                md["completion_pct"] = round(md["actual_word_count"] / md["target_word_count"] * 100)
            
            # category 退回
            if not md["category"]:
                md["category"] = md["first_level_folder"]
            
            # 引用負債
            md["citation_debts"] = scan_citation_debts(content)
        
        except Exception as e:
            log(f"Failed to parse {filepath}: {e}")
            # 非 fatal，繼續使用預設值
    
    else:
        # 非 markdown：基本檔案資訊即可
        md["title"] = md["filename"]
        md["category"] = md["first_level_folder"]
    
    return md
```

## 字數計算（actual_word_count）

```python
def count_words(text):
    # 移除 frontmatter
    text = strip_frontmatter(text)
    # 移除 markdown syntax 不應計入字數
    text = strip_markdown_syntax(text)   # ![]() 連結文字保留，URL 移除
    
    chinese_chars = sum(1 for c in text if is_chinese(c))
    english_words = len([w for w in text.split() if not contains_chinese(w)])
    
    return chinese_chars + english_words
```

中文字單字符算 1，英文按空白分隔 word 算 1。中英混雜分別算後加總。標點不算。

## frontmatter 解析

支援標準 YAML frontmatter：

```
---
key: value
key: [list, item]
key:
  - nested
  - list
---
```

解析失敗 → 視為「無 frontmatter」，使用預設值。**不**因 frontmatter 損壞而跳過整個檔案。

## 引用負債掃描

per `references/citation_debt.md`，對 markdown 內容掃描 4 種 pattern。

## 增量 vs 全量

每次跑都全量掃描（vault 規模通常 <10000 檔，掃描 <30 秒）。`.snapshot.json` 用於：

- 偵測 status 變化（從 X 變 Y → 寫進 CHANGELOG）
- 偵測新檔（出現在當前但不在 snapshot）
- 偵測刪檔（在 snapshot 但不在當前）

snapshot 不為了加速掃描存在，純為 CHANGELOG 變化偵測。

## 失敗處理

| 場景 | 處理 |
|------|------|
| 某檔讀取權限不足 | log 並跳過該檔 |
| 某檔 frontmatter 損壞 | 用預設值處理該檔 |
| vault root 不存在 | 整個 skill FAIL |
| 中途網路硬碟斷線 | 已掃部分保留，重跑時重來 |

整體處理：個別檔案失敗不阻擋整體掃描。失敗檔案數 > 5% → 整體 status = WARN。
