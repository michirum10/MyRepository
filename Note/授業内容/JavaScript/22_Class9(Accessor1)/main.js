// クラスについて
// アクセサ1
// getSwing()

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
// fan01のメソッドの呼び出し
fan01.pressSwingButton() + '<br>'
output.innerHTML += fan01.getSwing() + '<br>'
output.innerHTML += fan01.getBlades() + '<br>'

output.innerHTML += fan02.getSwing() + '<br>'
// fan02のメソッドの呼び出し
fan02.pressSwingButton() + '<br>'
output.innerHTML += fan02.getSwing() + '<br>'
output.innerHTML += fan02.getBlades() + '<br>'

// バリデーションで弾かれる(ルール違反)
fan02.setBlades(-5)
output.innerHTML += fan02.getBlades() + '<br>'

// バリデーションでは弾かれない(ルール通り)
fan02.setBlades(12)
output.innerHTML += fan02.getBlades() + '<br>'


// 扇風機の統計情報の表示
Fan.statisticsOutput = document.getElementById('output')
Fan.infoFans()