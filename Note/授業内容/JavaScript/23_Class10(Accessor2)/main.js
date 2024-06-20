// クラスについて
// アクセサ2(実践教科書p66)
// blades

// モジュールのインポート(default)、標準モジュール取り込み
import Fan from "./Fan.js"

// モジュールのインポート、モジュール出力
// import {Fan} from "./Fan.js"


// 出力先の要素を習得
let output = document.getElementById('output')

// インスタンス化
// 羽根の枚数を指定なし
let fan01 = new Fan(output)
// 羽根の枚数を指定あり
let fan02 = new Fan(output, 7)

// アクセサの呼び出し
// getする

output.innerHTML += fan01.getSwing() + '<br>'
/ fan01のメソッドの呼び出し
fan01.pressSwingButton() + '<br>'
output.innerHTML += fan01.swing + '<br>'
output.innerHTML += fan01.blades + '<br>'

output.innerHTML += fan02.swing + '<br>'
// fan02のメソッドの呼び出し
fan02.pressSwingButton() + '<br>'
output.innerHTML += fan02.swing + '<br>'
output.innerHTML += fan02.blades + '<br>'

// バリデーションで弾かれる(ルール違反)
fan02.blades = -5
output.innerHTML += fan02.blades + '<br>'

// バリデーションでは弾かれない(ルール通り)
fan02.blades = 12
output.innerHTML += fan02.blades + '<br>'



// 扇風機の統計情報の表示
Fan.statisticsOutput = document.getElementById('output')
Fan.infoFans()