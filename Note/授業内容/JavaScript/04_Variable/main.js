// 変数
// 定義する。宣言する。
// var let
// 使い分け難しいので、基本は'let'を使う
// let=仮に～とするという意味？
// varはVariable

// 変数は使う前にletで宣言して初期化

// 変数の定義と初期化(=)
// ＝は代入
// 定義したら初期化する
// 基本　文字列型
let name = '森美智瑠'

// 入力なし、未定義だとundefinedと出る
let name2

// let name = '森美智瑠'の処理を2行に分解
let name3
name3 = '森美智瑠２'

// 出力する場合は変数なのでinnerHTMLを使う
// output.innerHTML += name3
// 下でoutput.textContent = msgしてるので上書きされてるっぽい。

// 変数名の付け方
// 意味のある名前をつける
// ２単語以上の場合、２単語目から大文字で読みやすく
// 命名規則に従う
let personalName

// 命名規則について
// キャメルケース（camelCase）
// ローワーキャメルケース（lowerCamelCase）
// アッパーキャメルケース（UpperCamelCase）
// スネークケース（snake_case）（SNAKE_CASE）
// 変数は基本的にローワーキャメルケースを利用する。

// 変数の代入について
// = を利用して右辺の値を左辺に代入する
// 左辺に値が入っていた場合は上書きされる。元々のやつは消える。

// 変数の取得について
// 変数名を書くだけ。わかりやすい名前なら何でも良い

// JavaScriptでHTMLに出力する処理
// 一番上に書く
// ドキュメントからIDアウトプットを検索。その答えを左辺に代入
// どのタグになにをするのか
// ()は関数
// . ～のと言う意味
// ドキュメントのIDを取得
// オブジェクト型
let output = document.getElementById('output')

// 入力する文字を定義
let msg = '表示したい文字を入力'
// 文字を出力する
// 関数ではない。変数。
// アウトプットのテキストコンテンツ
// 基本的には型が一致してないと入らないが、JSはその限りではない。
output.textContent = msg

// 変数の型について
// 大きく分類すると基本型と参照型に分けられる

// 基本型
// 文字列や数値型のことで、その値がそのまま変数に格納されている。
// 一覧：
// 数値型
// 文字列型
// 真偽型
// numll
// undefined
// シンボル

// 参照型
// 配列やオブジェクト、関数の事でその値が格納されているアドレスを格納している。
// 一覧：
// 配列
// オブジェクト
// 関数

// 数値型としての変数
let num1 = 100
// 文字列型としての変数
let str1 = '100'

// タグや変数にはinnerHTML HTMLが使える
// num は数字
// str は文字列
// 文字に対して数字が代入できてしまってる。
output.innerHTML += '<br>'
output.innerHTML += num1
output.innerHTML += '<br>'
output.innerHTML += str1

// 動的型付けについて
// 計算結果の型が違っても、代入することができる。(自動的に型が変化する)
// データ型。TYPE
let num2 = num1 + num1
output.innerHTML += '<br>'
output.innerHTML += num2

// 文字列型+文字列型 : 文字列型
let str2 = str1 + str1
output.innerHTML += '<br>'
output.innerHTML += str2

// 数値型+文字列型 : 文字列型
let mix1 = num1 + str1
output.innerHTML += '<br>'
output.innerHTML += mix1

