# Sync engine 演算法

對單一 source 的同步演算法。SKILL.md Step 2 的核心。

## 輸入

- `source_path`: source 根目錄的絕對路徑
- `dest_path`: `D:\Bedridden Library\<dest_name>` 的絕對路徑
- `source_type`: `obsidian-vault` 或 `skill-repo`
- `whitelist`: 解析後的白名單規則（per `whitelist_dsl.md`）

## 輸出

- `new_files`: 新增檔案清單（含相對路徑與來源完整路徑）
- `changed_files`: 修改檔案清單
- `archived_files`: 從 source 消失但 dest 還有的檔案清單
- 副作用：dest 內檔案被建立、修改、移動到 _archive

## 演算法

### Phase 1: 建立 source set

對 source_path 走訪所有檔案：

```python
source_set = {}     # 相對路徑 → (絕對路徑, mtime, sha256)
for filepath in walk(source_path):
    rel_path = relative(filepath, source_path)
    
    # 套用白名單篩選
    if not match_whitelist(rel_path, whitelist):
        continue
    
    # source_type 特殊處理
    if source_type == "obsidian-vault":
        if rel_path.endswith(".md"):
            frontmatter = parse_frontmatter(filepath)
            if frontmatter.get("status") in ["draft", "private"]:
                continue
    elif source_type == "skill-repo":
        # 第三方排除偵測
        skill_root = find_skill_root(rel_path, source_path)
        if skill_root:
            if exists(f"{skill_root}/.do_not_publish"):
                continue
            skill_md = f"{skill_root}/SKILL.md"
            if exists(skill_md):
                fm = parse_frontmatter(skill_md)
                if fm.get("author") and fm["author"] != USER_NAME:
                    continue
    
    source_set[rel_path] = (filepath, mtime, sha256_quick(filepath))
```

`sha256_quick` 對 <1MB 的檔案讀全檔算 hash；>1MB 的檔案讀首尾各 64KB 與 mtime + size 算 quick hash。寫入 `_curator/.cache/<source>.json` 供下次比對。

### Phase 2: 建立 dest set

對 dest_path 走訪所有檔案：

```python
dest_set = {}
for filepath in walk(dest_path):
    rel_path = relative(filepath, dest_path)
    if rel_path.startswith("_archive/"):
        continue   # _archive 不參與比對
    dest_set[rel_path] = (filepath, mtime, sha256_quick(filepath))
```

### Phase 3: Diff

```python
new_files     = source_set.keys() - dest_set.keys()
removed_files = dest_set.keys() - source_set.keys()
both          = source_set.keys() & dest_set.keys()

changed_files = []
for rel_path in both:
    if source_set[rel_path][2] != dest_set[rel_path][2]:   # hash 不同
        changed_files.append(rel_path)
```

### Phase 4: 預覽

印出 `+N ~M -K` 摘要與檔案清單。互動模式等使用者確認，排程模式自動繼續。

### Phase 5: 執行同步

#### new + changed

對每個 new / changed 檔案：

```
src = source_set[rel_path][0]
dst = f"{dest_path}/{rel_path}"
ensure_dir(parent(dst))
copy(src, dst)              # 保留 mtime
```

寫入完成後再做下一個——不要批次寫，否則 partial failure 難復原。

#### archived

對每個 removed 檔案：

```
src = dest_set[rel_path][0]
archive_dir = f"D:\\Bedridden Library\\_archive\\{source_name}\\{today}\\{rel_path}"
ensure_dir(parent(archive_dir))
move(src, archive_dir)
```

注意：用 move（不是 copy + delete），保證原子性。

#### 大檔警告

對 new + changed 中 >10MB 的檔案：

- 寫入 logs/<today>.md：「⚠ 大檔同步：{rel_path} ({size}MB)」
- **不**阻擋同步（per C-6）
- **不**自動轉 git-lfs

### Phase 6: 更新 cache

寫 `_curator/.cache/<source>.json`：

```json
{
  "last_synced": "2026-04-30",
  "files": {
    "<rel_path>": {"mtime": ..., "sha256": "..."}
  }
}
```

下次同步用此 cache 加速 hash 比對（mtime 沒變的檔案不重算 hash）。

## 原子性保證

完整 sync 不是原子操作（多個檔案個別處理），但每個檔案層級是原子：

- new / changed：先寫到 `<dst>.tmp`，rename 為 `<dst>`
- removed：用 OS move（單一 syscall）

若中途 crash：

- 已處理的檔案 stay
- 未處理的檔案下次重跑會被識別為 new / changed（hash 不同）
- 不會留下半寫入的破檔（rename 保證）

## hash 比對效能

對 1000+ 檔案的 source：

- 首次同步：全部算 hash，慢但只發生一次
- 後續同步：使用 cache，只對 mtime 變動的檔案重算 hash
- mtime 比對極快（os.stat call）

cache miss 處理：cache 不存在 → 退回首次同步行為。

## 失敗處理

| 失敗 | 處理 |
|------|------|
| 某檔案讀取權限不足 | 記錄到 logs，跳過該檔案，繼續其他 |
| 磁碟空間不足 | 立即停下，整個 source 視為 FAIL |
| dest 路徑不存在 | 建立後重試 |
| copy 失敗（其他 IO） | 重試 1 次，仍失敗則跳過該檔案、記錄警告 |
| frontmatter 解析失敗 | 跳過 frontmatter 篩選，視為通過（保險起見不阻擋公開） |

整個 source 同步結束時報告：成功 N，跳過 M，失敗 K。任一檔案失敗 → 該 source 標記為 WARN（不全部 FAIL）；整個 source 失敗 → FAIL（不嘗試後續 source）。

## 與 git 的銜接

sync engine 結束後**不**自動 git add / commit。SKILL.md Step 4 才做 git 操作。理由：

1. 多個 source 的同步要全部完成才一起 commit（一日一 commit 慣例）
2. 同步失敗 → 不污染 git 工作樹
3. 排程觸發時的 git 操作集中管理便於除錯
