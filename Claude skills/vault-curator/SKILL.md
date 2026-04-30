---
name: vault-curator
description: |
  多源聚合圖書館館長 skill。維護 D:\Bedridden Library\ 作為公開展示廳，
  從多個本地 source（如 Obsidian vault、skill repo）依各自白名單同步檔案到對應子資料夾，
  最後對整個 Bedridden Library 做 git commit + push 到 GitHub。
  
  使用觸發條件：
  - 「跑同步」「同步到 GitHub」「上傳到 Bedridden」「觸發 curator」「執行 daily sync」
  - 「mirror Obsidian / Claude skills」「push 到 GitHub」「commit 今天的變更」
  - 「新增 source X」「修改白名單」「加入排除清單」（白名單 / source 編輯）
  - 「Claude skills 的 X 不要公開」「pocus 不要進 git」
  - 排程環境每日 07:00 自動觸發（schedule task: bedridden-library-daily-sync）
  
  不要 trigger 於：
  - 純 Obsidian 內部編目需求（用 internal-cataloger）
  - Bedridden Library 端公開編目（用 vault-cataloger）
  - 寫文章 / 規劃架構（用 longform-architect / longform-writer）

requires:
  - output-supervisor (可選，用於手動稽核 audit_checklist)
---

# vault-curator

> 「展示廳的多源聚合管理員」。每日從多個本地 source，依各自的白名單規則 rsync-同步檔案到 D:\Bedridden Library\，並對整個 Bedridden Library 做 git commit + push。

## 核心紀律

- **永不破壞性操作**：禁止 force push、reset --hard、rebase。任何「需要判斷」的狀況停下來通知使用者。
- **白名單心智模型**：預設「什麼都不進 git」，要進就明確登記。隱私邊界靠物理隔離（Bedridden Library vs Obsidian），不靠 .gitignore 規則。
- **Source 解耦**：每個 source 有自己的白名單檔，互不干擾。
- **Chain 紀律**：上游 FAIL 時不嘗試下游（vault-cataloger）。

## 執行模式判斷（Step 0）

依使用者指令進入下列模式之一：

| 指令類型 | 範例 | 進哪個流程 |
|---------|------|-----------|
| 跑同步 | 「跑同步」「daily sync」「commit 今天」 | Step 1（同步流程） |
| 排程觸發 | 環境變數 `SCHEDULED_RUN=true` | Step 1 + 自動繼續所有確認 |
| 編輯 source | 「新增 source X」「停用 source Y」 | 進 source 編輯流程，**讀** `references/source_management.md` |
| 編輯白名單 | 「把 X 加入白名單」「Claude skills 的 Y 不要公開」 | 進白名單編輯流程，**讀** `references/whitelist_dsl.md` |
| 查狀態 | 「show 上次跑掉了什麼」 | 印 `LAST_RUN_STATUS.md` 與 `sources.md` 摘要結束 |

## 同步流程（核心）

### Step 1: 環境檢查

依序檢查（任一失敗 → 寫 `LAST_RUN_STATUS.md = FAIL` 並停下）：

1. `D:\Bedridden Library\` 是否存在？若否 → **讀** `references/first_run.md` 跑首次初始化
2. 是否已 git init？若否 → init + 寫 `.gitignore`（含 `_curator/` 與 `_curator/logs/`）
3. `_curator/sources.md` 存在且至少 1 個 enabled source？
4. `_curator/remote_config.md` 已設 remote URL？
5. 對每個 enabled source：source_path 存在？對應 whitelist 檔存在？

### Step 2: 對每個 enabled source 跑同步子流程

**讀** `references/sync_engine.md` 取得演算法細節。對每個 source 依序執行：

1. 解析 whitelist（依 source `type` 用 obsidian-vault 規則或 skill-repo 規則 — **讀** `references/source_types.md`）
2. 掃描 source 目錄產生 source set
3. Diff against 對應 dest 子資料夾 → 得 new / changed / removed 三組
4. 預覽 `+N ~M -K`；排程模式自動繼續，互動模式問使用者
5. 執行同步：new + changed 複製；removed 移到 `_archive/<source>/<YYYY-MM-DD>/<原相對路徑>/`
6. 偵測大檔（>10MB）→ 警告寫 log，不阻擋
7. 更新該 source 在 `sources.md` 的 `last_synced`

### Step 3: 寫合併 log

寫入 `_curator/logs/YYYY-MM-DD.md`，分 source 列出本日同步摘要。logs 由 .gitignore 排除，**不**進 git history。

### Step 4: Git 階段

對整個 Bedridden Library 一次 commit + push：

```
cd D:\Bedridden Library
git status --porcelain    # 應與 Step 2 結果一致
git add .                 # _curator/ 已被 gitignore；_archive/ 會進 commit
git commit -m "[curator] YYYY-MM-DD multi-source sync: ..."
git push origin main
```

push 失敗依 `references/push_failures.md` 矩陣處理。**永遠不嘗試** force push / rebase / reset。

### Step 5: 寫 LAST_RUN_STATUS

寫 `_curator/LAST_RUN_STATUS.md`：

- 第一行：`STATUS: PASS` 或 `STATUS: FAIL`
- 含時間、各 source 同步檔數、commit hash（成功時）、失敗 stage（失敗時）

### Step 6: 交棒 vault-cataloger（Chain A 第二棒）

- **若 Step 1-5 任一 FAIL**：不交棒，停下提示使用者
- **互動模式 PASS**：問使用者是否繼續，得確認後 chain
- **排程模式 PASS**：自動 chain vault-cataloger，傳入本次同步清單

## Commit message 格式

```
[curator] YYYY-MM-DD multi-source sync: A(+N1 ~M1 -K1) B(+N2 ~M2 -K2)

Sources synced:
  - Claude basic   : +3 ~2 -0
  - Claude skills  : +0 ~5 -1

Details:
[Claude basic]
  New:
    - articles/foo.md
  Changed:
    - published/bar.md
[Claude skills]
  Changed:
    - alphaxiv-paper-lookup/SKILL.md
  Archived:
    - old-skill/  →  _archive/Claude skills/2026-04-30/old-skill/
```

第一行的 prefix `[curator]` 方便 `git log --grep="^\[curator\]"` 篩選。Body 列出實際變更，cataloger 可直接讀 git log 解析（不必重跑 diff）。

## 失敗處理原則

per `references/push_failures.md`，失敗矩陣的核心是：

- 任何「需判斷」狀況（衝突、auth、non-fast-forward）→ 停下提示使用者
- 網路逾時 → 重試 3 次，仍失敗 → commit 保留、明日再試
- 排程模式遇任何 FAIL → 不自動修，只記錄；使用者隔日處理

## 與其他 skill 的關係

- **下游 vault-cataloger**：Chain A 第二棒。本 skill PASS 才交棒，傳入同步清單作為 input。
- **下游 internal-cataloger**：間接，透過 cataloger 結束後再接（cataloger 有自己的 chain）
- **不直接觸發**：longform-* skill（Chain B 與 Chain A 解耦）

## audit_checklist.md

本 skill 為「動作型」，**不主動鏈式觸發 output-supervisor**。但仍維護 `audit_checklist.md` 供使用者手動稽核或 governance 檢查。
