# Description Quality Rubric (Rule 7)

`description` 是 SKILL.md frontmatter 中決定 skill 是否被自動觸發的關鍵欄位。寫得不好 → skill 在該被叫時沒被叫，或在不該被叫時誤觸。

本檔由 `skill-governance` 在 LLM 判斷階段使用：對 `audit.py` 回傳的 `descriptions` 字典每一筆，套用以下三要素判定 PASS / WARN。

---

## 三要素（必須全中才算 PASS）

### 要素 1：雙語觸發詞（中文 + 英文）

description 內必須**列舉**雙語觸發詞，使中英文使用者的自然語句都能命中。

✅ 範例（PASS）：
> Trigger on phrases like "make a board update", "Q1 board deck", "董事會 update", "季度 review", "all-hands deck", "全員會議簡報", "team weekly", "對團隊報告"...

❌ 失格：
- 只列英文觸發詞
- 只列中文觸發詞
- 只說「use when working with skills」這類抽象條件，沒有具體片語

### 要素 2：具體動詞 + 名詞片語

觸發詞應是「動詞 + 受詞」的形式，貼近使用者實際說話的方式。
- 「make X」「audit Y」「create Z」「查 W」「整理 W」「對 N 簡報」
- 純名詞（"pitch deck"、"investor presentation"）較弱，可作為輔助但不能只有名詞

### 要素 3：明確排除條款

description 必須說明**何時不該用**這支 skill，通常的寫法是點名 sibling skill 處理相關情境。

✅ 範例（PASS）：
> Do NOT use for auditing the content of a specific skill's deliverable (use output-supervisor for that), nor for creating/editing skills (use skill-creator).

> If the user asks for an investor pitch / fundraising deck → redirect to `startup-pitch-investor`.

❌ 失格：
- 完全沒有「do not」「instead use X」「redirect to Y」之類的句子
- 排除條款過於抽象，無法真正消歧義（例：「do not use for unrelated tasks」）

---

## 判定邏輯

對每個 skill 的 description：

| 要素 1 | 要素 2 | 要素 3 | 判定 |
|--------|--------|--------|------|
| ✅ | ✅ | ✅ | **PASS** |
| 任一缺失 | — | — | **WARN**（標明缺哪一項） |

---

## 報告寫法

在最終報告 §7 段落，對每個 WARN 的 skill 給：

```
- `<skill-name>`: WARN — 缺少要素 N（要素名稱）
  建議：<具體可寫進 description 的句子草稿>
```

對 PASS 的 skill 簡單列出即可：

```
- `<skill-name>`: PASS
```

---

## 邊界情況

- **新建立的 skill 還在草稿階段**：仍以同樣標準判定。不要因為「skill 還不完整」就跳過。
- **description 過長（>250 字）**：這不是判定要素之一，但若觀察到應在報告中以 INFO 補註。
- **觸發詞數量太少（< 4 個英文 + 4 個中文）**：可降為 WARN 並建議擴充。
- **要素 3 用 sibling skill 名但對方實際不存在**：標 WARN 並建議改寫。

---

## 給最終報告作者（Claude orchestrator）的指引

1. 不要照抄 description 全文進報告。只要寫該 skill 的判定結果 + 缺漏要素 + 修補建議。
2. 修補建議要具體到「可貼回 description 使用的句子」，不是抽象建議。
3. 若所有 skill 都 PASS，§7 直接寫「All skill descriptions PASS the rubric.」一行帶過。
