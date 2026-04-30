# 00-DASHBOARD.md schema

internal-cataloger 的核心輸出。初版單檔，>500 檔升級多檔結構。

## Frontmatter

```yaml
---
maintained_by: internal-cataloger
last_updated: YYYY-MM-DD HH:MM
total_files: <int>
total_words: <int with thousand separator>
vault_root: D:\Obsidian\TorchBase\TorchBased\Claude workspace
status_counts:
  draft: <int>
  wip: <int>
  blocked: <int>
  abandoned: <int>
  published: <int>
  private: <int>
  untagged: <int>
---
```

## Body 結構（單檔版）

```markdown
# Internal Catalog Dashboard

> 本檔本地專用，永不上 GitHub。最後更新：YYYY-MM-DD HH:MM
>
> ⚠ Obsidian 設定建議：請在「Files & Links → Excluded files」加入 `_internal-catalog/`
>   讓本目錄不出現在搜尋結果與圖譜中（仍可在檔案總管瀏覽）。

## 總覽

- <total_files> 份檔案，總字數 <total_words>
- 狀態分布：published <N>, wip <N>, draft <N>, blocked <N>, abandoned <N>, private <N>, untagged <N>
- 跨資料夾分布：Basic\ (<N>), notes\ (<N>), meetings\ (<N>), ...
- 最近 7 日新增 <N> / 修改 <N>

## 最近活動（最近 7 日）

| 日期 | 檔案 | 狀態 | 操作 |
|------|------|------|------|
| YYYY-MM-DD | [[<相對路徑>]] | <status> | 新增 / 修改 / 狀態變化 |
| ... | ... | ... | ... |

## 依狀態

### WIP（<count>）
- [[<相對路徑>]] — 完成度 <pct>% (<actual>/<target> 字) — next: <next_action>
- ...

### Draft（<count>）
- [[<相對路徑>]] — <word_count> 字 — next: <next_action>
- ...

### Blocked（<count>）
- [[<相對路徑>]] — 等：<blocked_by> — next: <next_action>
- ...

### Abandoned（<count>）
- [[<相對路徑>]] — 標記 abandoned 於 <abandoned_at>
- ...

### Private（<count>）
- [[<相對路徑>]]
- ...

### Published（<count>）
- [[<相對路徑>]] — 已公開到 Bedridden Library
- ...

### Untagged（<count>，請補 frontmatter）
- [[<相對路徑>]]
- ...

## 依資料夾

### Basic\（<count>）
依資料夾結構，深度展開到第二層子資料夾：

#### Basic\articles\
- [[<完整路徑>]] — <一行 description> — <status>
- ...

#### Basic\drafts\
- [[<完整路徑>]] — <description> — <status>
- ...

### notes\（<count>）
...

### meetings\（<count>）
...

## Next Actions（all files）

依優先序（priority + mtime）：

- [ ] [[<相對路徑>]] — <next_action>
- [ ] [[<相對路徑>]] — <next_action>
- ...

## 引用負債

掃描下列記號，aggregate 後分配到對應檔案：
- `[TODO: ...]`
- `[需查證]`
- `[?]`
- `[CITATION-NEEDED]`

| 檔案 | 記號類型 | 行號 | 周圍 context |
|------|---------|------|--------------|
| [[<檔案>]] | TODO | L<N> | <前後 80 字 context> |
| ... | ... | ... | ... |
```

## 完成度計算

對 status == wip 的檔案，若 frontmatter 有 `target_word_count`：

```
completion_pct = round(actual_word_count / target_word_count * 100)
```

顯示：「完成度 65% (3,200/5,000 字)」

target_word_count 缺失 → 不顯示完成度，只顯示「<N> 字」。

actual_word_count 算法：

- 中文：每 char 算 1 字（除標點外）
- 英文：每 word 算 1 字（whitespace split）
- 中英混雜：分別計算後加總

## 連結格式（Obsidian wikilink）

per K-6 + I-4，internal-cataloger 用 wikilink 完整相對路徑：

```
[[Basic/articles/2026-04/foo]]              ← 含資料夾路徑
[[notes/half-thought]]
[[meetings/2026-04-30]]
```

不要：
- `[[foo]]` — 沒路徑會在同名檔時衝突
- `[foo](path)` — markdown 連結（這是 vault-cataloger 的格式）

## 排序規則

每個區塊內的條目排序：

- **依狀態**內：依優先序（priority + mtime 新到舊）
- **依資料夾**內：依檔名字母序
- **最近活動**：依日期新到舊
- **Next Actions**：依 priority 數字小到大，同 priority 依 mtime 新到舊
- **引用負債**：依檔名 → 行號

## 升級條件（>500 檔）

當 total_files > 500，dashboard 在「總覽」之後加提示：

```
⚠ 已超過 500 檔。建議升級為多檔結構：
   - _by-status/    各狀態獨立檔
   - _by-folder/    各資料夾獨立檔
   - _by-action/    Next Actions 與引用負債獨立
   
請說「升級 internal catalog」我會處理拆分。
```

升級不自動執行（per I-6 「保留升級」）。

## 升級後的多檔結構

升級後：

```
_internal-catalog/
├── 00-DASHBOARD.md      ← 簡化版，只有總覽 + 最近活動 + 連結到子檔
├── _by-status/
│   ├── draft.md
│   ├── wip.md
│   ├── blocked.md
│   ├── abandoned.md
│   ├── published.md
│   ├── private.md
│   └── untagged.md
├── _by-folder/
│   ├── Basic.md
│   ├── notes.md
│   └── ...
├── _by-action/
│   ├── next-actions.md
│   └── citation-debt.md
├── CHANGELOG.md
└── .snapshot.json
```

升級後 dashboard 簡化為「導覽頁」（一頁式儀表板無法承載 500+ 檔資訊）。

## 區塊空 list 處理

任一狀態區塊或分類區塊若 0 檔 → 顯示「（無）」。

例：

```markdown
### Blocked（0）
（無）
```

不要乾脆刪掉區塊——使用者可能習慣看那裡。

## 維護規則

- 每次 Step 4 重寫 dashboard 時**完整重生成**，不 in-place edit
- 重寫時若 diff 為空（無實質變化）→ 不寫檔（避免無謂 mtime 變動）
- 寫入失敗 → 保留舊版，記錄到 CHANGELOG
