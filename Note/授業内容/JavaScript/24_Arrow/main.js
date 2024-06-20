// アロー関数について

// 出力先の要素を習得
let output = document.getElementById('output')

// 通常の関数の作り方
function func01() {
    console.log("Hello")
}
// func01()を実行
func01()

// 無名関数を生成してfun02に代入
const func02 = function () {
    console.log("Hello")
}
func02()

// アロー関数（基本）
const func03 = () => {
    console.log("Hello")
}
func03()

// 一行しかない場合{}を省略したアロー関数
const func04 = () => console.log("Hello")
func04()

// {}とreturnを省略したアロー関数
const func05 = () => "Hello"
// 出力の書き方注意
console.log(func05())