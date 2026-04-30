# 領域寫作模板

per A-7，使用者選 medical-imrad 與 stem-imrad 兩個模板。不匹配的領域 fallback 到 generic。

## 模板選擇邏輯

Round 0 結束後依「文體類型」與使用者明示偏好決定模板：

| 文體 / 領域 | 預設模板 |
|-----------|---------|
| 醫學文獻回顧 | medical-imrad |
| 臨床研究論述 | medical-imrad |
| 生醫實驗報告 | medical-imrad |
| 物理 / 化學 / 工程實驗 | stem-imrad |
| STEM 領域論文 | stem-imrad |
| 人文 / 社科 / 跨領域 / 其他 | generic |
| 使用者明示偏好 | 依使用者 |

interview 檔的 Q7 也可由使用者明示。

## medical-imrad 模板

### 章節結構（典型）

```
1. Introduction（XX% 字數）
   - 1.1 背景與重要性
   - 1.2 文獻 gap 或臨床問題
   - 1.3 本文目的與範疇

2. Methods（YY% 字數）
   - 2.1 文獻搜尋策略（PRISMA-style 描述）
   - 2.2 納入與排除標準
   - 2.3 資料萃取與品質評估

3. Results（YY% 字數）
   - 3.1 文獻特徵總覽
   - 3.2 主題 A 結果
   - 3.3 主題 B 結果
   - ...

4. Discussion（YY% 字數）
   - 4.1 主要發現
   - 4.2 與既有文獻的對話
   - 4.3 臨床意義
   - 4.4 限制
   - 4.5 未來方向

5. Conclusion（XX% 字數）

6. References
```

### 字數分配建議

- Introduction: 15-20%
- Methods: 15-20%
- Results: 30-35%
- Discussion: 25-30%
- Conclusion: 5-10%

### PRISMA-style 描述

Methods 章節若是文獻回顧，必須包含 PRISMA flow 描述：

- 資料庫搜尋（PubMed、Embase、Cochrane 等）
- 搜尋字串（具體寫出 boolean）
- 納入排除標準
- 紀錄篩選流程（檢出 N 篇 → 標題篩選 → 全文篩選 → 最終納入 M 篇）

writer 寫 Methods 時可以選擇是否畫 flow diagram；不畫的話用文字精確描述。

### 必寫的方法學細節

- 文獻搜尋日期範圍
- 語言限制
- Quality assessment 工具（CASP / GRADE / Cochrane Risk of Bias）

## stem-imrad 模板

### 章節結構（典型）

```
1. Introduction（XX% 字數）
   - 1.1 問題背景
   - 1.2 既有方法回顧
   - 1.3 本文貢獻

2. Methods / Methodology（YY% 字數）
   - 2.1 實驗設計
   - 2.2 材料與設備
   - 2.3 流程
   - 2.4 資料分析方法

3. Results（YY% 字數）
   - 3.1 主結果
   - 3.2 次要結果

4. Discussion（YY% 字數）
   - 4.1 結果解釋
   - 4.2 與理論預測的比較
   - 4.3 限制
   - 4.4 後續工作

5. Conclusion（XX% 字數）

6. References
```

### 字數分配建議

- Introduction: 15-20%
- Methods: 20-25%
- Results: 25-30%
- Discussion: 20-25%
- Conclusion: 5%

### 必寫的方法學細節

- 實驗條件（溫度、壓力、樣品濃度等）
- 統計方法（若適用）
- 可重複性資訊（樣本數、重複次數）

## generic 模板（fallback）

### 章節結構

```
1. Introduction（15-20%）
   - 1.1 主題背景
   - 1.2 本文範疇與目的

2. Body chapters（多章，60-70%）
   - 各章依論述邏輯展開

3. Discussion / Synthesis（10-15%）
   - 跨章節整合

4. Conclusion（5-10%）

5. References
```

### 適用情境

- 人文（文學評論、哲學論述）
- 社會科學（無實驗的論述型文章）
- 跨領域 essay
- 政策分析
- 其他無標準模板的文體

### 寫作風格注意

generic 模板下 writer 應特別注意：

- 章節間銜接段落要清楚（無 IMRaD 結構支撐時，邏輯流要靠論述本身串）
- 引用慣例可能不只是 [author, year]——人文常用腳註，但本系統一律 [author, year] 統一處理（per A-7）
- supervisor 對 generic 模板會額外 WARN 一筆，提示「此文章使用通用模板，請使用者確認結構合適」

## 模板選擇後的 architect 行為

選定模板後，Round 1 架構草稿依模板章節結構生成。但 architect 不是「死板照抄模板」：

- 章節數可增減（依實際 target_word_count 與內容需求）
- 章節順序可微調（例如先 Background 再 Method 是慣例，但 narrative 風格可調）
- 子節結構彈性大

模板的核心約束：

- 必有 References 章節
- 結構符合該模板的「閱讀流」期待（讀者看到 Methods 期待找到方法說明）
- 字數分配大致符合建議比例

## 切換模板（罕見）

迭代中使用者要求換模板（例如從 medical-imrad 換成 generic）：

- architect 重做 Round 1（保留主題與已討論的關鍵點）
- 重新生成草稿時明確說「依新模板重做」
- 修改 target structure 時 frontmatter `template:` 欄位也更新

## 領域與模板的對應參考

| 領域 / 內容 | 建議模板 |
|------------|---------|
| 醫學系統性回顧 | medical-imrad（PRISMA） |
| 臨床指引 / 診療建議 | medical-imrad（去掉 PRISMA） |
| 生醫實驗論文 | medical-imrad 或 stem-imrad（依領域慣例） |
| 物理理論論文 | stem-imrad |
| 工程方法論 | stem-imrad |
| 計算機論文 | stem-imrad |
| 哲學論述 | generic |
| 文學評論 | generic |
| 社會學論述（非實驗） | generic |
| 心理學實驗 | stem-imrad（IMRaD 適用） |
| 政策白皮書 | generic |
| 跨領域評論 | generic |
| 教學講義 | generic（章節依教學流） |

## 未來擴充

新增模板的步驟：

1. 在本檔新增區塊定義其章節結構與字數比例
2. 在 SKILL.md 明確列出新模板名稱
3. 更新 audit_checklist.md 「template 欄位是 ... 之一」清單
4. 不破壞既有模板

候選未來模板：

- `humanities-essay`：人文 essay 細化版
- `policy-analysis`：政策分析特化（含 stakeholder 章節）
- `case-study`：個案研究結構（背景 → 案例描述 → 分析 → 推廣）

目前不實作。使用者需要時再擴充。
