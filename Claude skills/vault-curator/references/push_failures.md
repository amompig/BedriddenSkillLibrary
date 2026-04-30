# Git push 失敗處理矩陣

curator Step 4 (git 階段) 的失敗處理。**核心原則：永不破壞性操作**。

## 失敗分類

依 `git push` 的 stderr 與 exit code 分類。

### 1. 未設 remote

**徵兆**：`fatal: 'origin' does not appear to be a git repository`

**處理**：

- 不嘗試任何修復
- 寫 `LAST_RUN_STATUS.md = FAIL` 含原因 `remote not configured`
- 提示：「`_curator/remote_config.md` 中的 remote 未設或失效。請填入後重跑 curator。」
- 注意：commit **保留**（不 reset）。下次同步重 push 即可。

### 2. Auth 失敗

**徵兆**：`fatal: Authentication failed` 或 `Permission denied (publickey)` 或 `403 Forbidden`

**處理**：

- 不重試（重試只會持續失敗）
- 寫 `LAST_RUN_STATUS.md = FAIL` 含原因 `auth failed`
- 提示：「GitHub 認證失敗。請檢查：
  - HTTPS 用 PAT：是否已設定（git config 或 credential helper）
  - SSH：~/.ssh/id_rsa 或對應 key 是否在 ssh-agent
  - PAT 是否過期或權限不足（需要 repo write 權限）」
- commit **保留**

### 3. Non-fast-forward（有人手動推 commit）

**徵兆**：`Updates were rejected because the remote contains work that you do not have locally`

**處理**：

- **絕對不**自動 rebase / merge / force push
- 寫 `LAST_RUN_STATUS.md = FAIL` 含原因 `non-fast-forward`
- 提示：「remote 有你本機還沒有的 commit。可能是你在其他機器或網頁直接編輯過。請：
  1. `git fetch origin`
  2. 檢查 `git log origin/main..main` 看本機獨有 commits
  3. 檢查 `git log main..origin/main` 看 remote 獨有 commits
  4. 自行決定 merge 還是 rebase（curator 不替你做這個決定）
  5. 解決後重跑 curator」
- commit **保留**

### 4. 衝突檔案（merge conflict 應不發生但保險）

**徵兆**：working tree 內有 `<<<<<<< HEAD` 或類似衝突標記

**處理**：

- 不嘗試解
- 寫 LAST_RUN_STATUS.md = FAIL
- 提示：「working tree 有未解決的衝突檔案。這不該發生在純 mirror flow 中——可能是上次 push 失敗後使用者手動操作的殘留。請：
  1. `git status` 檢查
  2. 解衝突或 `git reset --hard` 清掉本機改動
  3. 重跑 curator」

注意：警告中的 `git reset --hard` 是**給使用者的**指示，curator 自己**永不執行**。

### 5. 網路逾時 / 連線失敗

**徵兆**：`Could not resolve host` / `Operation timed out` / 任何 connection error

**處理**：

- 重試 3 次，每次間隔 30 秒
- 仍失敗 → 寫 LAST_RUN_STATUS.md = FAIL 含原因 `network failure after 3 retries`
- 提示：「網路問題。commit 已保留，明日排程會自動重試。若你想手動立即重試，跑 `git push origin main`。」
- commit **保留**

### 6. 大檔超過 GitHub 100MB 上限

**徵兆**：`File <path> is XXX MB; this exceeds GitHub's file size limit`

**處理**：

- 寫 LAST_RUN_STATUS.md = FAIL
- 識別該檔案路徑
- 提示：「{path} 超過 GitHub 100MB 上限，無法 push。建議：
  - 把該檔加入 source 對應的 whitelist exclude，或
  - 將檔案搬離 source 範圍，或
  - 設定 git-lfs（curator **不**自動處理）」
- 注意：commit 已包含該檔，需要 amend 或 reset 才能移除

修復步驟（curator 提供但**不**自動執行）：
```
cd D:\Bedridden Library
git reset --soft HEAD~1
# 從 staging 移除大檔
git restore --staged <path>
# 加入 exclude 後重跑同步
```

### 7. 未知錯誤

**徵兆**：上述都不命中

**處理**：

- 寫完整 stderr 到 LAST_RUN_STATUS.md
- 寫到 logs/<today>.md
- 提示使用者人工介入
- commit 保留

## 重試政策

| 失敗類型 | 自動重試？ | 次數 | 間隔 |
|---------|-----------|------|------|
| 網路 | 是 | 3 | 30 秒 |
| Auth | 否 | - | - |
| Non-fast-forward | 否 | - | - |
| 衝突 | 否 | - | - |
| 大檔超限 | 否 | - | - |
| 未知 | 否 | - | - |

只有網路類失敗適合自動重試（暫態性）。其他都需要使用者判斷。

## 排程模式 vs 互動模式

排程模式下任何 FAIL：
- 不提示使用者（沒人在）
- 寫入 LAST_RUN_STATUS.md（FAIL + 原因）
- 寫到 logs
- 整個 Chain A 終止（不嘗試 cataloger）

互動模式：
- 立即將失敗訊息與建議步驟印給使用者
- 等使用者決定下一步

## 永不執行的操作

curator 在任何狀況下**永不**執行：

- `git push --force` / `git push -f`
- `git push --force-with-lease`
- `git reset --hard`
- `git reset --soft HEAD~N`（除非 N=0，那等於沒做）
- `git rebase`（含 `--continue` / `--skip` / `--abort`）
- `git filter-branch` / `git filter-repo`
- `git reflog expire`

這些都是「破壞 history」或「重寫 history」的操作，可能 silently 丟失資料。即使使用者要求 curator 執行這些命令，curator 應拒絕並建議使用者手動執行（並告知風險）。
