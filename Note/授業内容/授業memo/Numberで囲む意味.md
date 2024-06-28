# なぜ、num.valueをNumber()で囲うのか？

`result.textContent = Number(num1.value) + Number(num2.value)` は、JavaScriptで2つの入力フィールドの値を足して、その結果を表示するためのコードです。各部分の意味を説明します。

1. `num1`と`num2`は、それぞれHTMLの入力フィールド（たとえば、`<input>`要素）のことです。
2. `num1.value`と`num2.value`は、入力フィールドにユーザーが入力した値を取得します。

## なぜ `Number()` で囲むのか

`num1.value` や `num2.value` は文字列（String）として取得されます。たとえば、ユーザーが「5」と「10」を入力すると、それぞれ `"5"` と `"10"` という文字列になります。

文字列をそのまま足し算しようとすると、数値の足し算ではなく文字列の連結（結合）が行われます。たとえば：

```javascript
let num1 = { value: "5" };
let num2 = { value: "10" };
let result = num1.value + num2.value;
console.log(result); // "510"（文字列として結合される）
```

これを避けるために、`Number()` を使って文字列を数値に変換します。数値に変換してから足し算を行うことで、正しい数値の足し算が行われます。

### 具体的なコードの動作

```javascript
result.textContent = Number(num1.value) + Number(num2.value);
```

- `num1.value` と `num2.value` は、入力された文字列の値を取得します（例： "5" と "10"）。
- `Number(num1.value)` と `Number(num2.value)` は、それぞれの文字列を数値に変換します（例： 5 と 10）。
- `Number(num1.value) + Number(num2.value)` は、数値同士の足し算を行います（例： 5 + 10 = 15）。
- `result.textContent` に、その計算結果（15）を表示します。

このようにして、ユーザーが入力した値を正しく足し算し、その結果を表示することができます。
