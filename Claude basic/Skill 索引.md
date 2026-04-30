---
title: Skill 索引
created: 2026-04-24
updated: 2026-04-24
tags:
  - MOC
  - skill
  - index
  - claude
aliases:
  - Skill Index
  - 技能索引
---

# Skill 索引

> 兩個 repo 的所有 skill 分類總表。點擊名稱可跳到對應 skill 卡片，點擊 🔗 可開啟 GitHub 原始檔。

## 快速查找

想用功能找 skill？試試這張表：

| 我的情境              | 可能需要的 skill                            |
| ----------------- | -------------------------------------- |
| 有模糊想法想探索          | [[idea-refine]]                        |
| 開新專案先寫規格          | [[spec-driven-development]]            |
| 把大任務拆成小任務         | [[planning-and-task-breakdown]]        |
| 寫程式前要先寫測試         | [[test-driven-development]]            |
| 寫 UI、設計系統         | [[frontend-ui-engineering]]            |
| 設計 API            | [[api-and-interface-design]]           |
| 測試瀏覽器上的 app       | [[browser-testing-with-devtools]]      |
| Test 失敗想除錯        | [[debugging-and-error-recovery]]       |
| 自我 code review    | [[code-review-and-quality]]            |
| 感覺 code 太亂想簡化     | [[code-simplification]]                |
| 安全強化              | [[security-and-hardening]]             |
| 效能最佳化             | [[performance-optimization]]           |
| 寫 commit / 開 PR   | [[git-workflow-and-versioning]]        |
| 設定 CI/CD          | [[ci-cd-and-automation]]               |
| 汰除舊 API           | [[deprecation-and-migration]]          |
| 寫 ADR / 文件        | [[documentation-and-adrs]]             |
| 準備上線              | [[shipping-and-launch]]                |
| 用 Gemini API      | [[gemini-api]]                         |
| 用 BigQuery        | [[bigquery-basics]]                    |
| 用 Cloud Run / GKE | [[cloud-run-basics]] / [[gke-basics]]  |
| 初入門 GCP           | [[google-cloud-recipe-onboarding]]     |
| GCP 安全 / 可靠性 / 成本 | [[google-cloud-waf-security]] 等 WAF 系列 |

---

## Part 1 — addyosmani/agent-skills

**20 個 skill，分 6 個階段 (Define → Plan → Build → Verify → Review → Ship)。**
覆蓋 AI 編碼代理的完整工程生命週期。

> 📦 Repo：[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)
> 🏷️ 授權：MIT　　👤 作者：Addy Osmani (Google Chrome)

### 🎯 Define — 釐清要做什麼

