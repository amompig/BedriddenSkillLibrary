# 終止 token 偵測規則

architect 識別「使用者明確同意架構，可進 Round Final 落地」的關鍵詞清單與處理規則。

## 白名單 token（明確同意）

per A-2，使用者說下列任一語句 → architect 進入 Round Final：

### 中文 token

- 「架構通過」
- 「定案」
- 「就這個架構」
- 「OK 落地」
- 「鎖架構」
- 「進下一步」
- 「OK 開寫」
- 「就這樣」
- 「這版定案」
- 「lock 架構」
- 「鎖定」（在架構討論 context 下）

### 英文 token

- "architecture approved"
- "lock it in"
- "ship it"
- "go for it"

### 偵測寬容度

token 比對採「子字串」（substring）而非「完全相等」：

- 「OK，架構通過。開始吧。」 → 命中「架構通過」 → 進 Round Final
- 「我覺得這架構通過得了」 → 命中「架構通過」 → 進 Round Final
- 「架構不通過」 → 命中「架構通過」嗎？需要否定詞偵測（見下）

## 否定詞偵測

子字串命中後，需檢查前後 5 字內是否有否定詞：

- 「不」「不要」「沒」「沒有」「還沒」「未」
- "not", "don't", "haven't"

若有否定詞 → **不**視為終止 token：

- 「架構**不**通過」 → 否定，**不**進 Round Final
- 「**還沒**到鎖架構的時候」 → 否定，**不**進 Round Final

## 模稜兩可詞（必須反問）

下列詞**不**算終止 token，但 architect 需主動反問澄清：

- 「好像可以」「應該還行」「差不多了」「大概 OK」
- 「sort of」「kind of」"maybe"

範例反問：

```markdown
我聽到「應該還行」，不確定這是「架構定案，可以交給 writer」還是「方向對但細節再修」。

要進入 Round Final（落地寫 structures 檔），還是再迭代一輪？
```

得到明確 yes/no 後再決定。

## 易混淆詞（不算 token）

下列詞**不**進 Round Final，但容易誤觸：

- 「OK」（單獨一個 OK，可能是任何同意）→ 不算終止 token
- 「好」（單獨一個好）→ 不算
- 「同意」（沒明確指涉架構）→ 不算

在 token 比對時，要求 **token 與「架構」「方向」「定案」這類關鍵詞共現**：

```python
# 使用者單獨說 "OK"
# → 不命中（無 context）
# → architect 反問：「你說 OK 是指架構通過了嗎？」

# 使用者說 "OK 我看這架構行"
# → 命中（有「架構」context）
# → 進 Round Final
```

## 未表態時的策略

若 N 輪後使用者表態仍模糊：

- architect **不**主動推進到 Round Final
- 主動問「你需要更多時間思考？或要我提幾個候選方向再選？」
- 不偽造同意

## 反向：使用者要求停止

若使用者說「停下來」「不要寫了」「先放著」：

- 不進 Round Final
- 不寫 structures 檔
- 保留對話迭代狀態（下次回來可從現在這版繼續）

範例：

```
使用者：今天先到這裡，我明天再想想。
architect：好的，今天的草稿是 v3。明天若你想繼續，告訴我「繼續規劃 X」就會接著這版。
```

## 微調模式的終止 token

writer 觸發 architect 進微調模式時，相同 token 機制適用：

- 「微調通過」
- 「修正版定案」
- 「OK，改完這樣可以」（含關鍵詞）

微調終止 → revision +1，寫回 structures 檔。

## 補充：interview 檔模式的終止

interview 檔模式下：

1. 使用者說「讀問卷繼續」 → architect 讀檔，進 Round 1（不是 Round Final）
2. Round 1..N 仍要使用者表態終止 token
3. 不能因為「interview 填完」就直接 Round Final

interview 檔提供 Round 0 的答案，但架構討論仍要正常迭代。

## 防呆：在錯的時機落地

architect 自己 audit：

- Round 1 進行中 → **不**寫檔
- 沒收到 token → **不**寫檔
- 即使使用者催「快點寫」「直接寫」 → 仍堅持要終止 token，否則不寫

例：

```
使用者：別墨蹟了，趕快給我寫好。
architect：理解你想推進。但為了確保 writer 拿到的架構是你真的同意的版本，
         我需要你明確說「架構通過」（或同義詞）才寫檔。
         
         這版（v3）你同意嗎？
```

## token 偵測的實作層次

簡單實作：對使用者每則訊息做子字串掃描 + 否定詞檢查。

進階實作（保留設計空間）：

- LLM-based 意圖判斷（在邊界 case 由 architect 自己判斷）
- 信心分數（高信心直接進，低信心反問）

目前用簡單實作即可——子字串 + 否定詞 + 反問模糊詞。
