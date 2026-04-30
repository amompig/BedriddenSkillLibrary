# 白名單檔解析規則（DSL）

`_curator/whitelists/<source>.md` 是給人讀的 markdown，但需要被 vault-curator 程式化解析。本檔定義解析規則：哪些 markdown 結構視為配置項，哪些是說明文字。

## 整體結構

```markdown
---
source: <source 名>
type: <obsidian-vault | skill-repo>
last_updated: YYYY-MM-DD
---

# <自由標題>

<自由說明文字>

## <區塊 1>

- list item 1
- list item 2

## <區塊 2>

- list item 1
...
```

## 解析原則

### 區塊識別

- 每個 `##` 標頭開啟一個「區塊」
- 區塊名稱用標頭文字（去除前後空白）
- 區塊內第一個 `##` 之後、下一個 `##` 之前的所有內容屬於該區塊

### List item 抽取

每個區塊只解析「`-` 開頭」的 list item：

```markdown
## included_folders
- published/    ← 抽取
- articles/     ← 抽取

這段說明文字會被忽略。

- references/   ← 仍會被抽取（不論前面有沒有空段落）
```

### 註解處理

list item 裡面的 `#` 後面內容視為註解，解析時去除：

```markdown
- _meta/                # 稽核報告，不公開
```

抽取結果：`_meta/`（不含註解）

### 空行與標題層級

- 空行不影響解析
- `#` `###` `####` 等其他標頭層級**不**開啟新區塊（只有 `##` 算）
- frontmatter（前後 `---` 之間）獨立解析，不在區塊內

## 各區塊的解析語意

### `## included_folders` (obsidian-vault)

- 路徑相對於 source root
- 路徑可有或沒有尾隨 `/`，解析後一律加 `/`
- 包含子資料夾（不需明確列子目錄）

### `## included` (skill-repo)

- 路徑相對於 source root
- 可以是檔案（如 `README.md`）或資料夾（含尾隨 `/`）
- 不展開子資料夾——只列頂層或具體路徑

### `## excluded_globs` / `## excluded`

- 支援 glob 語法：
  - `*` 匹配除 `/` 外的任意字元
  - `**` 匹配任意路徑（含子目錄）
  - `?` 單字元
  - `[abc]` 字元集合
- glob 路徑相對於 source root，除非以 `**/` 開頭

範例：
```
**/.obsidian/**       匹配任何位置的 .obsidian 資料夾下檔案
*.tmp                 source root 下 .tmp 檔
**/*.tmp              任何位置的 .tmp 檔
articles/draft-*.md   articles 資料夾下 draft- 開頭的 md
```

### `## frontmatter 規則` (obsidian-vault)

- 純文字描述
- 解析「跳過下列 status 值」之後的 list items
- 將每個 list item 視為一個 status 值（lowercase 比對）

### `## 第三方排除規則` (skill-repo)

- 純文字描述
- 解析時忽略——這個區塊是給人讀的政策說明
- 實際排除邏輯硬編碼在 sync_engine：
  1. 檢查 `<skill>/.do_not_publish` 是否存在
  2. 讀 `<skill>/SKILL.md` frontmatter，檢查 `author` 欄位

### `## skill 排除清單` 或類似名稱

- 抽取 list items 加入 `excluded` 集合
- 與 `## excluded` 內容合併處理

## 互動編輯模式（per M-9）

當使用者說「把 X 加入白名單」「Claude skills 的 Y 不要公開」時：

1. 解析使用者意圖（哪個 source、加入或移除、哪個區塊）
2. 讀對應 whitelist 檔
3. 修改該區塊的 list items
4. 更新 frontmatter `last_updated`
5. 寫回檔案
6. 印出 diff 給使用者確認

互動編輯不破壞註解或說明文字（只改 list items）。

## 解析失敗處理

- frontmatter 缺失或損壞 → 警告但繼續用 type=unknown 處理（停下提示使用者）
- 必要區塊缺失（如 obsidian-vault 缺 `## included_folders`）→ 視為「無檔案符合」（保險起見）
- glob 語法錯誤 → 跳過該 entry，警告使用者
- 整個檔案無法解析（YAML 損壞等）→ FAIL，跳過該 source

## 防呆規則

- list item 內容若包含 `..`（試圖逃逸 source root）→ 拒絕該 entry
- list item 內容若是絕對路徑（以 `/` 或 `D:\` 開頭）→ 拒絕
- 重複 entry → 去重，警告
