# vault-cataloger audit checklist

由 output-supervisor 在 Chain A 自動讀取。

## 連結正確性（CRITICAL）

- [ ] 00-MOC.md 中所有相對路徑連結對應實際存在的檔案
- [ ] 沒有指向 `_archive/` 內檔案的連結（archive 不該被 surfacing）
- [ ] CHANGELOG.md 當日新增區塊在最頂端（prepend，不 append）
- [ ] 所有連結是相對路徑形式（`./<path>` 或 `<path>`），**不**使用 wikilink `[[]]`

## 一致性（CRITICAL）

- [ ] catalog 列出的檔案數 = source dest 子資料夾內實際符合白名單的檔案數
- [ ] 沒有檔案被列入兩個分類
- [ ] frontmatter category 與檔案實際路徑分類一致（per K-3 (c) 規則）
- [ ] 每個 enabled source 都有對應的 00-MOC.md 與 CHANGELOG.md

## Bedridden 端特性（CRITICAL）

- [ ] 沒有 Obsidian wikilink 殘留（`[[文章名]]` 形式）
- [ ] 沒有 Obsidian 專屬 syntax（`#tag`、callouts `> [!note]` 等）出現在 catalog 內
  - 注意：被編目的「內容檔」可以有，但 catalog 自己不能有
- [ ] catalog frontmatter 含 `maintained_by: vault-cataloger` 與 `last_updated`

## 完整性（⚠ WARN）

- [ ] 「最近 7 日」區塊有當日項目（若當日有 sync）
- [ ] CHANGELOG 當日有「新增 / 修改 / 歸檔」全部三類（即使空，要顯示「（無）」）
- [ ] frontmatter total_files 或 total_skills 已更新
- [ ] CHANGELOG 區塊含對應的 commit_hash

## 可讀性（⚠ WARN）

- [ ] 00-MOC 檔案開頭有清楚說明「自動維護，請勿手動編輯」
- [ ] 連結文字清楚（不是「點這裡」這類無意義）
- [ ] Claude skills MOC 依 README 三個分類組織
- [ ] Claude basic MOC 依 frontmatter category 或路徑分類

## graceful degrade（⚠ WARN）

- [ ] 若 curator 沒給 input：catalog 用 manual full mode 重生成
- [ ] 若某個 source dest 不存在：跳過該 source，不阻擋其他 source 編目
- [ ] CHANGELOG.md 損壞 → 備份後重建空檔（不偽造歷史）

## 範圍邊界（CRITICAL）

- [ ] **沒有**寫入 Obsidian vault 內任何檔案（vault 端是 internal-cataloger 的責任）
- [ ] **沒有**修改 source 路徑下的內容檔（cataloger 只讀不寫 source）
- [ ] **沒有**做 git 操作（git 是 curator 的責任）
