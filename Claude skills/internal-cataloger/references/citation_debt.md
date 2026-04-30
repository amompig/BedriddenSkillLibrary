# 引用負債偵測

internal-cataloger 掃描 vault 內 markdown 檔，找出尚未補完整 metadata 的引用記號。彙總到 dashboard「引用負債」區塊提醒使用者。

## 偵測 pattern（4 種，per I-7 已定）

### 1. `[TODO: ...]`

最常見的待辦記號。`[TODO: 查 Engel 2007 完整 metadata]`、`[TODO: ...]`。

regex：`\[TODO:\s*([^\]]+)\]`

抓取：
- type: `TODO`
- detail: `[TODO: ...]` 中冒號後的內容

### 2. `[需查證]`

中文待查記號。可能單獨出現或附在引用後：
- `根據 Smith 2020 [需查證]，光合作用...`
- `[需查證]`

regex：`\[需查證\]`

抓取：
- type: `需查證`
- detail: 空（單純記號）

### 3. `[?]` 在引用 context 附近

含糊引用：「Smith [?]」、「根據某研究 [?]」。

regex：`\[\?\]`

但必須在「引用 context」附近——避免誤抓數學公式或其他 `[?]` 用法。判斷規則：

- `[?]` 前後 30 字內含下列任一關鍵詞 → 視為引用負債：
  - `年`、`報告`、`研究`、`論文`、`paper`、`study`、`report`、`Smith`、`et al`、人名（capitalize 開頭）
- 否則 → 不視為引用負債

實務上 false positive 仍可能（誰知道你寫什麼），WARN 級可接受。

### 4. `[CITATION-NEEDED]`

英文引用待補。常見於翻譯自英文資料或學術書寫慣例：
- `quantum coherence at room temperature [CITATION-NEEDED]`

regex：`\[CITATION-NEEDED\]`

抓取：
- type: `CITATION-NEEDED`
- detail: 空

## 抓取後處理

對每個命中的 pattern：

```python
{
    "type": "TODO",
    "line": 42,                          # 行號（1-indexed）
    "detail": "查 Engel 2007 完整 metadata",
    "context": "...光合作用研究 [TODO: 查 Engel 2007 完整 metadata]...",  # 前後 40 字
    "raw_match": "[TODO: 查 Engel 2007 完整 metadata]"
}
```

context 取「整行」或「前後 40 字」，取較短者。標點與空白保留。

## 在 dashboard 中的呈現

```markdown
## 引用負債

掃描下列記號，aggregate 後分配到對應檔案：
- `[TODO: ...]`
- `[需查證]`
- `[?]`（在引用 context 附近）
- `[CITATION-NEEDED]`

| 檔案 | 記號類型 | 行號 | 周圍 context |
|------|---------|------|--------------|
| [[Basic/articles/foo]] | TODO | L42 | 「光合作用研究 [TODO: 查 Engel 2007 完整 metadata]」 |
| [[Basic/articles/foo]] | 需查證 | L78 | 「根據 Smith 2020 [需查證]，相干態...」 |
| [[notes/quantum]] | CITATION-NEEDED | L15 | 「quantum coherence at room temperature [CITATION-NEEDED]」 |
| ... | ... | ... | ... |
```

依檔名 → 行號排序。

## 限制

### Code block 內忽略

markdown 程式碼區塊（` ``` ` 或縮排 4 空白）內的記號**不**算引用負債。例如：

````markdown
```python
print("[TODO: implement this]")
```
````

這個 `[TODO: ...]` 在 code block 內，不該被視為引用負債。掃描時用 markdown parser 識別 code block 範圍，跳過。

### inline code 不忽略

行內 code（`single backtick`）內的記號**仍**算引用負債。例如：

```
這部分還沒寫完 `[TODO: 補資料]`
```

這個 `[TODO: ...]` 仍會被抓。理由：行內 code 通常是引用變數名或短代碼，不該用來轉義 TODO 記號。若使用者真的要轉義，用「\[TODO:」即可（escape backslash）。

### 上限保護

單一檔案命中 > 50 個記號 → 只列前 10 個，後面合併「...等 N+ 個記號」。避免 dashboard 被單一檔案淹沒。

## 統計與排序

dashboard 「引用負債」區塊額外加：

```markdown
**統計**：
- 共 <total> 筆記號，分布於 <file_count> 個檔案
- TODO: <N>，需查證: <N>，CITATION-NEEDED: <N>，含糊引用 [?]: <N>
```

排序規則：

1. 檔案名字母序
2. 同檔案內：行號升序

不依「嚴重度」排（每種類型對使用者重要程度因人而異）。

## 客製化（保留設計空間）

未來若使用者要新增自己的 pattern（例如 `[FIXME: ...]` 或 `[REF?]`）：

- 在 SKILL.md frontmatter 加 `custom_debt_patterns:` 欄位
- 由本檔解析該欄位

目前不支援——5 種 pattern 已覆蓋常見場景。
