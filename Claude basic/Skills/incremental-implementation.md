---
title: incremental-implementation
repo: addyosmani/agent-skills
category: build
stage: Build — 寫程式
slash: /build
created: 2026-04-24
updated: 2026-04-24
tags:
  - skill
  - skill/build
  - addyosmani
  - repo/addyosmani
aliases:
  - incremental-implementation
source: https://github.com/addyosmani/agent-skills/tree/main/skills/incremental-implementation
---

# incremental-implementation

> 用「薄垂直切片」的方式把功能一層一層加上去，每層都包含實作 + 測試 + 驗證 + 提交。搭配 feature flags、安全預設、可回滾。

**Slash command**：`/build`

## 階段

**Build — 寫程式**

## 用途

用「薄垂直切片」的方式把功能一層一層加上去，每層都包含實作 + 測試 + 驗證 + 提交。搭配 feature flags、安全預設、可回滾。

## 觸發時機

任何跨多檔案的變更，或需要在 main 分支上安全推進的功能。

## 怎麼用

Skill 強調 commit 小步快跑，每次提交都能 pass CI、可以獨立 revert。適合做大型 refactor 或新功能上線。

## 相關 Skill

- [[test-driven-development]]
- [[git-workflow-and-versioning]]
- [[shipping-and-launch]]

## 來源

- 📦 Repo：[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)
- 📄 SKILL.md：<https://github.com/addyosmani/agent-skills/blob/main/skills/incremental-implementation/SKILL.md>
- 🔗 資料夾：<https://github.com/addyosmani/agent-skills/tree/main/skills/incremental-implementation>

---

*tag: #skill #skill/build #addyosmani*
*回索引：[[Skill 索引]]*
