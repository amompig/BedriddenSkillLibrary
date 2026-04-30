---
title: debugging-and-error-recovery
repo: addyosmani/agent-skills
category: verify
stage: Verify — 證明可運作
slash: none
created: 2026-04-24
updated: 2026-04-24
tags:
  - skill
  - skill/verify
  - addyosmani
  - repo/addyosmani
aliases:
  - debugging-and-error-recovery
source: https://github.com/addyosmani/agent-skills/tree/main/skills/debugging-and-error-recovery
---

# debugging-and-error-recovery

> 五步分流：**重現 → 定位 → 縮小 → 修復 → 防護**。搭配 stop-the-line 規則（test 紅的時候全隊停手先修）。

## 階段

**Verify — 證明可運作**

## 用途

五步分流：**重現 → 定位 → 縮小 → 修復 → 防護**。搭配 stop-the-line 規則（test 紅的時候全隊停手先修）。

## 觸發時機

Test 失敗、build 破、行為異常、production incident 發生時。

## 怎麼用

Skill 禁止「看到 bug 直接猜解法」的反模式。要求先寫重現步驟，再定位最小失敗 case，修完後必須加 regression test。

## 相關 Skill

- [[test-driven-development]]
- [[browser-testing-with-devtools]]

## 來源

- 📦 Repo：[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)
- 📄 SKILL.md：<https://github.com/addyosmani/agent-skills/blob/main/skills/debugging-and-error-recovery/SKILL.md>
- 🔗 資料夾：<https://github.com/addyosmani/agent-skills/tree/main/skills/debugging-and-error-recovery>

---

*tag: #skill #skill/verify #addyosmani*
*回索引：[[Skill 索引]]*
