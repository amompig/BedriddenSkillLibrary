# Source 登記與管理流程

per M-9：「都支援」——使用者可以透過互動指令登記 source，也可以手動編輯 `_curator/sources.md`。

本檔描述互動指令模式的處理流程。

## 互動指令類型

### 「新增 source」

**識別語**：「新增 source X 路徑 Y」「加一個 source」「register source」

**處理流程**：

1. 解析參數：
   - source 名稱（user 提供，或從路徑推測）
   - source 路徑（必要）
   - dest 名稱（user 提供，預設等於 source 名）
   - source 類型（user 選或自動判斷）

2. 自動類型推測：
   - 路徑下有 `.obsidian/` → 提示「這像 Obsidian vault，type 用 obsidian-vault？」
   - 路徑下多個 kebab-case 子資料夾 + `SKILL_STORAGE_RULES.md` → 「這像 skill repo，type 用 skill-repo？」
   - 否則 → 詢問使用者

3. 驗證：
   - source_path 必須存在
   - dest 名與既有 source 不衝突
   - source 名與既有 source 不衝突

4. 寫入 `sources.md`：
   - 用標準 schema 新增區塊
   - `last_synced: (尚未同步)`
   - `enabled: true`

5. 寫初始白名單：
   - 在 `_curator/whitelists/<dest>.md` 寫入對應 type 的預設模板
   - 預設保守：obsidian-vault 給 `published/` `articles/` 兩項；skill-repo 給 `*` 與 `_meta/` 排除

6. 提示使用者：
   - 「source 已登記。建議檢查 `_curator/whitelists/<dest>.md` 並調整白名單後再跑 curator。」
   - 「下次跑 curator 會把 <source_path> mirror 到 <dest_path>。」

### 「移除 source」

**識別語**：「移除 source X」「停用 source X」「unregister source」

**選項**：

- (a) **stop publishing**：保留 mirror 在 Bedridden Library，從此不再更新
  - 設 sources.md 的該 source `enabled: false`
  - 不刪 `Bedridden Library/<dest>/`
  - 不刪 `_curator/whitelists/<dest>.md`

- (b) **archive**：把 mirror 移到 `_archive/<source>/<date>/`，保留 git history
  - 設 enabled: false
  - 移動整個 dest 子資料夾到 _archive
  - 提示「歷史已歸檔，可在 `_archive/<source>/<date>/` 找回」

- (c) **purge**：完全刪除（罕見，警告使用）
  - 警告：「這會把 Bedridden Library 中該 source 的所有歷史從工作樹刪除（git history 仍在）。確定？」
  - 確認後：移除 sources.md 區塊、刪 whitelist 檔、刪 dest 子資料夾
  - **不**清 git history（per X-1 設計：永不破壞性操作）

預設給使用者選 (a) 或 (b)，(c) 需要明確要求。

### 「改名 source」

**識別語**：「把 source X 改名為 Y」「rename source」

**處理流程**：

1. 確認新名與既有 source 不衝突
2. **這個操作會 invalidate 既有 mirror**：因為 dest 名變了，下次同步會把舊 dest 視為 removed（會被 archive），新 dest 從零建立
3. 警告使用者並確認
4. 修改 sources.md：source 名與 dest 名都改
5. 改 whitelist 檔名：`Claude basic.md` → `<新名>.md`
6. 改 whitelist frontmatter `source:` 欄位
7. 提示：「下次 curator 會把舊 dest 整個 archive 掉，新 dest 從零建立。」

### 「啟用 / 停用 source」

**識別語**：「停用 source X」「enable source Y」

**處理流程**：

1. 修改 sources.md 對應 source 的 `enabled` 欄位
2. 不動 dest 子資料夾、不動 whitelist
3. 停用後該 source 在下次 sync 不會被處理

## 手動編輯模式（per M-9 也支援）

使用者直接編輯 `sources.md` 是允許的。curator 在 Step 1 環境檢查時會驗證：

- frontmatter 完整
- 每個 source 區塊有必要欄位（source_path, dest_name, type, whitelist, enabled）
- source_path 存在
- whitelist 檔存在
- 沒有 dest_name 衝突

任一驗證失敗 → 停下提示使用者修正。

## sources.md 的合法 schema

```markdown
---
maintained_by: vault-curator
last_updated: YYYY-MM-DD
---

# Bedridden Library Source 登記

## Source: <source 名>
- source_path: <絕對路徑>
- dest_name: <Bedridden Library 內的子資料夾名>
- type: obsidian-vault | skill-repo | generic-folder
- whitelist: _curator/whitelists/<dest_name>.md
- enabled: true | false
- last_synced: YYYY-MM-DD | (尚未同步)
```

每個欄位用 `- key: value` 形式。順序不限（curator 解析 key 不靠順序）。

## 防呆規則

- source_path **不**能是 `D:\Bedridden Library\` 自己或子資料夾（自我 mirror 會無限循環）
- source_path **不**能是 source 已登記的另一個 source 的子資料夾（避免重複 mirror）
- dest_name **不**能含路徑分隔符（`\`、`/`）
- dest_name **不**能與保留名衝突：`_curator`、`_archive`、`.git`
- type 必須在合法集合內

任一防呆失敗 → 拒絕登記，提示使用者。
