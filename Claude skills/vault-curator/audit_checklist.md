# vault-curator audit checklist

供 output-supervisor 在使用者手動觸發稽核時讀取。本 skill 為動作型，不主動鏈式觸發 supervisor。

## 同步正確性（CRITICAL）

- [ ] 同步前後每個 source 的 mirror 結構符合對應 whitelist
- [ ] 沒有檔案被同步到非 dest_name 之外的位置
- [ ] `_archive/` 內結構為 `<source>/<YYYY-MM-DD>/<原相對路徑>/`
- [ ] 排除清單上的檔案（如 alphaxiv-paper-lookup, pocus-em-domain, nhird-hwdc-feasibility）未出現在 mirror

## Git 操作（CRITICAL）

- [ ] commit message 列出的檔案數 = `git diff --stat` 顯示的檔案數
- [ ] commit message 第一行符合 `[curator] YYYY-MM-DD multi-source sync: ...` 格式
- [ ] 沒有 force push 痕跡（`git reflog` 顯示 commits 都是線性）
- [ ] 沒有 reset --hard 痕跡
- [ ] 沒有 rebase 痕跡

## 檔案佈局（CRITICAL）

- [ ] `_curator/` 整個被 .gitignore 排除（不在 git tracked files）
- [ ] `_curator/logs/` 在 .gitignore 中
- [ ] `_curator/LAST_RUN_STATUS.md` 在 .gitignore 中
- [ ] `_archive/` **未**在 .gitignore（per M-10 進 git history）
- [ ] `_curator/sources.md` 與 `_curator/whitelists/` 存在但不 tracked

## Source 一致性（⚠ WARN）

- [ ] `sources.md` 每個 enabled source 的 `last_synced` 為今日（若今日已跑）
- [ ] `_curator/whitelists/<source>.md` 對應每個 sources.md 中的 enabled source
- [ ] 沒有孤兒白名單檔（whitelist 對應的 source 已停用或不存在）

## Log 完整性（⚠ WARN）

- [ ] `_curator/logs/YYYY-MM-DD.md` 已生成
- [ ] log 內容包含每個同步過的 source 摘要
- [ ] `LAST_RUN_STATUS.md` 反映本次結果（PASS / FAIL + 時間）

## 排程與環境（⚠ WARN）

- [ ] 排程模式跑時 `SCHEDULED_RUN=true` 環境變數有設
- [ ] 排程模式下 LAST_RUN_STATUS 有時間戳
- [ ] 大檔（>10MB）警告有寫入 log（若有）
