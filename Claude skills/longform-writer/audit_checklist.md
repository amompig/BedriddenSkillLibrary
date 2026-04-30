# longform-writer audit checklist

由 output-supervisor 在 writer Stage 3 完成後讀取。

## 風格（CRITICAL）

- [ ] 全文僅開頭區塊有條列；正文章節無孤立條列段落
- [ ] 沒有 GPT-ism 起手式（「在快速變遷的世界中」「眾所週知」「在當今...」「不可否認的是」等）
- [ ] 沒有「我覺得」「個人猜想」「我認為」等主觀詞
- [ ] 條列出現的場景符合例外規則：開頭摘要 / 並列項目（前後敘述包裹）/ References / 表格
- [ ] 章節間有銜接段落（不是突然跳到下一章）

## 架構符合度（CRITICAL）

- [ ] structure 中「必寫的關鍵主張」全部覆蓋
- [ ] 章節順序與 structure 一致
- [ ] 字數落 target_word_count ±25% 內
- [ ] frontmatter `revision_consumed` = structure 檔的 revision

## 引用合法性（CRITICAL）

- [ ] 所有引用屬於 4 類允許來源（peer-reviewed / preprint / thesis / report）
- [ ] References 章節格式統一（每筆同樣的 metadata 順序）
- [ ] 沒有捏造的引用（每筆有可查驗的 title + venue/journal）
- [ ] preprint 標 [PREPRINT]、thesis 標 [THESIS]、report 標 [REPORT]
- [ ] References 全用英文 metadata（per W-8 中英混雜處理）

## 引用比例（⚠ WARN）

- [ ] Peer-reviewed 比例 ≥ 60%
- [ ] Preprint 比例 ≤ 25%（超過要在文中註明依賴未發表研究的理由）
- [ ] Thesis 引用有腳註說明依賴未發表研究的理由

## 完整性（⚠ WARN）

- [ ] References 章節存在且非空
- [ ] 沒有「TODO」「TBD」「[待補]」殘留
- [ ] 圖表（若有）的標題與引用編號連貫
- [ ] frontmatter 含 actual_word_count, sources_used (各類別 count), status

## 落地細節（⚠ WARN）

- [ ] 落地路徑為 `published/<category>/<slug>.md`
- [ ] frontmatter `category` 對應路徑
- [ ] frontmatter `status` 為 `published` 或 `awaiting-review`
- [ ] frontmatter `actual_word_count` 已填且合理（非 0）

## 模板合規（⚠ WARN）

- [ ] structure 中 `template` 是 generic 時，本檔 frontmatter 也標 `template: generic`，且 supervisor 加 WARN 紀錄
- [ ] medical-imrad 模板：章節含 Introduction / Methods / Results / Discussion；若文獻回顧含 PRISMA-style 描述
- [ ] stem-imrad 模板：章節含 IMRaD 古典結構；Methods 章節含實驗流程與資料分析方法

## graceful degrade（⚠ WARN）

- [ ] writer 自檢失敗 3 次後停下，frontmatter `status: awaiting-review`
- [ ] 中途引用不確定時，frontmatter `pending_citations` 列出該引用清單
- [ ] 草稿仍在 `drafts/<slug>.draft.md`（中途備份）
