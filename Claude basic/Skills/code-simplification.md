---
title: code-simplification
repo: addyosmani/agent-skills
category: review
stage: Review — 合併前品質閘
slash: /code-simplify
created: 2026-04-24
updated: 2026-04-24
tags:
  - skill
  - skill/review
  - addyosmani
  - repo/addyosmani
aliases:
  - code-simplification
source: https://github.com/addyosmani/agent-skills/tree/main/skills/code-simplification
---

# code-simplification

> Chesterton's Fence（不懂為什麼存在就別移除）+ Rule of 500（檔案 <500 行才健康）。在保留行為的前提下降低複雜度。

**Slash command**：`/code-simplify`

## 階段

**Review — 合併前品質閘**

## 用途

Chesterton's Fence（不懂為什麼存在就別移除）+ Rule of 500（檔案 <500 行才健康）。在保留行為的前提下降低複雜度。

## 觸發時機

程式可以運作但難讀、難維護、難測試；或是發現同樣邏輯散落多處時。

## 怎麼用

輸入 `/code-simplify` 觸發。Skill 會識別重複、過度抽象、違反單一職責原則的片段，並提供安全的重構計畫。

## 相關 Skill

- [[code-review-and-quality]]
- [[documentation-and-adrs]]

## 來源

- 📦 Repo：[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)
- 📄 SKILL.md：<https://github.com/addyosmani/agent-skills/blob/main/skills/code-simplification/SKILL.md>
- 🔗 資料夾：<https://github.com/addyosmani/agent-skills/tree/main/skills/code-simplification>

---

*tag: #skill #skill/review #addyosmani*
*回索引：[[Skill 索引]]*
