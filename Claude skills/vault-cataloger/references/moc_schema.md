# 00-MOC.md schema

依 source `type` 用不同模板。本檔給兩個固定模板：obsidian-vault 與 skill-repo。

## obsidian-vault 型 (Claude basic\00-MOC.md)

### Frontmatter

```yaml
---
maintained_by: vault-cataloger
last_updated: YYYY-MM-DD HH:MM
total_files: <int>
source_path: D:\Obsidian\TorchBase\TorchBased\Claude workspace\Basic
---
```

### Body 結構

```markdown
# Claude basic Map of Contents

> 自動維護。請勿手動編輯。最後更新：YYYY-MM-DD HH:MM

## 總覽

<total_files> 份檔案。詳細變更見 [CHANGELOG.md](./CHANGELOG.md)。

## 分類索引

<分類列表，初版列在 MOC 內；>500 檔時升級為子索引檔>

### <分類 1>（<count>）

- [<檔名>](./<相對路徑>) — <一行描述（從 frontmatter `description` 或檔案首行）>
- ...

### <分類 2>（<count>）
...

## 最近 7 日新增 / 修改

| 日期 | 檔案 | 操作 |
|------|------|------|
| YYYY-MM-DD | [<title>](./<path>) | 新增 / 修改 |
| ... | ... | ... |
```

### 升級條件

當 total_files > 500：

- 「分類索引」區塊改為「分類索引（見子索引檔）」
- 在 dest 子資料夾建立 `_catalog\` 資料夾
- 對每個分類產一個 `_catalog\<category>.md`
- MOC 改為列出子索引連結

升級時保留歷史 MOC 一份在 `_catalog\.archive\<date>-MOC.md`。

## skill-repo 型 (Claude skills\00-MOC.md)

### Frontmatter

```yaml
---
maintained_by: vault-cataloger
last_updated: YYYY-MM-DD HH:MM
total_skills: <int>
source_path: D:\Claude skills
---
```

### Body 結構

```markdown
# Claude skills Map of Contents

> 自動維護，依 D:\Claude skills\README.md 的分類組織。
> 排除清單上的 skill 不出現在此（見 _curator/whitelists/Claude skills.md）。

## 內容產出型

- [<skill 名>](./<skill-name>/SKILL.md) — <description 第一行（從 SKILL.md frontmatter）>
- ...

## 投資審查型

- ...

## 監督稽核型

- ...

## 最近 7 日新增 / 修改

| 日期 | Skill | 操作 |
|------|-------|------|
| YYYY-MM-DD | [<skill 名>](./<skill-name>/SKILL.md) | 新增 / 修改 |
| ... | ... | ... |
```

### 分類解析（skill-repo）

從 source 的 `D:\Claude skills\README.md` 解析「目前 skills」表格，依其分類安排。

若 README 結構變動：
- 偵測「| skill | 用途 | 入口 |」表格
- 每個分類用 H3 標頭分隔
- 每個 skill 有對應的入口連結

讀不到 README 結構時，退回單一「全部」分類列出。

## description 取得規則

對每個被編目的檔案/skill，取一行描述：

1. 若有 frontmatter `description`：取第一行
2. 否則取檔案 body 第一個非空、非 H1 的段落首句
3. 都沒有：留空 `—`

description 截斷至 80 字元，超過加 `…`。

## 連結相對路徑規則

- 一律 `./` 開頭（明確相對於 catalog 檔位置）
- 路徑分隔符用 `/`（非 `\`），跨平台 + GitHub renderable
- 路徑包含中文、空格 → URL encode 處理

範例：

```markdown
[foo](./articles/2026-04/foo.md)                ✅
[bar](./published/long%20form/bar.md)          ✅（含空格 url-encode）
[baz](articles/baz.md)                         ❌（缺 ./）
[qux](.\articles\qux.md)                       ❌（用了 \）
[quux](D:/Bedridden%20Library/Claude%20basic/quux.md) ❌（絕對路徑）
[wikilink-style]([[文章]])                      ❌（wikilink 是 internal-cataloger 的責任）
```

## 維護規則

- 重寫 MOC 時**完整重生成**，不 in-place edit
- 重寫時若內容無實質變化（diff 空）→ 不寫檔（避免 mtime 變動觸發 git diff）
- 寫入失敗 → 保留舊版，記錄到 logs

## 多 source 的並列關係

每個 source 有自己的 MOC 與 CHANGELOG：

```
D:\Bedridden Library\
├── Claude basic\
│   ├── 00-MOC.md          ← 此 source 的 catalog
│   └── CHANGELOG.md
└── Claude skills\
    ├── 00-MOC.md          ← 另一 source 的 catalog
    └── CHANGELOG.md
```

**不**做「跨 source 總 MOC」——每個 source 是獨立的子展示廳。

未來若需要跨 source 的入口頁，可在 Bedridden Library 根目錄維護一份 README.md 含兩個 source 的入口連結（這個由 vault-curator 在 first_run 寫一份基本版，cataloger 不維護）。
