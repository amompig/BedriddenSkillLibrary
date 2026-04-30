# 從 vault-curator 接手 input 的合約

cataloger 是 Chain A 第二棒。本檔定義從 curator 收到的 input 結構與處理方式。

## Chain A 觸發時的 input

排程模式下，curator Step 5 完成後觸發 cataloger，傳入：

```yaml
synced_sources:
  - "Claude basic"
  - "Claude skills"

per_source_changes:
  "Claude basic":
    new:
      - "articles/2026-04/foo.md"
      - "articles/2026-04/bar.md"
    changed:
      - "published/longform/baz.md"
    archived:
      - "references/old-thing.md"
  "Claude skills":
    new: []
    changed:
      - "alphaxiv-paper-lookup/SKILL.md"
    archived: []

commit_hash: "abc123def456"
sync_date: "2026-04-30"
last_run_status: "PASS"
```

## input 解析

### synced_sources

list of source names。cataloger 只處理這些 source（非全 Bedridden 重編目）。

每個 source name 必須對應 `D:\Bedridden Library\<source name>\` 子資料夾。若不存在 → graceful degrade（跳過該 source，繼續其他）。

### per_source_changes

每個 source 有三個 list：new、changed、archived。

- **new**：該檔案是首次出現在 dest，cataloger 應新增到 MOC 與 CHANGELOG
- **changed**：該檔案內容有變但路徑沒變，cataloger 重抓 metadata（description 可能變）
- **archived**：該檔案已從 source 消失，curator 移到 _archive。cataloger 應從 MOC 移除，並在 CHANGELOG 記錄歸檔

路徑都是相對於 dest 子資料夾的相對路徑（不含 source 名稱前綴）。

### commit_hash

curator Step 4 commit 後的 hash。寫入 CHANGELOG 對應日期區塊。

graceful degrade：若 commit_hash 缺失（curator 沒推 git，例如離線狀態），CHANGELOG 區塊省略 commit hash，加註「（commit hash unavailable）」。

### sync_date

當日日期。CHANGELOG 區塊用此作為 H2 標頭。

### last_run_status

curator 的最終狀態。**若 != PASS → cataloger 不繼續**（per X-1，上游 FAIL 不嘗試下游）。

## 互動模式 / graceful degrade

若 cataloger 被手動觸發（無 curator input）：

1. 視為「全 Bedridden Library 重編目」
2. 對每個 enabled source（從 sources.md 讀）：
   - new = (掃描 dest 所有檔) - (現有 MOC 列出的檔)
   - changed = ?（無 hash 比對，假設 0 個 changed）
   - archived = (現有 MOC 列出但 dest 不存在的檔)
3. CHANGELOG 加當日區塊註明「（手動觸發重編目）」，commit_hash 留空

## input 驗證

收到 curator input 後：

- 結構必要欄位齊全？（synced_sources, per_source_changes, last_run_status）
- last_run_status == PASS？否則停下
- 每個 synced_source 在 sources.md 有對應登記？
- per_source_changes 的 source key 都在 synced_sources 中？

驗證失敗 → 寫錯誤到 _curator/logs/<today>.md，提示使用者，停下。

## chain 內的失敗傳遞

cataloger 自身失敗時：

- 寫 LAST_RUN_STATUS = FAIL（cataloger 階段）含原因
- **不**繼續 chain 到 internal-cataloger
- internal-cataloger 不會跑，下一階段中斷

cataloger 部分失敗（某個 source 編目成功、某個失敗）：

- 整體 status = WARN
- 仍 chain output-supervisor（讓 supervisor 把成功的 source 也驗證一遍）
- 後續 internal-cataloger 仍跑（per chain 紀律：cataloger WARN 不阻擋下游）

## 輸出回傳給 chain orchestrator

cataloger 完成後回傳：

```yaml
catalog_status: "PASS" | "WARN" | "FAIL"
catalogs_updated:
  - "Claude basic/00-MOC.md"
  - "Claude basic/CHANGELOG.md"
  - "Claude skills/00-MOC.md"
  - "Claude skills/CHANGELOG.md"
supervisor_verdict: "PASS" | "WARN" | "FAIL"
supervisor_report_path: "D:\\Claude skills\\_meta\\audits\\output\\vault-cataloger\\<timestamp>__<verdict>.md"
```

orchestrator 用這個結果決定是否繼續 chain 到 internal-cataloger。

## 跨日邊界

若 curator 跑完跨午夜（罕見），sync_date 用 curator Step 1 開始時的日期，不用 cataloger 啟動時的日期。這保證一個 sync run 內所有日期一致。
