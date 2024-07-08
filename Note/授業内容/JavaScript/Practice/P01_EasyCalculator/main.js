// 出力準備
let output = document.getElementById("result")

function click1() {
    // num1,num2,resultを取得
    // Numberで囲むことで、num1.valueを数字として扱う
    // .valueをつけることで、num1の値を取得
    let num1 = Number(document.getElementById("num1").value)
    let num2 = Number(document.getElementById("num2").value)
    let result = num1 + num2
    output.innerText = "答え：" + result
}
function click2() {
    let num1 = Number(document.getElementById("num1").value)
    let num2 = Number(document.getElementById("num2").value)
    let result = num1 - num2
    output.innerText = "答え：" + result
}
function click3() {
    let num1 = Number(document.getElementById("num1").value)
    let num2 = Number(document.getElementById("num2").value)
    let result = num1 * num2
    output.innerText = "答え：" + result
}
function click4() {
    let num1 = Number(document.getElementById("num1").value)
    let num2 = Number(document.getElementById("num2").value)
    let result = num1 / num2
    output.innerText = "答え：" + result
}
function click5() {
    let num1 = Number(document.getElementById("num1").value)
    let num2 = Number(document.getElementById("num2").value)
    let result = num1 % num2
    output.innerText = "答え：" + result
}
let bmi = document.getElementById("bmi")
function click6() {
    let height = Number(document.getElementById("height").value)
    let weight = Number(document.getElementById("weight").value)
    let result = weight / (height * height)
    output.innerText = "答え：" + result
}