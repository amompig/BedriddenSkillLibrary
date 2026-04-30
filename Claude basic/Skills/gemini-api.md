---
title: Gemini API in Agent Platform
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
  - Gemini API in Agent Platform
  - gemini-api
source: https://github.com/google/skills/tree/main/skills/cloud/gemini-api
---

# Gemini API in Agent Platform

> 在 Agent 平台中整合並呼叫 Gemini API（Google 生成式 AI 模型家族）的技能。涵蓋模型選擇、prompt 設計、streaming、function calling 等。

## 分類

**Google Cloud**（google/skills repo 目前唯一的分類）

## 用途

在 Agent 平台中整合並呼叫 Gemini API（Google 生成式 AI 模型家族）的技能。涵蓋模型選擇、prompt 設計、streaming、function calling 等。

## 觸發時機

你要讓 Claude 或其他 agent 能呼叫 Gemini、或在自己的應用裡嵌入 Gemini 生成功能時。

## 怎麼用

安裝到本機後，Claude 會在偵測到相關關鍵字（如 `gemini api`、對應產品名稱）時自動載入並依 SKILL.md 的步驟操作。

```bash
# 單獨安裝這個 skill
npx skills add google/skills/skills/cloud/gemini-api

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
- 📄 SKILL.md：<https://github.com/google/skills/blob/main/skills/cloud/gemini-api/SKILL.md>
- 🔗 資料夾：<https://github.com/google/skills/tree/main/skills/cloud/gemini-api>

---

*tag: #skill #skill/cloud #google #gcp*
*回索引：[[Skill 索引]]*
