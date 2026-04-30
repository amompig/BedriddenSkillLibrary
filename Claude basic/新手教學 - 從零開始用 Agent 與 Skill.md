---
title: 新手教學 - 從零開始用 Agent 與 Skill
created: 2026-04-24
updated: 2026-04-24
tags:
  - tutorial
  - claude
  - agent
  - skill
  - beginner
aliases:
  - Agent 教學
  - Skill 教學
  - 新手入門
---

# 新手教學 — 從零開始用 Agent 與 Skill

> 目標：看完這份文件後，你知道 **agent 是什麼、skill 是什麼、怎麼在 Claude 環境裡用它們、怎麼找到需要的 skill**。

## 目錄

- [[#1. 最核心的三個觀念]]
- [[#2. Skill 是怎麼運作的？]]
- [[#3. 如何在 Claude 裡「用」一個 skill？]]
- [[#4. 實戰範例：做一份 PPT]]
- [[#5. 如何挑選 skill？]]
- [[#6. 常見問題 FAQ]]
- [[#7. 下一步]]

---

## 1. 最核心的三個觀念

### 1.1 什麼是 Agent？

**Agent = 會用工具幫你完成任務的 AI 助手。**

你跟一般 ChatGPT 聊天時，它只會「回答」。Agent 不一樣——它可以：

- 讀寫你電腦上的檔案
- 呼叫 API、搜尋網路
- 開啟應用程式、點擊畫面、輸入文字
- 連續執行多個步驟直到任務完成

Claude Code、Cowork、Claude in Chrome 都是 agent 產品。它們底層是同一個 Claude 模型，只是被包裝成不同用途。

### 1.2 什麼是 Skill？

**Skill = 一份寫給 agent 看的「SOP 操作手冊」。**

想像你請一位新助理做簡報，他可能：
- 用錯字體大小
- 版面排得很醜
- 忘了加頁碼

如果你事先給他一本「公司簡報製作規範」，他就會按規範做，品質穩定很多。Skill 就是那本規範。

技術上：skill 是一個資料夾，裡面有一份叫 `SKILL.md` 的檔案，內含：
- `description` — 這個 skill 是做什麼的
- 觸發關鍵字（例如「簡報」「.pptx」「投影片」）
- 詳細步驟、範例、參考資料

### 1.3 Skill vs Agent vs Slash Command 差在哪？

| 概念 | 是什麼 | 範例 |
|---|---|---|
| **Agent** | AI 助手本體 | Claude、Claude Code、Cowork |
| **Skill** | 給 agent 用的 SOP 手冊 | pptx skill、docx skill |
| **Slash command** | 使用者在輸入框打 `/xxx` 觸發的捷徑 | `/review`、`/plan` |
| **MCP** | 讓 agent 連外部系統的「水管」 | Slack MCP、GitHub MCP |

簡單類比：
- Agent 是「員工」
- Skill 是「員工看的工作手冊」
- Slash command 是「老闆喊的口令」
- MCP 是「員工對外聯絡的電話線」

---

## 2. Skill 是怎麼運作的？

### 2.1 觸發機制：「按需載入」

Claude 不會一次把所有 skill 都讀進記憶體，那樣會爆掉。它採用**按需載入**：

```
你說：「幫我做一份 PPT 介紹公司」
  ↓
Claude 看 skill 清單，發現 pptx skill 的 description 寫著
「任何涉及 .pptx / 簡報 / 投影片的任務都要用這個 skill」
  ↓
Claude 讀取 pptx/SKILL.md 的內容
  ↓
按 SKILL.md 指示的步驟執行
```

所以 **description 寫得好不好，直接決定 skill 會不會被觸發**。

### 2.2 Skill 的基本檔案結構

```
pptx/
├── SKILL.md              (主文件，必備)
├── references/           (附加資料，可選)
│   ├── template-guide.md
│   └── branding.md
└── scripts/              (可執行腳本，可選)
    └── create_deck.py
```

`SKILL.md` 的開頭通常長這樣：

```markdown
---
name: pptx
description: 任何涉及 .pptx 檔案的任務（建立、讀取、編輯簡報）...
---

# Creating Presentations

## Step 1: Gather requirements
...
```

上面那個 YAML 區塊叫 **frontmatter**，Claude 會先讀它判斷要不要載入 skill。

---

## 3. 如何在 Claude 裡「用」一個 skill？

### 3.1 三種使用方式

**方式 A — 自動觸發（最常見）**

你用自然語言描述任務，Claude 自己去找合適的 skill：

> 「幫我把這份文字整理成 Word 檔」 → Claude 自動載入 docx skill

**方式 B — 顯式指定 slash command**

有些 skill 會對應 slash command，你可以直接打：

> `/review`  → 觸發 code-review-and-quality skill
> `/ship`    → 觸發 shipping-and-launch skill

**方式 C — 安裝別人的 skill 集**

用 CLI 指令從 GitHub 安裝：

```bash
# 安裝 addyosmani 整組 20 個 skills
npx skills add addyosmani/agent-skills

# 安裝 Google Cloud 相關 skills
npx skills add google/skills
```

### 3.2 在 Claude Code / Cowork 裡的路徑

已安裝的 skill 通常放在：

```
~/.claude/skills/                  (macOS / Linux)
C:\Users\<你>\.claude\skills\      (Windows)
```

也可以放在你 repo 根目錄的 `.claude/skills/` 裡，這樣團隊所有成員都能共用。

### 3.3 自己寫 skill？

最小可用 skill 只需要一個 `SKILL.md`：

```markdown
---
name: commit-message
description: 幫使用者寫符合 conventional commit 格式的 commit 訊息。
  任何涉及 git commit、訊息撰寫、版本控制的任務都應觸發。
---

# Commit Message Skill

請使用 conventional commit 格式：
- `feat:` 新功能
- `fix:` 修 bug
- `docs:` 文件
- `chore:` 其他

訊息應該 <50 字，動詞開頭（用現在式）。
```

把這個檔案放在 `.claude/skills/commit-message/SKILL.md`，Claude 下次看到 commit 相關任務就會用它。

---

## 4. 實戰範例：做一份 PPT

我們走一遍完整流程，感受 skill 怎麼介入。

**Step 1 — 你輸入指令：**

> 「幫我做一份 5 頁的簡報，主題是 2026 Q1 業績回顧，公司是某科技業 startup」

**Step 2 — Claude 載入 skill：**

```
Claude: [檢查 skill 清單]
Claude: [發現 pptx skill，description 符合「簡報」關鍵字]
Claude: [讀取 pptx/SKILL.md]
```

**Step 3 — Claude 按 SKILL.md 指示執行：**

```
Claude: [SKILL.md 說「第一步要問清楚受眾、版面風格、關鍵訊息」]
Claude: 先問你幾個問題：
  - 受眾是投資人還是內部員工？
  - 要用 16:9 還是 4:3？
  - 有品牌主色嗎？
```

**Step 4 — 你回答後，Claude 產出 .pptx 檔：**

```
Claude: [用 python-pptx 套件產出檔案]
Claude: [存到 workspace 資料夾]
Claude: [給你 computer:// 連結方便開啟]
```

跟沒有 skill 的差別：**沒有 skill 時，Claude 可能直接丟一個排版糟糕的檔案給你；有 skill 時，它會先問清楚再做。**

---

## 5. 如何挑選 skill？

### 5.1 從任務反推

先想清楚「我要做什麼類型的任務」，再去 [[Skill 索引]] 查分類。

| 我要做... | 去找哪類 |
|---|---|
| 新專案的規格書 | `#skill/define` |
| 把需求拆成 tasks | `#skill/plan` |
| 寫程式、寫 UI | `#skill/build` |
| 測試、除錯 | `#skill/verify` |
| Code review、簡化 | `#skill/review` |
| 發佈、部署 | `#skill/ship` |
| Google Cloud 操作 | `#skill/cloud` |

### 5.2 看 description 判斷

打開 skill 卡片，看 `description` 欄位。好的 description 會明確寫：

- **什麼情況下用** — 例如「處理 .pptx 檔」
- **什麼情況下不用** — 例如「不要用於 Google Slides」
- **觸發關鍵字** — 例如「簡報、投影片、deck」

### 5.3 疊加使用

多個 skill 可以同時作用。例如做一個功能可能會用到：

- `spec-driven-development` (寫規格)
- `planning-and-task-breakdown` (拆任務)
- `test-driven-development` (寫測試)
- `code-review-and-quality` (自我審查)
- `shipping-and-launch` (上線)

Claude 會在每個階段自動切換對應 skill。

---

## 6. 常見問題 FAQ

**Q1：Skill 會不會被觸發錯？**

會。Description 寫得不夠精準時可能誤觸發，或該觸發的沒觸發。解法：看到 Claude 用錯 skill 時直接跟它說「請改用 X skill」。

**Q2：我可以關閉某個 skill 嗎？**

可以。把該 skill 的資料夾從 `.claude/skills/` 移除或改名，Claude 就找不到了。

**Q3：Skill 跟 MCP 衝突嗎？**

不衝突，兩者合作。MCP 提供「能力」（例如能連 Slack），skill 提供「方法論」（例如該在哪些情況發 Slack、要怎麼格式化訊息）。

**Q4：為什麼有些 skill 的 SKILL.md 很短，有些很長？**

短的是「入口」，詳細內容在 `references/` 裡的附加檔案。Claude 只會在需要時才去讀 references，節省 context。

**Q5：Skill 可以呼叫程式碼嗎？**

可以。Skill 資料夾裡的 `scripts/` 底下可放 .py / .sh 檔，SKILL.md 裡會指示「請執行 scripts/xxx.py」。

**Q6：更新 skill 會不會蓋掉我自己的客製？**

用 `npx skills add` 安裝的 skill 會寫到一個固定位置。你自己改的 skill 建議放**不同的資料夾**並用 git 管理，避免被覆蓋。

---

## 7. 下一步

- 去 [[Skill 索引]] 看看兩個 repo 有哪些 skill 可用
- 選一個看起來實用的 skill，打開它的卡片讀完
- 挑一個週末的小任務實際用用看
- 如果有新 skill 加入，跑 [[如何同步更新 Skills|update-skills.ps1]] 重新整理索引

---

## 延伸閱讀

- [addyosmani/agent-skills README](https://github.com/addyosmani/agent-skills) — 20 個工程級 skill 的完整說明
- [google/skills README](https://github.com/google/skills) — Google 官方的 Cloud skills
- [agentskills.io](https://agentskills.io/home) — skill 發佈平台
- [Anthropic Skills 官方文件](https://docs.claude.com) — 架構與最佳實踐

---

*tag: #tutorial #beginner*
