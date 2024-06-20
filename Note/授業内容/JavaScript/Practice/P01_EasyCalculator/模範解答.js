// 一番上に書いたほうがいい

// HTML　num1,num2,resultを取得
let num1 = document.getElementById("num1")
let num2 = document.getElementById("num2")
let result = document.getElementById("result")

// Functionはclick1を押したときに動く
function click1() {
   // resultのtextContentに、num1+num2を代入
   // Number()で囲むことで、num1.valueを数字として扱う
   // num1だけだと参照するだけ
   // .valueをつけることで、num1の値を取得
   result.textContent = Number(num1.value) + Number(num2.value)
}
function click2() {
   result.textContent = Number(num1.value) - Number(num2.value)
}
function click3() {
   result.textContent = Number(num1.value) * Number(num2.value)
}
function click4() {
   result.textContent = Number(num1.value) / Number(num2.value)
}
function click5() {
   result.textContent = Number(num1.value) % Number(num2.value)
}