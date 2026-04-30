---
title: Basic - Claude Agent & Skill 知識庫
created: 2026-04-24
updated: 2026-04-24
tags:
  - MOC
  - claude
  - agent
  - skill
  - index
aliases:
  - Home
  - Basic 首頁
---

# Basic — Claude Agent & Skill 知識庫

> 這個資料夾是我的 Claude agent / skill 速查站。包含新手教學、兩個主要 skill 儲存庫（addyosmani & google）的索引，以及未來同步用的腳本。

## 從哪裡開始？

- 完全沒用過 skill → [[新手教學 - 從零開始用 Agent 與 Skill]]
- 想找某個特定功能的 skill → [[Skill 索引]]
- 想更新 skill 清單 → [[如何同步更新 Skills]]
- 查看上次更新時間 → [[更新日誌]]

## 資料夾結構

```
Basic/
├── README.md                                (本檔，Obsidian Home)
├── 新手教學 - 從零開始用 Agent 與 Skill.md   (Tutorial)
├── Skill 索引.md                             (主索引 + 分類表)
├── 如何同步更新 Skills.md                     (腳本使用教學)
├── 更新日誌.md                                (每次同步的紀錄)
├── update-skills.ps1                         (PowerShell 同步腳本)
└── Skills/                                   (每個 skill 一張卡片)
    ├── addyosmani/   (20 張卡片，分 6 大類)
    └── google/       (13 張卡片，Cloud 類)
```

## 兩個 Repo 速覽

| Repo | 作者 | 定位 | Skill 數 | 主題 |
|---|---|---|---|---|
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | Addy Osmani (Google Chrome) | 工程師級別的 AI 編碼工作流 | 20 | 規格、測試、審查、上線 |
| [google/skills](https://github.com/google/skills) | Google 官方 | Google Cloud 操作技能 | 13 | GCP、BigQuery、GKE、Firebase |

## 相關標籤

在 Obsidian 搜尋列輸入以下標籤可快速過濾：

- `#skill/define` — 釐清需求類
- `#skill/plan` — 拆解任務類
- `#skill/build` — 實作類
- `#skill/verify` — 驗證類
- `#skill/review` — 審查類
- `#skill/ship` — 發佈類
- `#skill/cloud` — Google Cloud 類
- `#tutorial` — 教學文件
- `#reference` — 參考資料

---

*上次同步：2026-04-24*
*來源：[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) + [google/skills](https://github.com/google/skills)*
