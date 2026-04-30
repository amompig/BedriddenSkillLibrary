# 多輪迭代協議

architect 與使用者的對話迭代規範。Round 0 到 Round Final 的每輪行為。

## 整體紀律

1. **不靜默改動**：每輪明確列「本輪改了什麼」。使用者沒提到要改的部分，不主動改。
2. **不主動推進**：未得到使用者回應前，不假設可以推進到下一輪。
3. **不寫檔直到最終**：所有迭代在對話中進行，**不**寫 structures/<slug>.md。

## Round 0：議題理解

### 必問項目（5 項）

per A-1，5 個必問項目，可分為「必問」與「選問」處理：

**必問**：
1. 目標讀者
2. 大致字數
3. 文體類型

**選問（依答案 follow-up）**：
4. 已有素材
5. 立場 / 主軸論點

完整呈現方式：

```markdown
我會幫你規劃一篇關於 <主題> 的長文。先確認幾件事：

1. **目標讀者**是誰？（跨領域學者 / 同領域專家 / 科普讀者 / 其他）
2. **大致字數**？（短：3000 字內 / 中：5000-8000 / 長：10000+ / 不確定請建議）
3. **文體類型**？（文獻回顧 / 觀點論述 / 個案研究 / 教學介紹）
```

得到上述 3 項後，依答案決定要不要追問 4-5：

- 若文體類型是「文獻回顧」或「論述」→ 追問「已有素材？」與「立場？」
- 若文體類型是「個案研究」→ 追問「個案是？」
- 若文體類型是「教學介紹」→ 追問「讀者已知什麼？預期學到什麼？」

### Round 0 結束條件

5 項（或對等的追問項目）都有答案 → 進 Round 1。

若使用者答「不知道」「請你決定」→ architect 自己合理選默認，但在 Round 1 開頭明確聲明：「我假設目標讀者是 X、字數 Y、文體 Z。如果不符你預期請告訴我。」

## Round 1：架構初稿

### 行動清單

1. 依模板（medical-imrad / stem-imrad / generic）寫架構草稿
2. 在對話中印出（不寫檔）：
   - 預擬章節大綱（含預估字數）
   - 各章重點
   - 引用方向預估
3. 主動問 3-5 個關鍵點
4. 若使用者沒提供文獻 → 建議鏈式觸發 lit-search skill

### 架構草稿格式

對話中呈現如下（這是 chat 內容，不寫檔）：

```markdown
**架構草稿 v1**

預估目標字數：X 字（你說的範圍是 X-Y）

### 1. 章節 A（XXX 字）
- 重點 1
- 重點 2

### 2. 章節 B（XXX 字）
...

### References（XXX 字）
- 預期引用方向：Engel 2007 系列、Hore 系列、...

---

幾個關鍵點請你回應：

1. **章節 A** 中要不要加入 X 子節？
2. 章節 B 與 C **順序**：先回顧證據還是先講理論？
3. 是否要把 **退相干批評**獨立成一章？
4. 字數分配是否合理（章節 A 比 B 重）？
5. 我的「預期引用方向」漏掉什麼？
```

### Round 1 結束條件

使用者回應上述問題，但不一定全答完。只要有實質回應 → 進 Round 2 修訂。

## Round 2..N：修訂迭代

### 每輪行動

1. 依使用者回應修訂草稿
2. 印出修訂版時，**明確列出本輪改了什麼**：

```markdown
**架構草稿 v2 — 本輪改動**

- 章節 A 加入 1.3 子節「環境輔助量子傳輸」
- 章節 B 改為先理論後證據（你建議的順序）
- 退相干批評獨立為章節 4
- 引用方向加入 Wilde et al. 2019

---

[完整修訂版章節大綱]

---

請你看看是否往對的方向。如果這版可以了請說「架構通過」；如果還有要改的地方請告訴我。
```

3. 等使用者回應，不主動推進

### 終止條件

per `references/termination_tokens.md`：

- 使用者明確說 token 之一 → 進 Round Final
- 模稜兩可表態 → architect 反問確認，**不**直接推進

### 反問範例

使用者說「OK 好像可以」：

```markdown
我聽到「OK 好像可以」，但不確定這是「架構定案」還是「方向對但細節再修」。

要進入 Round Final（落地寫 structures 檔，交棒給 writer），還是再迭代一輪？
```

## Round Final：落地

### 行動

1. 寫 `D:\Obsidian\TorchBase\TorchBased\Claude workspace\Basic\structures\<slug>.md`（per `references/structure_schema.md`）
2. 寫「交棒摘要」於對話：

```markdown
**架構已落地：[slug]**

📁 **檔案位置**：`D:\Obsidian\TorchBase\TorchBased\Claude workspace\Basic\structures\<slug>.md`
📐 **目標字數**：X 字
📋 **章節數**：N 章
🎯 **必寫關鍵主張**：
  1. ...
  2. ...

**給 writer 的提醒**：
- ...
- ...

要交棒給 longform-writer 開始撰寫嗎？（你說「開寫」「交棒給 writer」我就 chain 過去）
```

3. chain output-supervisor 稽核
4. supervisor PASS → 等使用者交棒回應；FAIL → 提示修正

### Round Final 後

使用者說「開寫」「交棒」「開始撰寫」→ orchestrator chain 到 longform-writer

使用者說「等等再想想」→ structure 檔保留，下次直接從那裡接力

## Round Loop：微調模式

writer 撰寫途中發現架構有缺，會停下提示使用者重啟 architect。

### 微調模式行動

1. 讀現有 `structures/<slug>.md`
2. 識別 writer 反饋的問題章節
3. **只**改受影響章節，保留其他原樣
4. 在對話印出修訂版（同 Round 2..N 規範）
5. 使用者同意 → revision +1，寫回同檔
6. 不同意 → 繼續迭代

### 範圍紀律

- 不主動「順便改其他章節」
- 不重寫 frontmatter 除了 revision 與 locked_at
- 不刪掉「給 writer 的提醒」區塊（writer 仍要看）

## 與其他 skill 的互動邊界

### 不主動鏈

architect **不**鏈式觸發：

- biomedical-lit-search
- alphaxiv-paper-lookup
- clinical-research-ideation
- longform-writer（除非使用者明確說「交棒」）

### 主動建議鏈

architect 在 Round 0 結束後，若使用者沒提供文獻，**主動建議**：

```
你還沒提供素材。建議先跑 biomedical-lit-search（生醫類）或 alphaxiv-paper-lookup（arxiv 類）找文獻，
回來給我這份清單，我可以基於實際素材規劃。

要先去找文獻嗎？或者你想直接讓我憑領域知識規劃？
```

使用者說「先找」→ architect 暫停，等使用者跑完 lit-search 回來
使用者說「直接規劃」→ architect 進 Round 1，引用方向用領域常識