| Skill                       | 用途                    | Slash   | 連結                                                                                        |
| --------------------------- | --------------------- | ------- | ----------------------------------------------------------------------------------------- |
| [[idea-refine]]             | 結構化發散/收斂思考，把粗略想法轉具體提案 | —       | [🔗](https://github.com/addyosmani/agent-skills/tree/main/skills/idea-refine)             |
| [[spec-driven-development]] | 在寫程式前先產出 PRD 規格文件     | `/spec` | [🔗](https://github.com/addyosmani/agent-skills/tree/main/skills/spec-driven-development) |
|                             |                       |         |                                                                                           |

### 📋 Plan — 拆解任務

| Skill | 用途 | Slash | 連結 |
|---|---|---|---|
| [[planning-and-task-breakdown]] | 把規格拆成小而可驗證的任務 | `/plan` | [🔗](https://github.com/addyosmani/agent-skills/tree/main/skills/planning-and-task-breakdown) |

### 🔨 Build — 寫程式

| Skill                          | 用途                       | Slash    | 連結                                                                                           |
| ------------------------------ | ------------------------ | -------- | -------------------------------------------------------------------------------------------- |
| [[incremental-implementation]] | 薄垂直切片、feature flag、可回滾   | `/build` | [🔗](https://github.com/addyosmani/agent-skills/tree/main/skills/incremental-implementation) |
| [[test-driven-development]]    | Red-Green-Refactor、測試金字塔 | —        | [🔗](https://github.com/addyosmani/agent-skills/tree/main/skills/test-driven-development)    |
| [[context-engineering]]        | 在對的時機餵 agent 對的 context  | —        | [🔗](https://github.com/addyosmani/agent-skills/tree/main/skills/context-engineering)        |
| [[source-driven-development]]  | 每個決策都以官方文件為依據並標註         | —        | [🔗](https://github.com/addyosmani/agent-skills/tree/main/skills/source-driven-development)  |
| [[frontend-ui-engineering]]    | 元件架構、設計系統、無障礙            | —        | [🔗](https://github.com/addyosmani/agent-skills/tree/main/skills/frontend-ui-engineering)    |
| [[api-and-interface-design]]   | Contract-first、錯誤語意、邊界驗證 | —        | [🔗](https://github.com/addyosmani/agent-skills/tree/main/skills/api-and-interface-design)   |

### ✅ Verify — 證明可運作

| Skill | 用途 | Slash | 連結 |
|---|---|---|---|
| [[browser-testing-with-devtools]] | 用 Chrome DevTools MCP 拿即時執行資料 | `/test` | [🔗](https://github.com/addyosmani/agent-skills/tree/main/skills/browser-testing-with-devtools) |
| [[debugging-and-error-recovery]] | 五步分流：重現→定位→縮小→修復→防護 | — | [🔗](https://github.com/addyosmani/agent-skills/tree/main/skills/debugging-and-error-recovery) |

### 🔍 Review — 合併前品質閘門

| Skill | 用途 | Slash | 連結 |
|---|---|---|---|
| [[code-review-and-quality]] | 五軸審查、變更 ~100 行、嚴重度標籤 | `/review` | [🔗](https://github.com/addyosmani/agent-skills/tree/main/skills/code-review-and-quality) |
| [[code-simplification]] | Chesterton's Fence、Rule of 500 | `/code-simplify` | [🔗](https://github.com/addyosmani/agent-skills/tree/main/skills/code-simplification) |
| [[security-and-hardening]] | OWASP Top 10、祕密管理、三層邊界 | — | [🔗](https://github.com/addyosmani/agent-skills/tree/main/skills/security-and-hardening) |
| [[performance-optimization]] | Core Web Vitals、bundle 分析、反模式偵測 | — | [🔗](https://github.com/addyosmani/agent-skills/tree/main/skills/performance-optimization) |

### 🚀 Ship — 有信心地上線

| Skill | 用途 | Slash | 連結 |
|---|---|---|---|
| [[git-workflow-and-versioning]] | Trunk-based、原子 commit、~100 行 | — | [🔗](https://github.com/addyosmani/agent-skills/tree/main/skills/git-workflow-and-versioning) |
| [[ci-cd-and-automation]] | Shift Left、Faster is Safer、品質閘 | — | [🔗](https://github.com/addyosmani/agent-skills/tree/main/skills/ci-cd-and-automation) |
| [[deprecation-and-migration]] | 強制 vs 建議性棄用、殭屍程式碼移除 | — | [🔗](https://github.com/addyosmani/agent-skills/tree/main/skills/deprecation-and-migration) |
| [[documentation-and-adrs]] | ADR、API 文件、記錄「為什麼」 | — | [🔗](https://github.com/addyosmani/agent-skills/tree/main/skills/documentation-and-adrs) |
| [[shipping-and-launch]] | 發佈檢查清單、分階段推出、回滾 | `/ship` | [🔗](https://github.com/addyosmani/agent-skills/tree/main/skills/shipping-and-launch) |

### 🧩 額外資源（非 skill 但在 repo 裡）

- **Agent Personas** — `agents/` 資料夾：`code-reviewer`、`test-engineer`、`security-auditor`
- **Reference Checklists** — `references/` 資料夾：`testing-patterns.md`、`security-checklist.md`、`performance-checklist.md`、`accessibility-checklist.md`

---

## Part 2 — google/skills

**13 個 skill，目前全部在 `cloud/` 分類底下。**
Google 官方推出的 Google Cloud 操作 skill 集合。

> 📦 Repo：[google/skills](https://github.com/google/skills)
> 🏷️ 授權：Apache 2.0　　👤 作者：Google 官方
> 📅 建立：2026-03-31（仍積極開發中）

### ☁️ Cloud — Google Cloud 操作

| Skill | 用途 | 連結 |
|---|---|---|
| [[gemini-api]] | 呼叫 Gemini API、整合生成式 AI | [🔗](https://github.com/google/skills/tree/main/skills/cloud/gemini-api) |
| [[alloydb-basics]] | AlloyDB (PostgreSQL 相容資料庫) 基礎 | [🔗](https://github.com/google/skills/tree/main/skills/cloud/alloydb-basics) |
| [[bigquery-basics]] | BigQuery 資料倉儲查詢、匯入、管理 | [🔗](https://github.com/google/skills/tree/main/skills/cloud/bigquery-basics) |
| [[cloud-run-basics]] | Cloud Run 無伺服器容器部署管理 | [🔗](https://github.com/google/skills/tree/main/skills/cloud/cloud-run-basics) |
| [[cloud-sql-basics]] | Cloud SQL (MySQL/PG/SQL Server) 基礎 | [🔗](https://github.com/google/skills/tree/main/skills/cloud/cloud-sql-basics) |
| [[firebase-basics]] | Firebase (Auth/DB/Hosting) 基礎 | [🔗](https://github.com/google/skills/tree/main/skills/cloud/firebase-basics) |
| [[gke-basics]] | GKE (Google Kubernetes Engine) 基礎 | [🔗](https://github.com/google/skills/tree/main/skills/cloud/gke-basics) |
| [[google-cloud-recipe-onboarding]] | GCP 新手導入 recipe：建專案/計費 | [🔗](https://github.com/google/skills/tree/main/skills/cloud/google-cloud-recipe-onboarding) |
| [[google-cloud-recipe-auth]] | GCP 驗證 recipe：gcloud/服務帳號/ADC | [🔗](https://github.com/google/skills/tree/main/skills/cloud/google-cloud-recipe-auth) |
| [[google-cloud-networking-observability]] | VPC Flow Logs、Network Intelligence | [🔗](https://github.com/google/skills/tree/main/skills/cloud/google-cloud-networking-observability) |
| [[google-cloud-waf-security]] | Well-Architected Framework：安全性支柱 | [🔗](https://github.com/google/skills/tree/main/skills/cloud/google-cloud-waf-security) |
| [[google-cloud-waf-reliability]] | Well-Architected Framework：可靠性支柱 | [🔗](https://github.com/google/skills/tree/main/skills/cloud/google-cloud-waf-reliability) |
| [[google-cloud-waf-cost-optimization]] | Well-Architected Framework：成本最佳化 | [🔗](https://github.com/google/skills/tree/main/skills/cloud/google-cloud-waf-cost-optimization) |

---

## Part 3 — Slash Commands 對照表

addyosmani repo 附帶的 7 個 slash command：

| Slash | 對應 Skill | 階段 |
|---|---|---|
| `/spec` | [[spec-driven-development]] | Define |
| `/plan` | [[planning-and-task-breakdown]] | Plan |
| `/build` | [[incremental-implementation]] | Build |
| `/test` | [[browser-testing-with-devtools]] | Verify |
| `/review` | [[code-review-and-quality]] | Review |
| `/code-simplify` | [[code-simplification]] | Review |
| `/ship` | [[shipping-and-launch]] | Ship |

---

## 安裝指令

```bash
# 安裝 addyosmani 全組
npx skills add addyosmani/agent-skills

# 安裝 Google Cloud 組
npx skills add google/skills

# 只裝某一個
npx skills add addyosmani/agent-skills/skills/code-review-and-quality
```

---

*上次整理：2026-04-24*
*標籤：#MOC #skill #index*
