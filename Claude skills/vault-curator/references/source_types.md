# Source 類型定義

vault-curator 支援多種 source `type`，每種類型有不同的白名單解析規則與檔案處理邏輯。本檔定義每種類型的合約。

## obsidian-vault

### 用途

source 是一個 Obsidian vault 的子資料夾，內含 markdown 檔案，可能有 Obsidian 專屬語法（wikilinks `[[]]`、frontmatter、tags）。

### 白名單規則

`_curator/whitelists/<source>.md` 必須含三個區塊：

#### 1. `## included_folders`

list item 形式（`-` 開頭），路徑相對於 source root。包括子資料夾。

```markdown
## included_folders
- published/
- articles/
- references/
```

#### 2. `## excluded_globs`

list item 形式，glob pattern。最高優先（即使在 included_folders 下也會被排除）。

```markdown
## excluded_globs
- **/.obsidian/**
- **/*.tmp
- **/Excalidraw/raw/**
```

#### 3. `## frontmatter 規則`

用文字描述 frontmatter `status` 欄位哪些值會被跳過。固定支援值：`draft`、`private`。

```markdown
## frontmatter 規則
跳過下列 status 值：
- draft
- private
```

### 檔案處理

對 source 內的每個檔案：

1. 路徑必須在 `included_folders` 列出的某個資料夾下（含子資料夾）
2. 路徑不命中任何 `excluded_globs`
3. 若是 markdown 檔且有 frontmatter：解析 `status` 欄位，命中跳過清單則排除
4. 若無 frontmatter 或 status 不在跳過清單：通過

### 同步邏輯

- 通過篩選的檔案：複製到 `D:\Bedridden Library\<dest_name>\<相對路徑>`
- **保留** Obsidian 語法（不轉換 wikilink）。理由：vault-cataloger 在 Bedridden 端會生成相對路徑連結用於 GitHub render，但檔案內的 wikilink 保留 Obsidian 慣例（讓使用者可選擇用 Obsidian 開啟 Bedridden Library 仍能跳轉）。

## skill-repo

### 用途

source 是一個 Claude skills 倉庫，內含多個 skill 資料夾與一些根層 metadata 檔（README.md, SKILL_STORAGE_RULES.md）。

### 白名單規則

`_curator/whitelists/<source>.md` 必須含區塊：

#### 1. `## included`

list item 形式。可包含：
- 具體檔案名（如 `README.md`）
- skill 資料夾名（kebab-case，含尾隨 `/`，如 `biomedical-lit-search/`）

#### 2. `## excluded`

list item 形式。最高優先。常見排除：
- `_meta/`（稽核報告、workspaces）
- `**/*-workspace/`（skill-creator 評估產物）
- `**/.git/`（如果 source 內有子 git repo）

#### 3. `## 第三方排除規則`

文字描述「不是使用者創建的 skill」如何識別與排除。固定 3 種偵測機制（任一命中即排除）：

1. skill 根目錄存在 `.do_not_publish` 標記檔
2. SKILL.md frontmatter `author:` 欄位非使用者本人
3. 名字列在 `excluded` 清單

### 檔案處理

對 source 內的每個檔案：

1. 路徑命中 `excluded` 任一規則 → 排除（最高優先）
2. 否則檢查路徑是否在 `included` 清單某項下
3. 對 skill 資料夾項：套用第三方排除規則（檢查 `.do_not_publish`、frontmatter author）

### 同步邏輯

- 通過篩選的檔案：複製到 `D:\Bedridden Library\<dest_name>\<相對路徑>`
- 保留 skill 內的 references/ 與 audit_checklist.md 等檔案
- skill repo 不解析 frontmatter status（與 obsidian-vault 不同）

## generic-folder（保留型，未來擴充）

### 用途

預留給未來「純文件庫」型 source。目前未實作，sources.md 不應使用此 type。

### 預期合約

- 無 frontmatter 解析
- 路徑式白名單
- 直接 mirror，不做任何內容轉換

實作時新增本檔對應區塊。

## 新增類型的步驟

若未來要新增第 4 種 source type：

1. 在本檔新增區塊定義其白名單規則與檔案處理邏輯
2. 在 `references/sync_engine.md` 補對應的處理分支
3. 在 SKILL.md Step 0 模式判斷與 Step 2 子流程提及新類型
4. 在 `audit_checklist.md` 補對應稽核項
5. 不要破壞既有兩種類型的合約
