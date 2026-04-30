# First-run 初始化流程

當 `D:\Bedridden Library\` 不存在或不完整時執行。本檔指引「從零」建立完整 Bedridden Library 結構。

## 觸發條件

下列任一情況：

- `D:\Bedridden Library\` 整個資料夾不存在
- 資料夾存在但無 `.git/`
- 資料夾存在、是 git repo，但 `_curator/sources.md` 不存在

## 初始化步驟

### Step 1: 建立資料夾骨架

```
D:\Bedridden Library\
├── _curator\
│   ├── whitelists\
│   ├── logs\
│   └── （其他檔案見下）
└── _archive\
```

注意：`Claude basic\` 與 `Claude skills\` 兩個 source 子資料夾**不在初始化階段建立**——首次同步時 sync engine 自動建立。

### Step 2: 寫 .gitignore

```gitignore
# vault-curator 內務檔案不進公開 repo
_curator/
!_curator/.gitkeep

# 但 _archive 進 git（per 設計 M-10）
# 不需要任何 _archive/ 排除規則
```

注意：原本想用 `!_curator/.gitkeep` 排除某個檔案進 git，但實務上 `_curator/` 整個 ignore 即可，gitkeep 不需要。

### Step 3: 寫初始 README.md

如果 `D:\Bedridden Library\README.md` 已存在 → **不覆蓋**（使用者可能自己寫過）。

否則寫入下列基本版（per M-8）：

```markdown
# Bedridden Library

This is a curated public mirror of selected files from local sources.

## Structure

- `Claude basic/` — published content from Obsidian vault
- `Claude skills/` — Claude Skills repository (selected skills)
- `_archive/` — deprecated content, preserved for reference

## How this is maintained

Files in this repository are automatically synced from local sources by `vault-curator`.
The sync logic, source whitelists, and run logs live locally and are not part of this repository.

To request changes to what's published here, contact the maintainer.

## Last sync

(automatically updated by vault-curator)
```

### Step 4: 寫初始 sources.md 模板

```markdown
---
maintained_by: vault-curator
last_updated: YYYY-MM-DD
---

# Bedridden Library Source 登記

## Source: Claude basic
- source_path: D:\Obsidian\TorchBase\TorchBased\Claude workspace\Basic
- dest_name: Claude basic
- type: obsidian-vault
- whitelist: _curator/whitelists/Claude basic.md
- enabled: true
- last_synced: (尚未同步)

## Source: Claude skills
- source_path: D:\Claude skills
- dest_name: Claude skills
- type: skill-repo
- whitelist: _curator/whitelists/Claude skills.md
- enabled: true
- last_synced: (尚未同步)
```

### Step 5: 寫兩個白名單初始檔

#### `_curator/whitelists/Claude basic.md`

```markdown
---
source: Claude basic
type: obsidian-vault
last_updated: YYYY-MM-DD
---

# Claude basic 發布白名單

## included_folders（相對於 source root，即 Basic\）

- published/
- articles/

## excluded_globs

- **/.obsidian/**
- **/*.tmp
- **/Excalidraw/raw/**

## frontmatter 規則

跳過下列 status 值：
- draft
- private
（沒有 frontmatter 視為通過）
```

#### `_curator/whitelists/Claude skills.md`

```markdown
---
source: Claude skills
type: skill-repo
last_updated: YYYY-MM-DD
---

# Claude skills 發布白名單

## included（相對於 D:\Claude skills\）

- README.md
- SKILL_STORAGE_RULES.md
- biomedical-lit-search/
- clinical-research-ideation/
- startup-pitch-investor/
- startup-pitch-internal/
- investor-diligence-review/
- skill-governance/
- output-supervisor/

## excluded（最高優先）

- _meta/
- **/*-workspace/
- **/evals/results/
- **/.git/
- alphaxiv-paper-lookup/
- pocus-em-domain/
- nhird-hwdc-feasibility/

## 第三方排除規則（交集，任一命中即排除）

任一條件命中即排除：
1. skill 資料夾根目錄存在 `.do_not_publish` 標記檔
2. SKILL.md frontmatter 含 `author:` 欄位且值非使用者本人
3. 該 skill 名稱列在上方 excluded 區段

新加入的 skill 預設「公開」。
```

### Step 6: 提示使用者填 remote_config.md

`_curator/remote_config.md` **不**自動填——必須使用者明確提供 GitHub remote URL。寫一份提示模板：

```markdown
# vault-curator remote 設定

請填入 GitHub remote URL（HTTPS 或 SSH 形式皆可），然後重跑同步。

remote_url: <PLEASE-FILL-IN-WITH-YOUR-GITHUB-REPO-URL>
default_branch: main
push_strategy: simple
```

並停下流程，告知使用者：「Bedridden Library 結構已建立，但 GitHub remote 尚未設定。請填好 `D:\Bedridden Library\_curator\remote_config.md` 後重跑 curator。」

### Step 7: git init + first commit

`git init` 之後**不**立即跑首次 commit——等使用者填好 remote_config.md 後，下一輪 curator 同步會做首次 commit。這樣的好處是首次 commit 已經包含實際 mirror 內容（不是空 repo）。

## 失敗處理

任一 step 失敗：

- 不要嘗試後續 step
- 寫一份 `_curator/INIT_FAILED.md` 含失敗原因與已完成 step
- 印出錯誤訊息給使用者
- 等使用者修正後重跑

不要做「部分初始化」——失敗就讓使用者完整看到狀態，不要留下半成品。

## 已初始化但缺零件的修復

若資料夾與 `.git` 都存在但缺 `_curator/sources.md` 或白名單檔：

- 不重跑整個 init
- 只補缺漏的檔案
- 在 `_curator/logs/<today>.md` 記錄補了什麼
