# 引用合法性規範

writer 在文章內引用任何資料來源，必須符合本檔規定。Stage 3 自檢與 supervisor 都會驗證。

## 4 類允許來源

per 系統設計（M-7 + W-3），只允許下列 4 類：

| 類別 | inline 標示 | 可信度 | 比例約束 |
|------|------------|-------|---------|
| Peer-reviewed 期刊論文 | `[author, year]` | 1.0 | ≥ 60%（WARN） |
| Preprint | `[author, year, PREPRINT]` | 0.7 | ≤ 25%（WARN if 超過） |
| 學位論文 | `[author, year, THESIS]` | 0.5 | 任何 thesis 引用需腳註說明 |
| 機構/政府技術報告 | `[author/org, year, REPORT]` | 0.6 | 無比例約束 |

不允許：

- 部落格文章（除非作者學術權威且引用脈絡需要）
- 媒體報導（新聞、雜誌）
- 維基百科
- 教科書（除非是「經典 textbook」歷史引用，需明確說明）
- 個人通訊（personal communication）
- 未具名來源

## Peer-reviewed 標示

預設形式（作者-年份）：

```
[Engel, 2007]                  單一作者
[Engel & Lee, 2007]            兩位作者
[Engel et al., 2007]           三位以上
[Engel, 2007a]                 同一年同一作者多筆
[Engel, 2007b]
```

References 章節：

```markdown
- Engel, G. S., Calhoun, T. R., Read, E. L., Ahn, T.-K., Mancal, T., Cheng, Y.-C., Blankenship, R. E., & Fleming, G. R. (2007). Evidence for wavelike energy transfer through quantum coherence in photosynthetic systems. *Nature*, 446(7137), 782-786. https://doi.org/10.1038/nature05678
```

格式：作者（all initials + 姓）, (年). 標題. *期刊*, 卷(期), 頁碼. DOI/URL.

## Preprint 標示

inline：

```
[Smith, 2024, PREPRINT]
```

References：

```markdown
- Smith, A. B., Jones, C. D. (2024). Title of preprint. *arXiv*. https://arxiv.org/abs/2401.12345 [PREPRINT, accessed 2026-04-30]
```

注意：

- venue 寫具體 preprint server（arXiv / medRxiv / bioRxiv / SSRN / ChemRxiv）
- 加 access date（preprint 內容可能被替換或撤回）
- 文章內若 preprint 比例 > 25% → supervisor WARN，建議在 Discussion 章節明確說明此議題依賴未發表研究

## Thesis 標示

inline：

```
[Smith, 2023, THESIS]
```

References：

```markdown
- Smith, A. B. (2023). *Title of dissertation* [Doctoral dissertation, University of XYZ]. ProQuest Dissertations Publishing. https://...
```

注意：

- 註明 Doctoral dissertation 或 Master's thesis
- 標出機構與來源（ProQuest / 機構 repository / 國家圖書館）
- 文章內**必須**有腳註說明為何依賴 thesis：

範例：

```markdown
此假設首見於 Smith 的博士論文 [Smith, 2023, THESIS]^1...

---

^1 此處引用碩博論文是因為相關質性研究尚未發表為期刊論文。Smith 的論文是該議題目前最完整的實證基礎。
```

## 機構/政府報告標示

inline：

```
[WHO, 2024, REPORT]              組織為作者
[Tan, 2023, REPORT]              個人作者，機構發布
```

References：

```markdown
- World Health Organization. (2024). *Title of report* (Report No. WHO/HQ/2024/X). https://...
- Tan, M. (2023). *Title*. National Institute of Health Research, Taiwan. https://...
```

注意：

- 機構名稱完整寫出，不縮寫（除非首次定義 abbreviation）
- 報告編號（如有）寫在標題後
- URL 必填

## 引用查驗

writer 在 Stage 2 寫到任何引用時：

1. 心裡驗證：這筆引用我能找到 metadata 嗎？
2. 不確定 → 在 frontmatter `pending_citations` 列出該引用：

```yaml
---
pending_citations:
  - "[Hore, 2016?] - 不確定具體 paper, 可能是 Annual Review article"
  - "[Engel, 2007] - 已查證"
---
```

3. 主動建議使用者鏈式觸發 lit-search skill 查驗（per W-7）

## 中英混雜處理（per W-8）

- 主文中文：引用 inline 仍用 `[author, year]`（不翻譯作者名）
- References 章節：**全用英文 metadata**（即使主文中文）

理由：原始期刊論文是英文，metadata 用英文一致性最高，未來搜尋與驗證最方便。

範例：

```markdown
## 主文（中文）

光合作用的 FMO 複合體中觀察到的長壽命相干態 [Engel et al., 2007]，
為量子生物學的核心證據之一...

## References（英文）

- Engel, G. S., Calhoun, T. R., Read, E. L., et al. (2007). Evidence for wavelike energy transfer through quantum coherence in photosynthetic systems. *Nature*, 446, 782-786.
```

## 引用比例的計算與報告

writer 在 Stage 3 自檢時，計算 References 章節的類別比例：

```python
total = peer_reviewed + preprint + thesis + report
peer_reviewed_pct = peer_reviewed / total
preprint_pct = preprint / total
```

寫入 frontmatter：

```yaml
sources_used:
  peer_reviewed: 12
  preprint: 3
  thesis: 1
  report: 2
  total: 18
peer_reviewed_pct: 0.667
preprint_pct: 0.167
```

supervisor 依此 verdict：

- peer_reviewed < 60% → WARN
- preprint > 25% → WARN
- thesis > 0 但無腳註說明 → CRITICAL FAIL
- 任何引用無法分類 → CRITICAL FAIL

## 違規處理

| 違規 | 級別 | 處理 |
|------|------|------|
| 未明確分類的引用（無法歸到 4 類之一） | CRITICAL | writer 必修，stop ship |
| Wikipedia / blog / 媒體報導引用 | CRITICAL | writer 必修 |
| 編造引用（無法查驗 metadata） | CRITICAL | writer 必修 |
| Preprint > 25% | WARN | 提示，使用者決定 |
| Peer-reviewed < 60% | WARN | 提示 |
| Thesis 無腳註 | CRITICAL | writer 必修 |
| 同一筆引用 inline 與 References 不一致 | CRITICAL | writer 必修 |

CRITICAL → writer 自檢失敗，重跑 Stage 2/3。連續 3 次仍 FAIL → 停下提示使用者人工介入（per W-2）。

## 格式工具

writer 應使用 markdown reference-style links 或保持 inline `[author, year]` 一致。

不要混用：

❌ 不對：

```markdown
研究 [Engel, 2007] 與 [Smith][^smith2024] 都顯示...

[^smith2024]: Smith et al. 2024 (footnote-style citation)
```

✅ 對（全 inline）：

```markdown
研究 [Engel, 2007] 與 [Smith et al., 2024] 都顯示...

## References

- Engel, G. S., et al. (2007). ...
- Smith, A. B., et al. (2024). ...
```

整篇文章用同一種引用格式。
