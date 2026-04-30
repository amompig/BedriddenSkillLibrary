# longform-architect audit checklist

由 output-supervisor 在 architect 寫完 structure 檔後讀取。

## 結構完整性（CRITICAL）

- [ ] structure 檔有完整 frontmatter，含必要欄位：
  - title
  - slug
  - target_word_count
  - audience
  - genre
  - status（必須是 `locked-for-writer`）
  - revision（v1, v2, ...）
  - template（medical-imrad / stem-imrad / generic）
  - locked_at（時間戳）
- [ ] 章節大綱存在，有預估字數
- [ ] 章節字數加總 ±20% 落在 target_word_count 範圍

## 內容約束（CRITICAL）

- [ ] 「writer 不該做的事」區塊存在且非空
- [ ] 「必寫的關鍵主張」區塊存在
- [ ] 「預期引用方向」區塊存在（即使粗略，至少列幾個方向）
- [ ] 「寫作指令給 writer」區塊存在

## 邊界（CRITICAL）

- [ ] structure 檔**不**包含完整段落內容（架構應是骨架，不是寫好的文章）
- [ ] structure 檔**不**包含 architect 自己的長段論述（>200 字的章節描述視為違規）
- [ ] structure 檔**沒有**「writer 應該寫…」之類的指示替代實際章節大綱

## 規範（⚠ WARN）

- [ ] template 欄位是 medical-imrad / stem-imrad / generic 之一
- [ ] slug 為 kebab-case
- [ ] 檔案路徑為 `Basic\structures\<slug>.md`（不是其他位置）
- [ ] 所有章節有編號（1, 1.1, 1.2, 2, ...）

## 落地細節（⚠ WARN）

- [ ] structure 檔的 frontmatter `authored_by_architect` 為本 skill 名
- [ ] 字數預估區間合理（非 "0" 或 ">10000" 這類無意義值）
- [ ] References 章節作為一個獨立章節列出（即使無具體論文）

## graceful degrade（⚠ WARN）

- [ ] 若使用者選擇 generic 模板：frontmatter 標 `template: generic`
- [ ] 微調模式時 revision > 1，且原章節未受影響部分保留原樣

## 流程合規（CRITICAL）

- [ ] structure 檔**只**在使用者明確說終止 token 後才寫入（檢查 chat history）
- [ ] **沒有**在 Round 1..N 迭代中先寫檔再修
