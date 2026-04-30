# internal-cataloger audit checklist

由 output-supervisor 在 Chain A 自動讀取。本 skill 雖然輸出純本地，仍稽核儀表板一致性。

## 一致性（CRITICAL）

- [ ] dashboard 列出的 total_files = 實際 vault 檔案數（含全部，排除 .obsidian/ 等）
- [ ] dashboard 中所有 wikilink 都對應實際存在的檔案
- [ ] 狀態分布（draft + wip + blocked + abandoned + published + private + untagged）加總 = total_files
- [ ] 沒有檔案在 dashboard 中重複出現於兩個 status 區塊
- [ ] 沒有檔案出現在「依資料夾」但不在「依狀態」（或反之）

## Wikilink 格式（CRITICAL）

- [ ] 所有檔案連結用 `[[完整相對路徑/檔名]]` 形式
- [ ] **不**使用 markdown 相對連結 `[](./path)`（那是 vault-cataloger 的格式）
- [ ] wikilink 路徑相對於 vault root（即 Claude workspace\）

## 範圍邊界（CRITICAL）

- [ ] **沒有**寫入 vault 內任何使用者內容檔（per I-9 不主動改 frontmatter）
- [ ] **沒有**寫入 Bedridden Library 任何位置
- [ ] **沒有**做 git 操作
- [ ] 輸出全部在 `_internal-catalog/` 下

## 完整性（⚠ WARN）

- [ ] 「最近活動」區塊有當日項目（若當日 vault 有變更）
- [ ] CHANGELOG 當日有區塊
- [ ] `.snapshot.json` 存在且為合法 JSON
- [ ] frontmatter total_files / total_words 已更新

## Untagged 提醒（⚠ WARN）

- [ ] dashboard 「Untagged」區塊存在
- [ ] 若 untagged 檔案 > 10% 增量於前次 → WARN 提示「最近 untagged 檔暴增」
- [ ] **未**主動為 untagged 檔寫 frontmatter（per I-9）

## 升級偵測（⚠ WARN）

- [ ] total_files > 500 時提示升級多檔結構
- [ ] 升級提示**不**自動執行升級（須使用者明確要求）

## 引用負債（⚠ WARN）

- [ ] 引用負債區塊有列出所有偵測到的記號
- [ ] 每筆有 (檔案, 行號, context) 三欄
- [ ] 4 種 pattern 都有納入掃描（TODO / 需查證 / [?] / CITATION-NEEDED）

## Obsidian 整合（⚠ WARN）

- [ ] `_internal-catalog/` 不會被同步到 Bedridden Library（檢查 Claude basic 白名單未含）
- [ ] dashboard 開頭有教學連結引導使用者 Obsidian 排除設定（首次跑或重大變動時）
