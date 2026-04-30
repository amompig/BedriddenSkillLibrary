---
title: Recipe: Authenticating to Google Cloud
repo: google/skills
category: cloud
slash: none
created: 2026-04-24
updated: 2026-04-24
tags:
  - skill
  - skill/cloud
  - google
  - repo/google
  - gcp
aliases:
  - Recipe: Authenticating to Google Cloud
  - google-cloud-recipe-auth
source: https://github.com/google/skills/tree/main/skills/cloud/google-cloud-recipe-auth
---

# Recipe: Authenticating to Google Cloud

> Google Cloud 驗證設定 recipe：gcloud 登入、服務帳號、Application Default Credentials (ADC)、Workload Identity。

## 分類

**Google Cloud**（google/skills repo 目前唯一的分類）

## 用途

Google Cloud 驗證設定 recipe：gcloud 登入、服務帳號、Application Default Credentials (ADC)、Workload Identity。

## 觸發時機

第一次設定本機或 CI 環境連線 GCP、或在排查「為什麼我的 SDK 跑不動」時。

## 怎麼用

安裝到本機後，Claude 會在偵測到相關關鍵字（如 `google cloud recipe auth`、對應產品名稱）時自動載入並依 SKILL.md 的步驟操作。

```bash
# 單獨安裝這個 skill
npx skills add google/skills/skills/cloud/google-cloud-recipe-auth

# 或裝整組 Google Cloud skills
npx skills add google/skills
```

## 相關 Skill

- [[google-cloud-recipe-onboarding]] — GCP 新手建議先看
- [[google-cloud-recipe-auth]] — 設定認證是前置條件
- [[google-cloud-waf-security]] — 做安全檢核
- [[google-cloud-waf-reliability]] — 做可靠性檢核
- [[google-cloud-waf-cost-optimization]] — 控制成本

## 來源

- 📦 Repo：[google/skills](https://github.com/google/skills)
- 📄 SKILL.md：<https://github.com/google/skills/blob/main/skills/cloud/google-cloud-recipe-auth/SKILL.md>
- 🔗 資料夾：<https://github.com/google/skills/tree/main/skills/cloud/google-cloud-recipe-auth>

---

*tag: #skill #skill/cloud #google #gcp*
*回索引：[[Skill 索引]]*
