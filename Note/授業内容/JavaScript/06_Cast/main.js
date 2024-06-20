// 型変換

// 出力準備
let output = document.getElementById('output')

// 文字列＋数値
let str1 = '1'
let num1 = 20
let result = str1 + num1
output.innerHTML += result
output.innerHTML += '<br>'
output.innerHTML += typeof result
output.innerHTML += '<br>'

// 文字列(数値に型変換)＋数値
result = Number(str1) + num1
output.innerHTML += result
output.innerHTML += '<br>'
output.innerHTML += typeof result
output.innerHTML += '<br>'

// 基本型を参照型に変換（ラッパー(包む)クラス）
let str2 = new String('3000')
output.innerHTML += typeof str2
output.innerHTML += '<br>'

// instanceof 型(参照型)を比べるキーワード
output.innerHTML += str2 instanceof String
output.innerHTML += '<br>'
