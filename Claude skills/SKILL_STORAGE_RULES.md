---
title: SKILL Storage Rules
purpose: 在使用 skill-creator 產出新 skill、或整理既有 skill 時應遵守的儲存與目錄慣例
last_updated: 2026-04-29
sources:
  - https://github.com/addyosmani/agent-skills (目錄/命名/progressive disclosure 慣例)
  - Anthropic 內建 skill (docx / pptx / pdf / skill-creator) 慣例 (references/ 與 scripts/ 放在 skill 內)
related_skills:
  - skill-governance: 對整個 repo 跑 §9 違規檢查清單的稽核 skill
  - output-supervisor: 對單一 skill 產出物做第二雙眼稽核的通用 skill
---

# SKILL Storage Rules

呼叫 `anthropic-skills:skill-creator` 之前**必先讀完此檔**。skill-creator 預設規則涵蓋寫作品質，但目錄結構、檔案命名、與多支 skill 共存時的歸類，由本檔規範。

## 1. Repository（skills 根目錄）配置

```
D:\Claude skills\
├── README.md                       # 根目錄導讀（每次新增/搬移結構時更新）
├── SKILL_STORAGE_RULES.md          # 本檔
├── <skill-name>/                   # 每支 skill 一個資料夾，名稱即 skill 名
├── <skill-name>/
└── _meta/                          # 所有「不是 skill」的檔案都歸這裡
    ├── templates/                  # 設計階段模板、藍本
    ├── stress-tests/               # 壓力測試紀錄、模擬演練
    ├── eval-tools/                 # 評估腳本、HTML 結果檢視器
    ├── backlog/                    # 版本待辦、未來規劃
    ├── workspaces/                 # skill-creator 跑出來的 *-workspace/ 評估產物
    └── audits/                     # 稽核 skill 的報告產物（不可進 skill 本體）
        ├── repo/                   # skill-governance 對整個 repo 的稽核報告
        └── output/<skill>/         # output-supervisor 對單一 skill 產出物的稽核報告
```

**硬規則**：根目錄只能出現「skill 資料夾」、`README.md`、`SKILL_STORAGE_RULES.md`、`_meta/`。任何其他檔案一律進 `_meta/` 對應子目錄。

## 2. 單一 skill 的目錄結構

採 Anthropic 慣例（references/ 在 skill 內，方便整支 skill 獨立移植）：

```
<skill-name>/
├── SKILL.md                # 入口；大寫檔名固定
├── references/             # 進階資料；progressive disclosure 載入
│   ├── persona.md
│   ├── data_verification.md
│   └── ...
├── scripts/                # （選用）skill 執行時呼叫的程式
└── evals/                  # （選用）skill 自己的 evals.json
    └── evals.json
```

**注意**：
- `SKILL.md` 一律大寫，其他檔案 lowercase + `_` 或 `-` 皆可（同一支 skill 內統一就好）。
- `references/` 內的檔案不可在 SKILL.md 外被預載，必須由 SKILL.md 在敘述中明確指示「Read `references/xxx.md`」。違反此原則就破壞了 progressive disclosure 的 token 節省效果。
- `evals/` 是評估產物的「定義」（測項與預期答案）；評估「執行結果」屬於工作產物，必須放到根目錄的 `_meta/workspaces/<skill-name>-workspace/`，**不可**留在 skill 內。

## 3. 命名規則

| 對象 | 規則 | 範例 |
|------|------|------|
| skill 資料夾名 | lowercase-kebab-case，名詞短語 | `startup-pitch-investor` |
| SKILL.md | 永遠大寫，副檔名小寫 | `SKILL.md` |
| references 內檔案 | snake_case 或 kebab-case，需具語意 | `competitor_moat_check.md` |
| frontmatter `name` | 與資料夾同名 | `name: startup-pitch-investor` |
| 多變體 skill | 同根字首 + 後綴變體名（不要用 v1/v2 數字） | `startup-pitch-investor` / `startup-pitch-internal` |

**禁止**：版本號塞進 skill 名（如 `xxx-v2`）、用底線當分隔（`startup_pitch_investor`）、混用大小寫資料夾名。

## 4. SKILL.md frontmatter

最低必填：

```yaml
---
name: <skill-name-同資料夾>
description: <一段話，必含使用觸發條件「Use when…」與「不要 trigger 於…」邊界>
---
```

`description` 是 skill 是否被自動觸發的關鍵欄位，需具備：
- 主動觸發詞（明確動詞 + 名詞，例如 "make a pitch deck", "投資人簡報"）
- 觸發語境的雙語列舉（中文 + 英文常見講法）
- 排除條件（指出不適用情境，避免誤觸）

可選欄位（非標準但有時有用）：`license`, `version`, `requires`（依賴的其他 skill）。如不需要，不要加。

## 5. Progressive disclosure（重要）

