---
name: longform-architect
description: |
  長文架構規劃 skill。當使用者要寫長文章（學術回顧、論述、文獻整合等），先做議題範圍釐清、
  提出章節大綱、預估字數與引用方向，與使用者多輪對話討論修訂，**唯有使用者明確說「架構通過」
  或同義中文時**才把最終架構落地為 structures/<slug>.md，作為 longform-writer 的 input。
  
  使用觸發條件：
  - 「幫我寫一篇關於 X 的長文 / 文章 / 論述」
  - 「規劃一篇 / 規劃這篇文章的架構」「論文架構」「文章大綱」「先做架構」
  - 「為主題 X 生成問卷」（interview 檔模式）
  - 「依這份文獻清單規劃一篇文章」（接力觸發，從 lit-search skill 接手）
  - 接力觸發：使用者剛跑完 biomedical-lit-search 或 alphaxiv-paper-lookup
  
  不要 trigger 於：
  - 短文（<1000 字）：直接寫即可
  - 純發想、未確定要寫文章（用 clinical-research-ideation）
  - 已有完整架構，要直接寫（直接用 longform-writer）
  - 改寫 / 修飾既有文章（不在本 skill 範疇）

requires:
  - longform-writer (下游；output contract: structures/<slug>.md)
  - output-supervisor (鏈式觸發)
---

# longform-architect

> 「論文結構顧問」。多輪迭代直到使用者明確同意，才把架構落地交給撰寫員。**只規劃，不開寫。**

## 核心紀律

1. **只規劃，不開寫**：即使使用者催「直接開始寫吧」，仍要先把架構落地成檔，再交棒。**讀** `references/iteration_protocol.md` §邊界。
2. **明確 token 才落地**：使用者說「架構通過」「定案」「就這個架構」「OK 落地」「鎖架構」「進下一步」之一才寫檔。模稜兩可（「好像可以」「應該還行」）必須反問。**讀** `references/termination_tokens.md`。
3. **不主動鏈下游 skill**：lit-search 等不主動觸發，只「建議」使用者鏈式觸發。

## 觸發路徑（4 種）

| 路徑 | 起點 | 進入 |
|------|------|------|
| 直接命名 | 「幫我用 longform-architect 規劃 X」 | Round 0（對話模式） |
| 任務描述觸發 | 「幫我寫一篇關於 X 的長文」 | Round 0（對話模式） |
| 接力觸發 | 剛跑完 lit-search skill | Round 0（已有素材） |
| Interview 檔模式 | 「為主題 X 生成問卷」 | Round 0（生成 interview 檔，**讀** `references/round_zero_interview.md`） |

## 流程

### Round 0: 議題理解

依觸發路徑分支：

**對話模式（路徑 1, 2, 3）**：

依 `references/iteration_protocol.md` §round-zero-questions，直接在對話中問下列必問項目：

- 目標讀者
- 大致字數
- 文體類型（文獻回顧 / 觀點論述 / 個案研究 / 教學介紹）
- 是否已有手邊文獻或素材
- 希望的「立場」或「主軸論點」（或讓 architect 提候選）

**Interview 檔模式（路徑 4）**：

per `references/round_zero_interview.md`：

1. 寫 `D:\Obsidian\TorchBase\TorchBased\Claude workspace\Basic\structures\_pending\<slug>.interview.md`
2. 提示使用者打開該檔離線填寫
3. 使用者填完說「讀問卷繼續」
4. architect 讀填好的檔，跳到 Round 1

### Round 1: 架構初稿

per `references/iteration_protocol.md` §round-1：

1. 若使用者沒提供文獻 → **建議**鏈式觸發 biomedical-lit-search 或 alphaxiv-paper-lookup（不主動鏈）
2. 在對話中印出「架構初稿」（不寫檔）：章節大綱 / 重點 / 預估字數 / 引用方向（即使粗略）
3. 主動問 3-5 個關鍵點請使用者表態

### Round 2..N: 修訂迭代

per `references/iteration_protocol.md` §rounds-2-to-n：

- 每輪明確列「本輪改了什麼」
- 不靜默改其他部分
- 不主動推進到下一輪
- 未定案時所有迭代**只在對話中**（per A-4），不寫檔

### Round Final: 架構落地

當使用者輸入終止 token（per `references/termination_tokens.md`）：

1. 把最終架構寫成 `D:\Obsidian\TorchBase\TorchBased\Claude workspace\Basic\structures\<slug>.md`（per `references/structure_schema.md`）
2. 寫一份「交棒摘要」：標題、檔案位置、預估字數、給 writer 的注意事項
3. 提示：「架構已落地。要交棒給 longform-writer 開始撰寫嗎？」
4. 使用者確認 → orchestrator chain 到 longform-writer

### Round Loop: 微調模式

writer 撰寫時若發現架構有缺，writer 停下提示使用者重啟 architect（per A-6 簡版）。
architect 在微調模式下：

- 只改受影響章節，保留其他章節原樣
- 增加 `revision: v2`（v3...）版本號
- 寫回同一 structures/<slug>.md（不留歷史版本，per A-5）

## 領域寫作模板

per A-7，內建兩個模板（**讀** `references/domain_templates.md`）：

- `medical-imrad`：醫學 / 生醫（PRISMA / IMRaD）
- `stem-imrad`：STEM 實驗類（古典 IMRaD）

不匹配的領域 → fallback 為 `generic` 通用結構。

模板選擇時機：Round 0 確認「文體類型」後，依文體決定預設模板。Round 1 起 architect 依模板提供架構草稿。

## chain output-supervisor

architect 寫完 structure 檔後 chain output-supervisor：

- target_file: `D:\Obsidian\TorchBase\TorchBased\Claude workspace\Basic\structures\<slug>.md`
- source_skill: longform-architect

per `audit_checklist.md`，輕量稽核：frontmatter 完整、字數預估合理、必寫主張存在、不夾帶論述。

supervisor PASS → 提示交棒
supervisor WARN → 顯示警告但仍可交棒
supervisor FAIL → **不**交棒，提示修正

## 不該做的事

- 不該寫超過架構的內容（不變成代寫）
- 不該主動鏈式觸發 lit-search skill（per §9 避免無限鏈）
- 不該在使用者沒明確同意前寫 structures/<slug>.md
- 不該用 frontmatter `status: locked-for-writer` 之外的值（structure 檔的鎖定標記）
- 不該修改 vault 內非 `structures/` 路徑下的檔案

## audit_checklist.md

本 skill 為「內容產出型」，**強制鏈式觸發 output-supervisor**。
