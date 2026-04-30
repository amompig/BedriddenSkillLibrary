# 領域寫作模板的執行細節

writer 接到 structure 檔的 `template:` 欄位後，依本檔執行對應寫作風格。

## medical-imrad

### 章節寫作要點

#### 1. Introduction

- 從臨床問題或文獻 gap 切入，避免泛泛之談
- 「重要性」要量化（疾病盛行率、死亡率、社會經濟負擔）
- 末段明確陳述本文的研究問題與目的（"This review aims to..."）
- 約 15-20% 字數

#### 2. Methods（PRISMA-style 文獻回顧時）

文獻搜尋章節必須含：

- 資料庫清單（PubMed, Embase, Cochrane Library, Web of Science）
- 搜尋字串範例（具體 boolean，不只「使用 keyword X 與 Y」）
- 搜尋日期範圍（從建庫至 YYYY-MM-DD）
- 語言限制（如 English only / 含中文）
- 納入標準（study design, population, intervention, outcomes）
- 排除標準

文獻篩選紀錄：

- 檢出 N 篇 → 標題篩選 → 全文篩選 → 最終納入 M 篇
- 文字描述即可，不必畫 PRISMA flow diagram（除非 structure 明示）

品質評估：

- 列具體工具名稱：CASP / GRADE / Cochrane Risk of Bias / Newcastle-Ottawa
- 描述如何處理低品質研究（剔除？敏感性分析？）

#### 3. Results

- 先呈現「文獻特徵總覽」表（含 study design, sample size, setting）
- 再依主題分節展開
- 使用「敘述合成」（narrative synthesis）整合異質研究——不是簡單並列
- 重要數值用「（95% CI: A-B, p < 0.05）」呈現
- 約 30-35% 字數

#### 4. Discussion

子節：
- 主要發現（重述但不重複 Results）
- 與既有文獻的對話（agreement / disagreement）
- 臨床意義（actionable insights）
- 限制（明列至少 3 項）
- 未來方向

避免：

- 不要在 Discussion 引入新資料（新資料屬於 Results）
- 不要對研究結果做過度推斷

#### 5. Conclusion

- 不超過 5%
- 以「核心 take-home message」收尾
- 不要列 5+ 點 bullet

### medical-imrad 風格細節

- 期刊風格參考：JAMA / NEJM / The Lancet 的 review article
- 主動語態優先，但 Methods 用被動可接受（「樣本以...保存」）
- 數字 < 10 寫文字（"three studies"），≥ 10 用阿拉伯數字
- 統計符號用標準寫法（p < 0.05, OR = 1.5, 95% CI: 1.2-1.8）

### 必須的引用格式

- Vancouver 或 APA 都可（structure 應指定）
- 預設 APA（與本系統 [author, year] inline 一致）
- 若 structure 指定 Vancouver → writer 改用 numbered citations [1], [2]，但 inline 仍標 author year 提供雙重資訊

## stem-imrad

### 章節寫作要點

#### 1. Introduction

- 從技術或科學問題切入
- 既有方法回顧（不只列出，要評論優缺）
- 末段陳述本文貢獻（"This work introduces..." / "We propose..."）
- 約 15-20%

#### 2. Methods / Methodology

實驗條件必寫：

- 樣本準備（純度、來源、處理）
- 設備規格（廠牌、型號、關鍵參數）
- 環境條件（溫度、壓力、濕度，若相關）
- 流程步驟（按順序，可重複）

資料分析：

- 統計方法（具體說明，不只「used statistical analysis」）
- 軟體與版本（如 Python 3.11, R 4.3, MATLAB R2024a）
- 重複次數（n = 3, three independent replicates）

#### 3. Results

- 先主結果（fig. 1 or table 1 對應）
- 後次要結果與 control 實驗
- 使用客觀描述（"The X showed Y" 而非 "We found that X is Y"）
- 量化數據呈現（mean ± SD, n = ?）
- 約 25-30%

#### 4. Discussion

- 結果解釋（為何看到這個 pattern）
- 與理論預測比較
- 與既有文獻比較
- 限制（明列）
- 後續工作

#### 5. Conclusion

- 簡短，重點 1-3 句

### stem-imrad 風格細節

- 期刊風格參考：Nature / Science / IEEE 的 research article
- 主動語態（"We measured..." / "The system exhibited..."）
- 數字一律阿拉伯（標準科學寫作）
- SI 單位（μm, ns, K, etc.）
- 圖表編號連貫（Figure 1, Figure 2, Table 1）

### 必須的引用格式

- IEEE numbered [1], [2] 或 APA author year（依 structure）
- 預設 APA（與本系統 inline 一致）

## generic（fallback）

### 章節寫作要點

無固定章節架構，依 structure 安排。但 writer 應確保：

- Introduction 章節定義範疇與目的
- Body 章節按論述邏輯展開（時序 / 主題 / 對比 / 因果）
- 章節間有銜接段落（不靠模板結構，全靠論述本身）
- Discussion 或 Synthesis 章節整合跨章節的論點
- Conclusion 收尾

### 寫作風格自由度

generic 模板下風格更彈性：

- 可用第一人稱（"In this essay, I argue..."），但仍避免「我覺得」這種口語
- 段落可較長（學術 essay 慣例）
- 引用慣例可用腳註（footnotes），但 writer 統一用 [author, year] inline
- 可有「對話式」結構（提問 → 探討 → 回應）

### supervisor 額外 WARN

generic 模板的文章 supervisor 加 WARN：

```markdown
本文使用 generic 模板（領域不匹配 medical-imrad 或 stem-imrad）。
請使用者確認文章結構是否合適該主題。
```

這 WARN 不阻擋交付，只提示。

## 模板執行的優先序

當 structure 與 style_rules 衝突時：

1. structure 檔的「writer 不該做的事」**最高優先**（明示約束）
2. style_rules 的硬規則
3. 模板特性
4. 一般學術寫作慣例

例：若 structure 說「不要用 IMRaD 章節」，即使 template == medical-imrad，也按 structure 不用 IMRaD。

## 跨領域文章的處理

structure 可能標 generic 但內容跨醫學與 STEM。writer 處理：

- 章節主題對應的領域用對應風格
- 例：醫學主題章節用 medical-imrad 引用慣例（含 PRISMA-like 描述若是文獻）
- STEM 主題章節用 stem-imrad 慣例
- 整篇 References 仍統一格式

writer 的判斷由 structure「writer 不該做的事」與「必寫的關鍵主張」校準——若 structure 沒明說，writer 自己合理判斷並在 frontmatter 註明。