從 addyosmani/agent-skills 採用的核心原則：**SKILL.md 是入口，所有細節都該下放到 references/**。

判斷規則：
- SKILL.md 應該 **150 行以下**。超過代表細節該下放。
- 任何「清單型」內容（反例庫、檢核表、模板樣式、人設描述）一律下放到 `references/`。
- SKILL.md 只保留：When to use / Step 流程 / What to deliver / 跳轉到哪些 references。

## 6. 多支 skill 共享資產的處理

addyosmani 的 repo-root `references/` 慣例（多 skill 共享）**不採用**，因為會破壞 skill 獨立移植性。改用以下兩種方式之一：

1. **複製貼上**：兩支 skill 各自帶一份相同的 `references/persona.md`。維護成本小（若兩邊很久才會 diverge），可移植性最佳。
2. **模板 + 生成**：把共用內容放在 `_meta/templates/`，新增 skill 時複製過去。**禁止**在 skill 內用 symlink 或相對路徑跨 skill 引用。

## 7. 工作產物與評估資料的歸宿

呼叫 skill-creator 跑 evals 後，會產生 `<skill-name>-workspace/` 含 iteration / grading / outputs。這些**永遠**歸 `_meta/workspaces/`，不留根目錄、不混進 skill 本體。

稽核 skill 產生的報告檔案：
- `skill-governance` → `_meta/audits/repo/<timestamp>__<verdict>.md`
- `output-supervisor` → `_meta/audits/output/<source-skill>/<timestamp>__<verdict>.md`

`<verdict>` 為 `PASS` / `WARN` / `FAIL` 三選一（兩級嚴重度：CRITICAL FAIL 任何一條 → `FAIL`；只有 WARN → `WARN`；全綠 → `PASS`）。

## 8. 與 skill-creator 互動的標準流程

每次要產出新 skill，依序：

1. 讀 `SKILL_STORAGE_RULES.md`（本檔）。
2. 確認 skill 名（kebab-case，不衝突）、確認該 skill 不應併入既有 skill。
3. 呼叫 `anthropic-skills:skill-creator`，要求：
   - skill 資料夾建立在 `D:\Claude skills\<skill-name>\`。
   - SKILL.md 維持 150 行內，細節進 `references/`。
   - 不要在 skill 內留 workspace / eval 結果。
4. skill-creator 完成後，搬移所有非 skill 產出物到 `_meta/`。
5. 更新根目錄 `README.md`。
6. （重要）回讀 SKILL.md，檢查 frontmatter `description` 是否同時涵蓋中英觸發語與排除條件。
7. **呼叫 `skill-governance` 對整個 repo 跑稽核**，確認新 skill 沒有違反本檔任何規則。報告會落在 `_meta/audits/repo/`。若有 CRITICAL FAIL 必須修復後才算完成。

## 9. 鏈式觸發慣例（chain-triggering）

Skill 不能直接呼叫另一支 skill；觸發鏈由 Claude（orchestrator）執行。SKILL.md 內若需要鏈式觸發稽核 skill，固定寫法如下：

**內容產出型 skill（如 startup-pitch-*、biomedical-lit-search 等）**
SKILL.md 最後一個 step 寫：

```markdown
## Step N（最後一步）：產出後稽核

完成 deliverable 後，**必須**呼叫 `output-supervisor`，傳入：
- target_file: <剛才產出的檔案絕對路徑>
- source_skill: <本 skill 名>

把稽核結果中所有 CRITICAL FAIL 摘要呈現給使用者，詢問是否依建議修正後再交付。
```

**Repo 結構變動型流程（如 §8 skill-creator 流程）**
工作流文件最後一步呼叫 `skill-governance`，無需參數（預設掃 `D:\Claude skills\`）。

**鏈式觸發要件**
- 被鏈式觸發的 skill 必須標明 input contract（哪些參數來自前一支、哪些向使用者問）
- 被觸發 skill 不應再鏈式觸發第三支 skill（避免無限鏈）
- 鏈式觸發失敗（檔案不存在、source_skill 沒有 audit_checklist.md）時，被觸發 skill 需 graceful degrade 並提示使用者，不可硬中止整個任務

## 10. 違規檢查清單

整理 / review 既有 skill 時跑這份：

- [ ] 根目錄只剩 skill 資料夾 + README + SKILL_STORAGE_RULES + `_meta/`
- [ ] 每支 skill 都有 SKILL.md（大寫）且有合法 frontmatter
- [ ] 每支 skill 名稱符合 kebab-case
- [ ] 每支 skill 的 SKILL.md ≤ 150 行
- [ ] 沒有 skill 內含有 workspace / 評估結果 / 暫存產物
- [ ] 沒有 skill 用相對路徑跨 skill 引用
- [ ] 每支 skill description 含中英觸發詞 + 排除條件
- [ ] `_meta/` 子目錄分類正確（templates / stress-tests / eval-tools / backlog / workspaces）
