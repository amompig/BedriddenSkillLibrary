# Stage 3 自檢規範

writer 在交付（chain output-supervisor）前的自檢。獨立於 supervisor，是 writer 的「第一道防線」。

## 自檢時機

- 模式 1（逐章交付）：每章寫完小自檢；全部章節完成後做全文自檢
- 模式 2（全文一氣呵成）：寫完做全文自檢
- 模式 3（先 outline 擴充）：Phase 2 結束後做全文自檢

每章小自檢項目較少；全文自檢全跑。

## 章節層級小自檢

每章寫完跑：

1. **字數**：actual 在 target ±25% 內？
2. **必寫主張覆蓋**：本章節對應 structure 中的「必寫主張」是否涵蓋？
3. **無孤立條列**：本章正文無單獨成段的條列？
4. **無 GPT-ism**：起手式沒有禁用語？
5. **引用格式**：本章用到的引用都用 [author, year]？

任一 FAIL：在章節內修正後重印。

## 全文自檢清單

對 published/<category>/<slug>.md 整篇跑：

### 風格層（CRITICAL）

- [ ] 開頭以外無孤立條列段落
- [ ] 條列出現的場景符合例外規則（並列含敘述包裹 / References / 表格）
- [ ] 無 GPT-ism 起手式
- [ ] 無「我覺得」「個人猜想」等主觀詞
- [ ] 章節間有銜接段落

### 架構符合度（CRITICAL）

- [ ] 章節順序與 structure 一致
- [ ] structure 中「必寫的關鍵主張」全部覆蓋
- [ ] 字數在 target_word_count ±25% 內
- [ ] frontmatter `revision_consumed` = structure 的 revision 號

### 引用合法性（CRITICAL）

- [ ] 所有引用屬 4 類允許來源
- [ ] References 章節格式統一
- [ ] inline `[author, year]` 與 References 對得上（每筆 inline 都有對應 References）
- [ ] 反向：每筆 References 都至少被 inline 引用過一次（無孤兒 reference）
- [ ] 無捏造引用（每筆有 title + venue/journal 可查驗）
- [ ] preprint / thesis / report 已標籤
- [ ] References 全英文 metadata（per W-8）

### 引用比例（⚠ WARN）

- [ ] peer-reviewed ≥ 60%
- [ ] preprint ≤ 25%
- [ ] thesis 引用有腳註說明

### 完整性（⚠ WARN）

- [ ] 無「TODO」「TBD」「[待補]」「[需補完]」殘留
- [ ] 無 `[?]` 模糊引用記號殘留
- [ ] 圖表（若有）標題編號連貫
- [ ] frontmatter 含 actual_word_count, sources_used (各類別), status

### 模板合規（⚠ WARN）

- [ ] medical-imrad: 章節含 IMRaD 結構，文獻回顧含 PRISMA-style 描述
- [ ] stem-imrad: 章節含 IMRaD，Methods 含實驗流程與資料分析
- [ ] generic: frontmatter 標 `template: generic`，supervisor 會 WARN

### 落地細節（⚠ WARN）

- [ ] 寫到 `published/<category>/<slug>.md`
- [ ] frontmatter category 對應路徑
- [ ] frontmatter status 為 `published` 或 `awaiting-review`

## 自檢失敗的處理

### CRITICAL FAIL

writer 嘗試自動修正：

1. 識別具體 FAIL 條目
2. 對應到文中段落
3. 修改該段落
4. 重跑自檢

最多 3 次 retry（per W-2 立場 + per chain X-2）。

連續 3 次 retry 仍 CRITICAL FAIL → 停下：

```markdown
**Stage 3 自檢連續 3 次 CRITICAL FAIL**：

- 嘗試 1：FAIL on <條目 A>
  修改：<具體修改 X>
- 嘗試 2：FAIL on <條目 B>
  修改：<具體修改 Y>
- 嘗試 3：FAIL on <條目 A 又出現>
  修改：<具體修改 Z>

我可能對你的寫作期望判斷不準。

當前草稿在 `drafts/<slug>.draft.md`。

建議：
1. 你檢視草稿，明確指出哪裡不對
2. 或你決定接受並標 `status: awaiting-review` 直接交付
3. 或暫停，明天再來

要怎麼做？
```

### WARN FAIL

WARN 不阻擋交付。處理方式：

- 寫進 frontmatter `audit_warnings` 列出
- 在交付訊息中提示使用者
- 使用者決定是否處理

```yaml
---
audit_warnings:
  - "preprint 比例 30%（>25%），請考慮在 Discussion 註明依賴未發表研究"
  - "本文使用 generic 模板，請確認結構合適"
---
```

## 自檢工具實作

writer 自檢時使用下列輔助計算：

### 條列偵測（CRITICAL）

掃描 markdown body（不含 frontmatter、開頭區塊「TL;DR」或「本文重點」、References、表格）：

- 若連續 ≥ 2 個 list item 不被前後敘述包裹 → 標為「孤立條列段落」
- 「敘述包裹」定義：list 前後 1 段內有 ≥ 50 字的敘述段落（非 list、非標題）

### 字數計算

per `references/style_rules.md` Rule 8（中英分別計算）。

排除：

- frontmatter
- markdown syntax（連結 URL、code block 內容）
- References 章節（單獨計算）

主文字數對應 frontmatter `actual_word_count`，References 字數另計。

### 引用一致性檢查

從 inline 抽取所有 `[author, year]` 與 `[author, year, MARKER]`，去重。

從 References 章節抽取所有條目（每行以 `-` 開頭）。

對比：

- inline 多 → CRITICAL（有 inline 沒對應 references）
- References 多 → WARN（孤兒 reference）

### GPT-ism 偵測

正則匹配下列 phrase（lowercase）：

- "在快速變遷的"
- "在當今.*時代"
- "眾所週知"
- "不可否認的是"
- "歸根究底"
- "in today's fast-paced"
- "let's dive into"
- "it goes without saying"

命中即 CRITICAL FAIL。

### 主觀詞偵測

匹配：

- "我覺得"
- "我認為"
- "個人猜想"
- "我相信"

但允許：

- "本文認為"
- "本研究認為"
- "依現有證據"
- "this review proposes"
- "this work argues"

命中後用 context 確認（前後 20 字內是否有「依」「依據」「本文」這類客觀化框架）。

## 自檢報告

每次自檢結果（PASS / WARN / CRITICAL）寫進 `drafts/<slug>.self-review.json`：

```json
{
  "slug": "quantum-biology-coherence-verification",
  "review_at": "2026-04-30T15:42:00+08:00",
  "verdict": "WARN",
  "critical_failures": [],
  "warnings": [
    {"item": "preprint_pct", "value": 0.30, "threshold": 0.25}
  ],
  "stats": {
    "actual_word_count": 6840,
    "target_word_count_range": "6000-8000",
    "sources_used": {
      "peer_reviewed": 12,
      "preprint": 6,
      "thesis": 1,
      "report": 1,
      "total": 20
    }
  }
}
```

供 supervisor 參考（不取代 supervisor 自己的 audit，只是 hint）。
