# Round 0 Interview 檔模式

per A-9 使用者選 (c) 混合：Round 0 可離線填問卷檔，Round 1 起回到對話迭代。

## 觸發語

「為主題 X 生成問卷」「離線回答」「給我一份 interview 檔」

或 architect 在對話模式中問完一輪問題後，使用者抱怨「問題太多想離線回答」→ architect 主動問「要切換到 interview 檔模式嗎？」

## interview 檔的位置

```
D:\Obsidian\TorchBase\TorchBased\Claude workspace\Basic\structures\_pending\<slug>.interview.md
```

`_pending\` 資料夾用來放尚未完成的 architect 工作。架構通過後 architect 把 `_pending\<slug>.interview.md` 與最終 `structures\<slug>.md` 一起留著（_pending 內可保存歷史紀錄，但不影響 writer）。

## interview 檔 schema

```markdown
---
slug: <kebab-case-slug>
topic: <主題>
created_at: YYYY-MM-DD HH:MM
status: pending-fillin
---

# 架構規劃 Interview：<主題>

> 請離線填寫下方各題答案，填完後在對話中說「讀問卷繼續」。
> 部分題目可空著或寫「請 architect 提建議」，architect 會依空白項目主動發問。

## Q1: 目標讀者是誰？

例：跨領域學術讀者，預設無量子背景 / 同領域專家 / 一般科普讀者

**你的答案**：

[請在這裡填寫]

## Q2: 大致字數？

例：6000-8000 字 / 3000 字 / 不確定，請建議

**你的答案**：

[請在這裡填寫]

## Q3: 文體類型？

選一個或寫自由文字：

- [ ] 文獻回顧（系統性整理某領域近期研究）
- [ ] 觀點論述（提出明確立場與支持論證）
- [ ] 個案研究（深入分析特定案例）
- [ ] 教學介紹（向初學者解釋概念）
- [ ] 其他：____

**你的答案**：

[請在這裡填寫]

## Q4: 是否已有手邊文獻或素材？

例：
- 已有 Engel et al. 2007、Hore 2016 等
- 還沒，請建議用 biomedical-lit-search 找
- 部分有，列在 D:\...

**你的答案**：

[請在這裡填寫]

## Q5: 希望的「立場」或「主軸論點」？

例：
- 量子相干態在生物中是真實但有限的現象
- 反對振動理論
- 沒立場，回顧式中性整理
- 請 architect 提幾個候選方向

**你的答案**：

[請在這裡填寫]

## Q6（選填）: 不希望寫到的內容？

例：
- 不要碰宗教 / 民俗領域的解釋
- 不要重複我前一篇 X 的內容
- 不要超過 4 章

**你的答案**：

[請在這裡填寫]

## Q7（選填）: 領域 / 寫作模板偏好？

選一個：

- [ ] medical-imrad（醫學/生醫，含 PRISMA / IMRaD 結構）
- [ ] stem-imrad（STEM 實驗類，IMRaD 古典結構）
- [ ] generic（通用結構，由 architect 決定）

**你的答案**：

[請在這裡填寫]

## Q8（選填）: 還有什麼想告訴 architect？

[請在這裡填寫]
```

## 生成 interview 檔的流程

當使用者要求「為主題 X 生成問卷」：

1. 從 X 推測 slug（kebab-case，最長 50 字元）
2. 確認 slug 無衝突（`_pending/<slug>.interview.md` 不存在；存在則加數字後綴）
3. 寫 interview 檔到 `_pending/<slug>.interview.md`
4. 提示使用者：「Interview 檔已生成於 [path]。請打開填答後說『讀問卷繼續』。」
5. architect 結束本回合，等使用者回應

## 讀填好 interview 檔的流程

當使用者說「讀問卷繼續」或同義：

1. 找出最近修改的 `_pending/*.interview.md` 檔
2. 解析每個 Q 之後的「**你的答案**」區塊
3. 對於空白或寫「請 architect 提建議」的題目：
   - 在 Round 1 主動問
   - 不直接默認推測
4. 對於有答案的題目：
   - 進 Round 1 直接基於答案
   - architect 不重複問

## 修改 interview 檔（少見）

若使用者填完問卷後想改某題答案，可直接編輯 `_pending/<slug>.interview.md` 再說「重新讀問卷」。architect 會：

1. 重新解析 interview 檔
2. 比較與上次的答案差異
3. 若 Round 1 已開始 → 提示「答案 Q3 從 X 變成 Y，會影響架構章節 N，要重新規劃這部分嗎？」

## 完成後的 interview 檔狀態

架構通過後（Round Final 寫了 `structures/<slug>.md`）：

- interview 檔留在 `_pending/<slug>.interview.md`（不刪）
- 修改 frontmatter `status: completed`
- 加 frontmatter `completed_structure: <相對路徑>` 指向最終 structure
- 未來重看 interview 檔可知該主題的初始想法

## interview 檔中的常見錯誤處理

| 場景 | 處理 |
|------|------|
| Q1-Q5（必填）有空白 | architect Round 1 反問 |
| 使用者填的 target word count 不合理（< 500 或 > 50000） | 確認是否真要這個範圍 |
| 文體選了多項或寫成自由文字無法解析 | 在 Round 1 確認 |
| Q4 列了文獻清單但格式無法解析 | 在 Round 1 請使用者確認，或建議鏈式 lit-search |

## interview 檔不適用的場景

- 使用者已在對話中明確回答問題 → 用對話模式更快
- 使用者要寫的是接續既有架構（微調模式）→ 不需要 interview
- 主題很簡單（短文 < 2000 字）→ 對話 1-2 回合即可
