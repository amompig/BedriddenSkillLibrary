# CHANGELOG.md schema

每個 source 的 dest 子資料夾下有一份獨立 `CHANGELOG.md`，記錄該 source 的歷史變更。

## 整體結構

```markdown
# <source 名> CHANGELOG

> vault-cataloger 自動維護。每日記錄新增 / 修改 / 歸檔。
> 對應的 git commit hash 標於每個區塊。

## YYYY-MM-DD（最新）

### Commit
- Hash: `<commit_hash>`
- Message: `[curator] YYYY-MM-DD multi-source sync: ...`

### 新增（<count>）
- [<檔名>](./<相對路徑>) — <分類>
- ...

### 修改（<count>）
- [<檔名>](./<相對路徑>) — <分類>
- ...

### 歸檔（<count>）
- `<原相對路徑>` → `_archive/<source>/<date>/<原相對路徑>`
- ...

## YYYY-MM-DD

...
```

## 維護規則

### Prepend 不 append

每日新區塊**插在頂端**（最新在上）：

```
[檔頭 + 說明]
## 2026-04-30 ← 今日新增（最頂）
## 2026-04-29
## 2026-04-28
...
```

### 沒變更的日子不寫

若某天 curator 跑了但 0 new、0 changed、0 archived → **不**新增 H2 區塊。CHANGELOG 只記實際有變動的日子。

### 三類都要顯示（即使空）

當日有任一類變更 → H2 區塊內三類「新增 / 修改 / 歸檔」全部顯示，沒項目寫「（無）」：

```markdown
## 2026-04-30

### Commit
- Hash: `abc123`

### 新增（1）
- [foo.md](./articles/foo.md) — 文章

### 修改（0）
（無）

### 歸檔（0）
（無）
```

## 分類取得

每筆 entry 後面的「— <分類>」依 `references/classification.md` 規則決定：

- 對 obsidian-vault 型：依 frontmatter `category` 或路徑（hybrid）
- 對 skill-repo 型：依 README 中的分類（內容產出型、投資審查型、監督稽核型）

無法分類 → 寫「— 未分類」。

## 歸檔項目格式

歸檔項目用「→」標示去向：

```
- `articles/old-thing.md` → `_archive/Claude basic/2026-04-30/articles/old-thing.md`
```

歸檔項目**不**用 markdown link（因為去處在 _archive，不應該被 surface）。

## 損壞處理

若 CHANGELOG.md 損壞（YAML 解析失敗、結構錯亂）：

1. 備份至 `_curator/logs/<today>/<source>-CHANGELOG.bak`（curator 端，不在 Bedridden）
2. **不**偽造歷史——重建為空 CHANGELOG，只含當日區塊
3. 在當日區塊加備註：「⚠ 前日 CHANGELOG 損壞已重建，舊版備份於 logs」
4. 後續正常維護

## 與 git history 的關係

CHANGELOG 是「人類可讀的變更摘要」，git log 是「機器精確的變更紀錄」。兩者互補：

- CHANGELOG 易讀但可能不精確（cataloger 解析 curator 結果）
- git log 精確但難讀（每個檔案的 line-level diff）

讀者要看「過去某天動了什麼」優先看 CHANGELOG；要看「某檔案的詳細演進」用 `git log <file>`。

## 升級空間

當 CHANGELOG 累積到 1000+ entries（約 3 年資料）：

- 考慮拆分：CHANGELOG.md 保留近 6 個月，舊資料移到 `CHANGELOG-archive/<year>.md`
- 升級時 cataloger 自動偵測並建議使用者
- 拆分動作不在排程模式自動跑，須使用者確認

## frontmatter（CHANGELOG 自己的）

```yaml
---
maintained_by: vault-cataloger
last_updated: YYYY-MM-DD HH:MM
covers_from: YYYY-MM-DD     # 第一筆 entry 的日期
total_entries: <int>        # H2 區塊數
---
```

`covers_from` 升級拆分時更新（指本檔當前涵蓋範圍）。
