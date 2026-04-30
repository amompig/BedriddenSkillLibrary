---
title: 如何同步更新 Skills
created: 2026-04-24
updated: 2026-04-24
tags:
  - guide
  - sync
  - powershell
  - tutorial
aliases:
  - Sync Guide
  - 更新教學
---

# 如何同步更新 Skills

> 當 GitHub 上的 repo 有新 skill 加入時，用這份指南把 Basic 資料夾同步到最新狀態。

## 一鍵同步（最簡單）

1. 開啟 **PowerShell**（按 Win 鍵 → 打 PowerShell → Enter）
2. 切換到 Basic 資料夾：
   ```powershell
   cd "D:\Obsidian\TorchBase\TorchBased\Claude workspace\Basic"
   ```
3. 執行腳本：
   ```powershell
   .\update-skills.ps1
   ```

完成後你會看到：
- `Skills/` 底下每個 skill 的 `.md` 卡片都已更新
- `Skill 索引.md` 尾端多了一段「🔄 自動同步區」列出最新狀態
- `更新日誌.md` 多了一筆時間戳記紀錄

---

## 第一次執行前：解除執行限制

Windows 預設禁止執行未簽章的 .ps1 腳本。只需要做一次：

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

這只允許 **你這個使用者** 跑本機寫的腳本，安全性可控。

---

## 腳本做什麼事？

```
┌─────────────────────────────────────────┐
│ 1. 呼叫 GitHub API 列出兩個 repo        │
│    的所有 skill 資料夾                  │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│ 2. 下載每個 skill 的 SKILL.md 原文      │
│    並解析 frontmatter (name, desc)      │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│ 3. 把每個 skill 寫成 Basic/Skills/X.md │
│    （覆蓋舊版，保留檔名 wikilink 不破） │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│ 4. 在 Skill 索引.md 尾端附上一張        │
│    「最新全部 skill 簡表」              │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│ 5. 在 更新日誌.md 追加時間戳紀錄         │
└─────────────────────────────────────────┘
```

## 避免 GitHub API Rate Limit

未登入時 GitHub API 每小時只給 60 次請求，兩個 repo + 33 個 SKILL.md 會接近上限。建議設一個 personal access token：

1. 到 <https://github.com/settings/tokens>
2. 產生 classic token，**不需要任何權限**（只讀公開 repo 不用勾）
3. 在 PowerShell 設環境變數：
   ```powershell
   # 暫時（只影響本次 session）
   $env:GITHUB_TOKEN = "ghp_xxxxxxxxxxxx"

   # 永久（寫到使用者環境變數）
   [Environment]::SetEnvironmentVariable("GITHUB_TOKEN", "ghp_xxxx", "User")
   ```

有 token 後 rate limit 會提升到每小時 5000 次，完全夠用。

---

## 常見問題

### ❓ 腳本顯示「無法抓取 SKILL.md」

該 skill 的 SKILL.md 可能還沒 commit、或路徑不標準。腳本會用預設欄位產出卡片，你可以之後手動補內容。

### ❓ 我手動編輯了某個 skill 卡片，會被覆蓋嗎？

**會**。腳本每次都會完整重寫 `Skills/*.md`。如果你要加自己的筆記，建議：

- 開一份同名的 `<slug>-notes.md`（例如 `bigquery-basics-notes.md`）放個人筆記
- 或在 Obsidian 用 back-links、tags 連結，不直接改卡片主檔

### ❓ 索引檔 `Skill 索引.md` 被覆蓋了嗎？

**沒有被覆蓋**。腳本只在尾端的「🔄 自動同步區」區塊做 append/replace，主手工分類區（上半部）完整保留。

### ❓ 我想加第三個 repo？

編輯 `update-skills.ps1` 頂端的 `$Repos` 陣列，照現有格式新增一筆即可：

```powershell
@{
    Name    = "你的/repo"
    ApiUrl  = "https://api.github.com/repos/你的/repo/contents/你的路徑"
    RawBase = "https://raw.githubusercontent.com/你的/repo/main/你的路徑"
    WebBase = "https://github.com/你的/repo/tree/main/你的路徑"
    SubDir  = "yourname"
}
```

### ❓ 想排程自動跑？

用 Windows 工作排程器：

1. Win + R → `taskschd.msc`
2. 建立基本工作 → 名稱：`Sync Claude Skills`
3. 觸發：每週一次
4. 動作：啟動程式 → `powershell.exe`
5. 引數：`-NoProfile -ExecutionPolicy Bypass -File "D:\Obsidian\TorchBase\TorchBased\Claude workspace\Basic\update-skills.ps1"`

---

## 手動更新（不跑腳本的話）

如果不想跑腳本，也可以口頭請 Claude 做同一件事：

> 「請到 Basic 資料夾，重新抓取 addyosmani/agent-skills 與 google/skills 的最新 skill 清單，更新 Skills/ 底下的卡片與 Skill 索引.md 的表格」

Claude 會按原本的整理邏輯再做一次。

---

*tag: #guide #sync*
*相關：[[Skill 索引]]、[[更新日誌]]、[[新手教學 - 從零開始用 Agent 與 Skill]]*
