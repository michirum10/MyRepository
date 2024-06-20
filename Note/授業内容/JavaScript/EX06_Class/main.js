import Fan from "./Fan.js"

// 出力先の要素を習得
let output = document.getElementById('output')

// インスタンス化
let fan01 = new Fan(output)

let p0btn = document.getElementById('p0')
let p1btn = document.getElementById('p1')
let p2btn = document.getElementById('p2')
let p3btn = document.getElementById('p3')
// 首振りボタン
let swingbtn = document.getElementById('swing')

// 間違いの例
// p0btn.addEventListener('click',fan01.pressPowerButton(Fan.POWER_STATUS.OFF))
// HTMLで定義していた『onClick』は押されたら実行するプログラムを入れておく
// 今回は、押されたら実行する関数を入れるのが正しい

// 正しくは以下の通りに書く

// 『切』ボタン
// コールバック関数の定義
function pressPowerButtonOFF() {
    fan01.pressPowerButton(Fan.POWER_STATUS.OFF)
}
// ボタンのイベントとコールバック関数の関連付け
// イベントと関数を関連付ける事をバインドと言う
// (Fan.POWER_STATUS.OFF)は書かない
p0btn.addEventListener('click',pressPowerButtonOFF)

// 省略した書き方
// 無名関数を利用すると、コールバック関数を用意しなくても実装できる
// 『弱』ボタン
p1btn.addEventListener('click',function (){fan01.pressPowerButton(Fan.POWER_STATUS.P1)})
// 『中』ボタン
p2btn.addEventListener('click',function (){fan01.pressPowerButton(Fan.POWER_STATUS.P2)})
// 『強』ボタン
p3btn.addEventListener('click',function (){fan01.pressPowerButton(Fan.POWER_STATUS.P3)})
// 首振りボタン
swingbtn.addEventListener('click',function (){fan01.pressSwingButton()})

// 出力
fan01.infoView()

// 関数、変数ctrl押しながらクリックすると定義したところに飛べる