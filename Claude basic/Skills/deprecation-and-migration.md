---
title: deprecation-and-migration
repo: addyosmani/agent-skills
category: ship
stage: Ship — 有信心地上線
slash: none
created: 2026-04-24
updated: 2026-04-24
tags:
  - skill
  - skill/ship
  - addyosmani
  - repo/addyosmani
aliases:
  - deprecation-and-migration
source: https://github.com/addyosmani/agent-skills/tree/main/skills/deprecation-and-migration
---

# deprecation-and-migration

> Code-as-liability 心態（程式碼是負擔不是資產）、區分強制 vs 建議性棄用、遷移模式、殭屍程式碼移除。

## 階段

**Ship — 有信心地上線**

## 用途

Code-as-liability 心態（程式碼是負擔不是資產）、區分強制 vs 建議性棄用、遷移模式、殭屍程式碼移除。

## 觸發時機

移除舊 API、淘汰舊系統、版本升級導致 breaking change 時。

## 怎麼用

Skill 會規劃時間表：宣告 deprecated → 加 warning → 加 error → 最終移除。並提供 shim / migration script 降低使用者負擔。

## 相關 Skill

- [[api-and-interface-design]]
- [[documentation-and-adrs]]

## 來源

- 📦 Repo：[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)
- 📄 SKILL.md：<https://github.com/addyosmani/agent-skills/blob/main/skills/deprecation-and-migration/SKILL.md>
- 🔗 資料夾：<https://github.com/addyosmani/agent-skills/tree/main/skills/deprecation-and-migration>

---

*tag: #skill #skill/ship #addyosmani*
*回索引：[[Skill 索引]]*
