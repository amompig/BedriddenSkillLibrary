---
maintained_by: vault-cataloger
last_updated: 2026-05-02 07:00
total_files: 40
source_path: D:\\Obsidian\\TorchBase\\TorchBased\\Claude workspace\\Basic
---

# Claude basic Map of Contents

> 自動維護。請勿手動編輯。最後更新：2026-05-02 07:00

## 總覽

40 份檔案。詳細變更見 [CHANGELOG.md](./CHANGELOG.md)。

分類分布：build(6), cloud(13), define(2), plan(1), review(4), ship(5), verify(2), （根目錄）(7)

## 分類索引

### build（6）

- [api-and-interface-design](./Skills/api-and-interface-design.md) — > Contract-first 設計、Hyrum's Law（所有可觀察行為終將被依賴）、One-Version Rule、錯誤語意、邊界驗證
- [context-engineering](./Skills/context-engineering.md) — > 在對的時機、餵 agent 對的資訊
- [frontend-ui-engineering](./Skills/frontend-ui-engineering.md) — > 元件架構、設計系統整合、狀態管理、響應式設計、WCAG 2
- [incremental-implementation](./Skills/incremental-implementation.md) — > 用「薄垂直切片」的方式把功能一層一層加上去，每層都包含實作 + 測試 + 驗證 + 提交
- [source-driven-development](./Skills/source-driven-development.md) — > 每個框架決策都要以官方文件為依據，並在 code 或 PR 描述中標註來源
- [test-driven-development](./Skills/test-driven-development.md) — > Red-Green-Refactor 循環、測試金字塔 (80 單元 / 15 整合 / 5 E2E)、DAMP over DRY、Beyonce Rule…

### cloud（13）

- [AlloyDB Basics](./Skills/alloydb-basics.md) — > Google Cloud AlloyDB（PostgreSQL 相容、高效能資料庫）的基礎操作：建立實例、連線、SQL 查詢、向量索引
- [BigQuery Basics](./Skills/bigquery-basics.md) — > BigQuery 資料倉儲的查詢、匯入、管理：SQL 語法、外部表、排程查詢、成本控制
- [Cloud Run Basics](./Skills/cloud-run-basics.md) — > Cloud Run（無伺服器容器）部署與管理：打包容器、設定擴縮、掛網域、環境變數
- [Cloud SQL Basics](./Skills/cloud-sql-basics.md) — > Cloud SQL（MySQL / PostgreSQL / SQL Server 託管版）基礎操作：建立、備份、連線、私有 IP
- [Firebase Basics](./Skills/firebase-basics.md) — > Firebase 應用開發平台的基礎：Authentication、Firestore / Realtime DB、Hosting、Cloud Functi…
- [Gemini API in Agent Platform](./Skills/gemini-api.md) — > 在 Agent 平台中整合並呼叫 Gemini API（Google 生成式 AI 模型家族）的技能
- [Kubernetes Engine (GKE) Basics](./Skills/gke-basics.md) — > GKE（Google Kubernetes Engine）叢集部署與管理：cluster 建立、deployment、service、ingress、aut…
- [Recipe: Google Cloud Network Observability](./Skills/google-cloud-networking-observability.md) — > GCP 網路可觀測性 recipe：VPC Flow Logs、Network Intelligence Center、封包追蹤、防火牆規則稽核
- [Recipe: Authenticating to Google Cloud](./Skills/google-cloud-recipe-auth.md) — > Google Cloud 驗證設定 recipe：gcloud 登入、服務帳號、Application Default Credentials (ADC)、…
- [Recipe: Onboarding to Google Cloud](./Skills/google-cloud-recipe-onboarding.md) — > 新手導入 Google Cloud 的步驟 recipe：建立 organization / project、設定計費、啟用 API、IAM 基礎
- [Google Cloud Well-Architected Framework: Cost Optimization](./Skills/google-cloud-waf-cost-optimization.md) — > 依 Well-Architected Framework 的「成本最佳化」支柱協助檢視 GCP 花費：資源合適化、折扣方案、自動停機
- [Google Cloud Well-Architected Framework: Reliability](./Skills/google-cloud-waf-reliability.md) — > 依 Well-Architected Framework 的「可靠性」支柱給出系統設計建議：SLO 設計、錯誤預算、災難復原
- [Google Cloud Well-Architected Framework: Security](./Skills/google-cloud-waf-security.md) — > 依 Google Cloud Well-Architected Framework 的「安全性」支柱進行系統設計檢核與指引

