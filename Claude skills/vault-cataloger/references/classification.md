# 分類規則（hybrid: frontmatter + path）

per K-3 使用者選 (c) 混合：frontmatter `category` 優先，無則退回路徑判斷。

本檔定義對單一檔案的分類流程。

## 流程

```
對檔案 file_path:

1. 若是 markdown 檔且有 frontmatter：
   - 解析 frontmatter
   - 若 category 欄位存在且非空：→ 用 frontmatter category
   - 否則 → 進 step 2

2. 退回路徑判斷：
   - 取 file_path 相對於 dest root 的第一層資料夾
   - 用該資料夾名作為分類

3. 若 file 在 dest root（無子資料夾）：
   - 分類 = "（根目錄）"

4. 對 skill-repo 型：
   - 不解析 frontmatter（用 D:\Claude skills\README.md 的分類體系）
   - 依本檔末段 §skill-repo 分類規則
```

## obsidian-vault 型分類

### frontmatter category 範例

```yaml
---
title: 量子生物學論文回顧
category: 文章
---
```

`category: 文章` → 該檔分類為「文章」。

### category 欄位的合法值

不限制（自由文字）。但建議使用者一致使用：

- 文章 / article
- 參考資料 / reference
- 筆記 / note
- 講義 / lecture
- 評論 / review
- 草稿 / draft（注意：status: draft 會被 curator 排除，所以這類會在 internal-cataloger 出現，不在 vault-cataloger）

cataloger 對 category 值做正規化：

- lowercase 比對（「文章」與「Article」視為不同類）
- 去前後空白
- 不做語義合併（「文章」與「文獻」視為不同類，由使用者自己一致）

### 路徑退回規則

無 frontmatter 或無 category 時取第一層資料夾名：

```
articles/2026-04/foo.md          → 分類「articles」
references/quantum-bio.md         → 分類「references」
notes/half-thought.md             → 分類「notes」
```

中文資料夾名也支援：

```
文章/foo.md                        → 分類「文章」
參考/bar.md                        → 分類「參考」
```

### 衝突處理

若同一分類同時有 frontmatter category 與路徑名稱（例如 frontmatter 寫「文章」但檔案在 `articles/` 下）：

- 採用 frontmatter（K-3 規則）
- 但在 audit_checklist 標 ⚠ WARN：「分類不一致：frontmatter 與路徑分屬不同分類」
- 這提醒使用者長期不一致會讓 catalog 與直覺脫節

## skill-repo 型分類

不解析 frontmatter。依 `D:\Claude skills\README.md` 的「目前 skills」表格：

```
README.md 中：
| Skill | 用途 | 入口 |
位於 H3 標頭「### 內容產出型」之下 → 該 skill 分類為「內容產出型」
位於 H3 標頭「### 投資審查型」之下 → 「投資審查型」
位於 H3 標頭「### 監督稽核型」之下 → 「監督稽核型」
```

cataloger 解析 README 時：

1. 找所有 H3 標頭
2. 找每個 H3 後第一個 markdown 表格
3. 表格中 skill name 欄（第 1 欄，去掉 backticks 與尾隨 `/`）
4. 對應該 skill name → H3 文字

若解析失敗（README 結構變動）：

- 退回「未分類」分類，全部 skill 在同一區塊
- WARN 提示使用者：「README 結構解析失敗，請檢查格式」

## 多分類處理

若同一檔案符合多個分類（罕見，但可能）：

- frontmatter category 是 list（如 `category: [文章, 評論]`）→ 兩個分類都列入
- 路徑命中多層匹配 → 用最深層（最具體）

list 形式範例：

```yaml
---
category:
  - 文章
  - 量子生物學
---
```

該檔同時出現在「文章」與「量子生物學」兩個分類區塊。

CHANGELOG 中只列一次（取第一個分類）。MOC 中兩處都列。

## 例外規則

下列檔案**不參與分類**（不出現在 MOC）：

- `00-MOC.md` 自己（避免自我引用）
- `CHANGELOG.md` 自己（在 MOC 開頭明確連結，不在分類索引）
- `.gitignore`、`.gitkeep` 等隱藏檔
- frontmatter `hide_from_catalog: true` 的檔案
- 路徑在 `_archive/` 下的檔案（curator 已歸檔，不該再被 surface）

## 一致性報告

cataloger 在 Step 3.6 的一致性檢查中報告：

- 「N 個檔案無 frontmatter 也無路徑可分類 → 分類為『未分類』」
- 「M 個檔案分類不一致（frontmatter 與路徑分屬不同類）」
- 「P 個分類只有 1 個檔案 → 可能拼寫錯（例如『文章』vs『文章 』）」

這些報告寫到 `_curator/logs/<today>.md` 的 cataloger 區段。
