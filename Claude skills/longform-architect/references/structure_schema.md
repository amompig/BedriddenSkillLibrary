# structures/<slug>.md schema

architect 最終 output。同時是 writer 的 input 與未來重寫的 reference。

## 檔案位置

```
D:\Obsidian\TorchBase\TorchBased\Claude workspace\Basic\structures\<slug>.md
```

slug 為 kebab-case，最長 50 字元。例：

- `quantum-biology-coherence-verification`
- `cardiac-arrest-em-management-2026`
- `cross-platform-frontmatter-survey`

## 完整 schema

```markdown
---
title: <可讀標題（中文或英文）>
slug: <kebab-case-slug>
authored_by_architect: longform-architect
locked_at: YYYY-MM-DDTHH:MM:SS+TZ
target_word_count: <int 或 "X-Y" range>
audience: <一句話描述目標讀者>
genre: <文體類型>
template: medical-imrad | stem-imrad | generic
status: locked-for-writer
revision: v1
---

# 架構：<title>

## 寫作指令給 writer

文體要求：
- 長文敘述，避免單獨條列文件
- 開頭可有條列摘要（最多 5 點）
- 引用優先序：peer-reviewed > preprint > thesis > tech-report
- 引用標示：[author, year] inline，References 章節列完整
- 語氣：學術冷靜，避免「我覺得」「個人猜想」

引用範圍：
- ☑ peer-reviewed 期刊論文
- ☑ preprint（arXiv, medRxiv, SSRN, ChemRxiv 等，標註 [PREPRINT]）
- ☑ 學位論文（標註 [THESIS]，需腳註說明）
- ☑ 機構/政府技術報告（標註 [REPORT]）

必寫的關鍵主張（writer 不可省略）：
1. <主張 1>
2. <主張 2>
3. ...

writer 不該做的事：
- <不該做 1>
- <不該做 2>

## 章節大綱

### 1. <章節名>（XXX 字）
- 子節重點 1
- 子節重點 2
- 內容指引：<要涵蓋什麼，避免什麼>

### 1.1 <子節名>（YYY 字）
- ...

### 2. <章節名>（XXX 字）
...

### N. References（XXX 字）
- 預期引用方向（writer 自行擴展）：
  - <方向 1>
  - <方向 2>

## 預期引用方向（writer 自行擴展）

- 領域 A：
  - 必引：<具體 paper / author 1>
  - 必引：<具體 paper / author 2>
  - 視需要：<...>
- 領域 B：
  - ...

## 給 writer 的提醒

- 中英混雜：References 全用英文 metadata
- preprint 比例：低於 25% 為佳；超過要在文中註明依賴未發表研究的理由
- 章節順序：依此架構，**不要**自行重組（重組需回頭觸發 architect 微調模式）
- 字數軟強制：±25% 內可接受，超過交付時要提示
```

## frontmatter 欄位定義

| 欄位 | 必要 | 說明 |
|------|------|------|
| `title` | ✅ | 可讀標題，中文或英文 |
| `slug` | ✅ | kebab-case，與檔名一致 |
| `authored_by_architect` | ✅ | 永遠 `longform-architect` |
| `locked_at` | ✅ | ISO 8601 時間戳 |
| `target_word_count` | ✅ | int 或 "X-Y" 範圍 |
| `audience` | ✅ | 一句話 |
| `genre` | ✅ | 文體類型（自由文字，但建議用模板對應分類） |
| `template` | ✅ | medical-imrad / stem-imrad / generic |
| `status` | ✅ | 永遠 `locked-for-writer`（writer 讀到此值才接手） |
| `revision` | ✅ | v1, v2, ... |
| `cited_sources_planned` | 選 | 預期引用論文清單（list） |

## 章節結構

### 編號慣例

- H3（`###`）為章節標頭（1, 2, 3, ...）
- H4（`####`）為子節標頭（1.1, 1.2, ...）
- 不超過 H4

### 字數預估

每個章節（H3）必須有預估字數：

```markdown
### 1. 引言（800 字）
```

子節（H4）若有也要預估：

```markdown
#### 1.1 量子生物學的歷史脈絡（300 字）
```

字數加總應 ±20% 落在 frontmatter `target_word_count`。

### 章節內容

每章節下列**重點**而非完整段落：

✅ 對：

```markdown
### 2. 理論背景（1200 字）
- 量子相干態在生物系統的時間尺度問題
- 室溫退相干的挑戰
- 「環境輔助量子傳輸」這個概念
- 內容指引：聚焦能解釋「為何此議題仍未定論」的理論張力
```

❌ 不對（夾帶論述）：

```markdown
### 2. 理論背景（1200 字）

量子相干態在生物系統面臨一個根本性難題：在室溫環境下，
退相干時間極短，這意味著任何量子效應都應該迅速崩解。然而，
過去十年的實驗暗示這個直覺可能不完全正確...

[繼續寫了 200 字 — 這已經是寫成文章了，不是架構]
```

architect audit 會標 CRITICAL 違規：「dynamics 段落 > 200 字，已是寫文不是架構」。

## 「必寫的關鍵主張」區塊

這些是 writer **不能省略**的核心內容。例：

```markdown
必寫的關鍵主張（writer 不可省略）：
1. 鳥類磁感的相干態爭議：論證雙方陣營
2. 光合作用的量子相干態實驗證據：列出至少 3 個關鍵實驗
3. 為何此議題仍未定論：歸因於哪些技術或概念瓶頸
```

writer audit 會檢查這些主張全部覆蓋。

## 「writer 不該做的事」區塊

避免 writer 漂移的負面提醒。例：

```markdown
writer 不該做的事：
- 不要把任何章節改成單純條列
- 不要省略反方論述章節（這是文章誠實性的核心）
- 不要使用學術語境外的口語（「我覺得」、「個人猜想」）
- 不要編造引用（每筆 reference 必須能在 Google Scholar 找到 metadata）
```

## 「預期引用方向」區塊

不一定要列具體 paper，但應給 writer 起點。例：

```markdown
預期引用方向（writer 自行擴展）：
- 光合作用 FMO 複合體：Engel et al. 2007、Lee et al. 2007、Panitchayangkoon 2010
- 鳥類磁感：Hore series（2011, 2016, 2018）、Ritz 2000
- 對振動理論的批評：Wilde et al. 2018, Tegmark 2000
- 退相干理論基礎：Schlosshauer 2007 textbook
```

## 維護規則

- 同一 slug 不同 revision **共用同檔**（覆蓋寫，per A-5 不留歷史版本）
- 修改後 frontmatter `revision` 加 1，`locked_at` 更新
- writer 在 Stage 0 讀此檔時必須驗證 `status: locked-for-writer`，否則拒絕接手

## 與 writer 的合約

writer 接到 structure 檔的承諾：

- 章節順序依此架構
- 「必寫的關鍵主張」全部覆蓋
- 「writer 不該做的事」全部遵守
- 字數軟強制 ±25% 內

writer 違反時：

- audit_checklist FAIL → output-supervisor 阻擋交付
- writer 自己 Stage 3 自檢時也應發現
