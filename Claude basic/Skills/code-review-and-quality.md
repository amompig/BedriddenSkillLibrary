---
title: code-review-and-quality
repo: addyosmani/agent-skills
category: review
stage: Review — 合併前品質閘
slash: /review
created: 2026-04-24
updated: 2026-04-24
tags:
  - skill
  - skill/review
  - addyosmani
  - repo/addyosmani
aliases:
  - code-review-and-quality
source: https://github.com/addyosmani/agent-skills/tree/main/skills/code-review-and-quality
---

# code-review-and-quality

> 五軸審查（功能性、設計、風格、測試、文件）+ 變更大小控制（~100 行/PR）+ 嚴重度標籤（Nit / Optional / FYI / Blocking）。

**Slash command**：`/review`

## 階段

**Review — 合併前品質閘**

## 用途

五軸審查（功能性、設計、風格、測試、文件）+ 變更大小控制（~100 行/PR）+ 嚴重度標籤（Nit / Optional / FYI / Blocking）。

## 觸發時機

合併前、或想自己先 self-review 一輪時。

## 怎麼用

輸入 `/review` 觸發。Skill 會逐檔檢視，標出 blocking issue / suggestion / nit，並引用 code review 最佳實踐原則。

## 相關 Skill

- [[code-simplification]]
- [[security-and-hardening]]
- [[test-driven-development]]

## 來源

- 📦 Repo：[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)
- 📄 SKILL.md：<https://github.com/addyosmani/agent-skills/blob/main/skills/code-review-and-quality/SKILL.md>
- 🔗 資料夾：<https://github.com/addyosmani/agent-skills/tree/main/skills/code-review-and-quality>

---

*tag: #skill #skill/review #addyosmani*
*回索引：[[Skill 索引]]*
