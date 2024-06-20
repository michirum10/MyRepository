# なぜvalueが必要なのか

`num1.value` が必要なのは、`num1` がHTMLの入力要素を指しており、その入力要素の中にユーザーが入力した値を取得するためです。`num1` だけでは、その要素自体を参照するだけで、中の値（ユーザーが入力した値）を取得することはできません。

## 例を使った説明

以下に具体的なHTMLとJavaScriptの例を示します。

### HTML

```html
<input id="num1" type="text">
<input id="num2" type="text">
<div id="result"></div>
<button onclick="calculate()">Calculate</button>
```

### JavaScript

```javascript
function calculate() {
  let num1 = document.getElementById("num1");
  let num2 = document.getElementById("num2");
  let result = document.getElementById("result");

  result.textContent = Number(num1.value) + Number(num2.value);
}
```

#### 詳細な説明

1. **HTML要素の取得**:

   ```javascript
   let num1 = document.getElementById("num1");
   let num2 = document.getElementById("num2");
   let result = document.getElementById("result");
   ```

   - `document.getElementById("num1")` は、HTMLドキュメント内のIDが "num1" である要素（つまり、最初の `<input>` 要素）を取得します。
   - `num1` は、この `<input>` 要素自体を指します。

2. **入力値の取得**

   ```javascript
   let value1 = num1.value;
   let value2 = num2.value;
   ```

   - `num1.value` は、その `<input>` 要素内にユーザーが入力した値を取得します。例えば、ユーザーが "5" と入力した場合、`num1.value` は `"5"` となります。
   - `num2.value` も同様に、その `<input>` 要素内にユーザーが入力した値を取得します。

3. **計算と表示**:

   ```javascript
   result.textContent = Number(value1) + Number(value2);
   ```

   - `Number(value1)` と `Number(value2)` は、それぞれの文字列を数値に変換します。
   - 数値に変換された後、これらの値を足し算します。
   - `result.textContent` に、その計算結果を設定します。この結果は、`<div id="result">` の中に表示されます。

### `num1` だけでは駄目な理由

もし `num1` だけを使って計算しようとすると、次のようなコードになるかもしれません：

```javascript
let value = num1 + num2;
```

しかし、これは要素自体を足し合わせようとするものであり、数値の計算ではなく、オブジェクトの操作となります。`num1` と `num2` は `<input>` 要素そのものを指しているため、そのままでは値を取得できず、数値計算もできません。したがって、`.value` プロパティを使ってその中の値を取り出し、数値に変換して計算する必要があります。
