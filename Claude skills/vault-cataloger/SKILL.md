---
name: vault-cataloger
description: |
  Bedridden Library 公開展示廳的編目師 skill。每日 Chain A 第二棒：在 vault-curator 完成同步後，
  接收同步清單，更新 Bedridden Library 中各 source 子資料夾的 00-MOC.md（Map of Content）
  與 CHANGELOG.md。產出物用相對路徑 markdown 連結，可在 GitHub render 直接點擊。
  
  使用觸發條件：
  - 「更新 catalog」「重編目」「更新 MOC」「regenerate catalog」
  - 「Bedridden Library 的編目本」「Claude basic 的索引」「Claude skills 的 MOC」
  - Chain A 自動觸發：vault-curator 完成後鏈式呼叫
  
  不要 trigger 於：
  - Obsidian vault 內部編目（用 internal-cataloger，那支才管 Obsidian 端）
  - 純檔案同步 / git push（用 vault-curator）
  - 寫文章（用 longform-* skill）

requires:
  - vault-curator (Chain A 上游；input contract: 同步清單)
  - output-supervisor (鏈式觸發)
---

# vault-cataloger

> 「公開展示廳編目師」。為 Bedridden Library 的每個 source 子資料夾維護 `00-MOC.md` 與 `CHANGELOG.md`。所有連結用相對路徑（GitHub-renderable），不使用 Obsidian wikilinks。

## 範圍紀律

本 skill 只管 **Bedridden Library 端**的編目。Obsidian vault 端的編目由 `internal-cataloger` 負責（per 設計 I-4 c）。兩者責任不重疊。

## Input contract（從 vault-curator 接手）

排程模式下，curator 完成 Step 5 (寫 LAST_RUN_STATUS) 後 chain 本 skill。傳入：

- `synced_sources`: 本次有變動的 source 名稱清單
- `per_source_changes`: dict `{source_name: {new: [...], changed: [...], archived: [...]}}`
- `commit_hash`: 本次 git commit hash

互動模式或 graceful degrade（curator 沒給 input）：

- 視為「全 Bedridden Library 重編目」
- 對每個 source 從零掃描 dest 內容

## 執行流程

### Step 1: 環境檢查

- `D:\Bedridden Library\` 存在
- 對每個要處理的 source：dest 子資料夾存在
- 若 LAST_RUN_STATUS = FAIL → **不**繼續（per X-1，上游 FAIL 時下游不嘗試）

### Step 2: 模式判斷

- **Chain mode**：從 curator input 取 synced_sources，只處理這些 source
- **Manual full**：對所有 sources.md enabled source 重編目
- **Manual single**：使用者指定某 source 重編目

### Step 3: 對每個 source 跑編目子流程

依 source `type` 用不同 schema：

- `obsidian-vault` → **讀** `references/moc_schema.md` §obsidian-vault
- `skill-repo` → **讀** `references/moc_schema.md` §skill-repo

子流程：

1. 掃描 dest 子資料夾所有檔案（排除 `_archive/` 與 `00-MOC.md` `CHANGELOG.md` 自己）
2. 對每個檔案：解析分類（**讀** `references/classification.md`）
3. 建立分類字典：`{category: [files]}`
4. 重寫 `00-MOC.md`（不 append，每次完整重生成）
5. 更新 `CHANGELOG.md`（**讀** `references/changelog_schema.md`）
6. 一致性檢查（檔案數加總、連結有效性）

### Step 4: chain output-supervisor

per `audit_checklist.md`，傳入：

- `target_file`: 本次更新的 catalog 檔案清單（兩個 source × 2 檔 = 4 個檔案）
- `source_skill`: vault-cataloger

排程模式：自動 chain，FAIL 不阻擋整個 Chain A 結束（但記錄到 LAST_RUN_STATUS）

互動模式：呈現 supervisor 結果，問使用者是否依建議修正

### Step 5: 交棒 internal-cataloger（Chain A 第三棒）

排程模式：自動 chain `internal-cataloger`，傳入「本日 catalog 已更新，可開始本地編目」

互動模式：問使用者是否繼續

## MOC 結構（簡述，詳見 references/moc_schema.md）

兩個 source 都生成 `00-MOC.md`，但結構不同：

**`Claude basic\00-MOC.md`** (obsidian-vault 型)：
- frontmatter（last_updated, total_files）
- 總覽（檔案數、分類分布）
- 分類索引（per K-2 初版只總索引；>500 檔升級子索引）
- 最近 7 日（per K-4 保留）
- 相對路徑連結（per K-6 完整路徑）

**`Claude skills\00-MOC.md`** (skill-repo 型)：
- frontmatter（last_updated, total_skills）
- 依 D:\Claude skills\README.md 的 3 個分類（內容產出型、投資審查型、監督稽核型）
- 每支 skill 列「skill 名 — 一行 description」
- 不深入 references/（per K-5）

## CHANGELOG 結構（簡述，詳見 references/changelog_schema.md）

- 獨立檔案 `<source>/CHANGELOG.md`
- 每日一個 H2 區塊，prepend 到頂端（最新在上）
- 含「新增 / 修改 / 歸檔」三類
- 對應的 commit_hash 寫進區塊

## 與 internal-cataloger 的差異

| 面向 | vault-cataloger | internal-cataloger |
|------|-----------------|---------------------|
| 對象 | Bedridden Library | 整個 Obsidian vault |
| 輸出進 git | 是 | 否 |
| 連結格式 | 相對路徑 markdown | wikilinks（Obsidian） |
| 含未公開檔 | 否（curator 已篩） | 是（含 drafts、private） |
| 加狀態 / next_action | 否（外人不需要看） | 是（per I-2 f） |
| 觸發時機 | Chain A 第二棒 | Chain A 第三棒 |

## audit_checklist.md

本 skill 為「內容產出型」，**強制鏈式觸發 output-supervisor**。詳細稽核項在 audit_checklist.md。
