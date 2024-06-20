// クラスについて
// コードの最適化

//モジュールのインポート(default)、標準モジュール取り込み
import Fan from './Fan.js'
// Fanの中身は見なくても良い
// ブラックボックスにしておく

// モジュールのインポート、モジュール出力
// 複数あるときは、｛｝で指定する
// import { Fan } from './Fan.js'


// 出力先の要素を習得
let output = document.getElementById('output')

// インスタンス化
// 羽根の枚数を指定なし
let fan01 = new Fan(output)
// 羽根の枚数を指定あり
let fan02 = new Fan(output, 7)

output.innerHTML += fan01.swing + '<br>'
// fan01のメソッドの呼び出し
fan01.pressSwingButton() + '<br>'
output.innerHTML += fan01.swing + '<br>'
output.innerHTML += fan01.blades + '<br>'

output.innerHTML += fan02.swing + '<br>'
// fan02のメソッドの呼び出し
fan02.pressSwingButton() + '<br>'
output.innerHTML += fan02.swing + '<br>'
output.innerHTML += fan02.blades + '<br>'

// 扇風機の統計情報の表示
// 標準出力の設定
Fan.statisticsOutput = document.getElementById('output')
Fan.infoFans()