### define（2）

- [idea-refine](./Skills/idea-refine.md) — > 用結構化的發散 / 收斂思考，把模糊的想法一步步逼近成具體提案
- [spec-driven-development](./Skills/spec-driven-development.md) — > 在寫任何程式碼前，先產出一份完整的 PRD（產品需求文件），包含目標、命令介面、結構、程式風格、測試策略、邊界案例

### plan（1）

- [planning-and-task-breakdown](./Skills/planning-and-task-breakdown.md) — > 把一份 spec 拆成數十個可獨立驗證的小任務，附上驗收條件與任務相依關係

### review（4）

- [code-review-and-quality](./Skills/code-review-and-quality.md) — > 五軸審查（功能性、設計、風格、測試、文件）+ 變更大小控制（~100 行/PR）+ 嚴重度標籤（Nit / Optional / FYI / Blockin…
- [code-simplification](./Skills/code-simplification.md) — > Chesterton's Fence（不懂為什麼存在就別移除）+ Rule of 500（檔案 <500 行才健康）
- [performance-optimization](./Skills/performance-optimization.md) — > 以測量為先，包含 Core Web Vitals (LCP/INP/CLS)、剖析工作流、bundle 分析、常見反模式偵測
- [security-and-hardening](./Skills/security-and-hardening.md) — > OWASP Top 10 防範 + 認證模式 + 祕密管理 + 相依稽核 + 三層邊界防護（輸入、處理、輸出）

### ship（5）

- [ci-cd-and-automation](./Skills/ci-cd-and-automation.md) — > Shift Left（越早越便宜）、Faster is Safer（快回饋才敢改）、feature flags、品質閘 pipeline、快速失敗回饋
- [deprecation-and-migration](./Skills/deprecation-and-migration.md) — > Code-as-liability 心態（程式碼是負擔不是資產）、區分強制 vs 建議性棄用、遷移模式、殭屍程式碼移除
- [documentation-and-adrs](./Skills/documentation-and-adrs.md) — > 架構決策紀錄（ADR）、API 文件、行內註解標準
- [git-workflow-and-versioning](./Skills/git-workflow-and-versioning.md) — > Trunk-based development、原子 commit、變更大小 ~100 行、commit 即存檔點（能獨立 revert）
- [shipping-and-launch](./Skills/shipping-and-launch.md) — > 發佈前檢查清單、feature flag 生命週期、分階段推出（canary → % roll-out → full）、回滾程序、監控告警

### verify（2）

- [browser-testing-with-devtools](./Skills/browser-testing-with-devtools.md) — > 透過 Chrome DevTools MCP 拿到瀏覽器執行時的真實資料：DOM 結構、console log、network request、perfor…
- [debugging-and-error-recovery](./Skills/debugging-and-error-recovery.md) — > 五步分流：**重現 → 定位 → 縮小 → 修復 → 防護**

### （根目錄）（7）

- [AI_Agent_與_Skill_完整教學](./AI_Agent_與_Skill_完整教學.md) — > Claude 中的智能代理與技能系統：概念、架構、使用與設計
- [AI_Agent_與_Skill_新手教學PPT](./AI_Agent_與_Skill_新手教學PPT.pptx)
- [Basic - Claude Agent & Skill 知識庫](./README.md) — > 這個資料夾是我的 Claude agent / skill 速查站
- [Skill 索引](./Skill 索引.md) — > 兩個 repo 的所有 skill 分類總表
- [如何同步更新 Skills](./如何同步更新 Skills.md) — > 當 GitHub 上的 repo 有新 skill 加入時，用這份指南把 Basic 資料夾同步到最新狀態
- [新手教學 - 從零開始用 Agent 與 Skill](./新手教學 - 從零開始用 Agent 與 Skill.md) — > 目標：看完這份文件後，你知道 **agent 是什麼、skill 是什麼、怎麼在 Claude 環境裡用它們、怎麼找到需要的 skill**
- [更新日誌](./更新日誌.md) — > 每次跑 `update-skills

## 最近 7 日新增 / 修改

| 日期 | 檔案 | 操作 |
|------|------|------|
| 2026-04-27 | [AI_Agent_與_Skill_新手教學PPT](./AI_Agent_與_Skill_新手教學PPT.pptx) | 新增 |
| 2026-04-27 | [AI_Agent_與_Skill_完整教學](./AI_Agent_與_Skill_完整教學.md) | 新增 |
| 2026-04-27 | [Skill 索引](./Skill 索引.md) | 新增 |
