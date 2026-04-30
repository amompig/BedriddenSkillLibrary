# Obsidian 排除設定教學

`_internal-catalog/` 在 vault 根目錄會被 Obsidian 預設顯示，搜尋時會把 dashboard 與 changelog 內容混入結果，干擾使用體驗。建議排除。

## 為什麼要排除

- dashboard 含所有檔案的 wikilink，搜尋任何關鍵字幾乎都會命中 dashboard
- changelog 也含大量 wikilink，每日都會更新
- 圖譜（Graph view）會被 dashboard 的密集連結淹沒
- 但**不能**直接刪除 `_internal-catalog/`——它是 internal-cataloger 的核心輸出

排除設定的效果是：「Obsidian 看不見它」（搜尋、自動完成、圖譜都忽略），但檔案仍在磁碟上，仍可在檔案總管瀏覽。

## 排除設定步驟（Obsidian 桌面版）

### Step 1: 開啟設定

點 Obsidian 左下角「Settings ⚙️」按鈕，或快捷鍵 `Ctrl+,`（Win）/ `Cmd+,`（Mac）。

### Step 2: 找到 Files & Links

左側選單中的「Files & Links」（中文界面是「檔案與連結」）。

### Step 3: 加入排除路徑

捲到「Excluded files」區塊（中文「排除的檔案」），點旁邊的「Manage」按鈕。

在彈出視窗的輸入框輸入：

```
_internal-catalog/
```

點「Add」加入清單。**注意**：路徑相對於 vault root，使用 `/` 分隔符。

### Step 4: 確認

確認清單有 `_internal-catalog/` 後，關閉設定。

## 驗證排除生效

開啟 Obsidian search（`Ctrl+Shift+F`），搜尋一個你知道存在於 dashboard 的字串（例如某檔案名）。

預期：

- ✅ 命中該檔案本身
- ❌ **不**命中 `_internal-catalog/00-DASHBOARD.md`

若仍命中 dashboard → 排除設定沒生效。檢查路徑是否完全一致（包括尾隨 `/`）。

## 仍能做什麼

排除後仍可：

- 手動點開 `_internal-catalog/00-DASHBOARD.md` 瀏覽
- 從檔案總管雙擊開啟
- 用 wikilink `[[_internal-catalog/00-DASHBOARD]]` 跳轉（但不會在自動完成中出現）

不能做：

- 在搜尋結果看到
- 在圖譜看到
- 在「Quick switcher」（`Ctrl+O`）看到

## 進階：透過 .obsidian 設定檔直接設定

若 Obsidian UI 操作不便，也可直接編輯 `.obsidian/app.json`：

```json
{
  "userIgnoreFilters": [
    "_internal-catalog/"
  ]
}
```

新增此欄位（如已有 list，直接 append 字串）。重開 Obsidian 生效。

## 與 vault-curator 白名單的關係

`_internal-catalog/` **永遠**不會被 vault-curator 同步到 Bedridden Library，理由：

1. 它在 vault root，**不**在 `Basic\` 子資料夾下
2. Source A (Claude basic) 的 source_path 是 `D:\...\Basic`，不涵蓋 vault root
3. 即使 source_path 改成 vault root，`_internal-catalog/` 也應加入 Claude basic 白名單的 excluded_globs

兩重保險：路徑隔離 + 白名單排除。實務上目前只靠路徑隔離已足。

## 排除生效後的工作流程

排除後仍能用內部編目本：

1. 在 Obsidian 任何位置打字 `[[_internal-catalog/00-DASHBOARD]]` 跳轉
2. 或設一個 Bookmark：File → Bookmarks → New bookmark → 選 dashboard 檔案
3. 或在 vault root 寫一個 `INDEX.md` 含跳轉連結，並把 INDEX.md 釘選

## 多 vault 場景（保留設計空間）

未來若使用者有多個 Obsidian vault，每個 vault 都用 internal-cataloger，每個都要分別做排除設定。

設定不會跨 vault 同步（每個 vault 有自己的 `.obsidian/app.json`）。
