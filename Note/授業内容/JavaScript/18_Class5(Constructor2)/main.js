// クラスについて
// コンストラクタ2編(引数とデフォルト引数を準備)

// 出力先の要素を習得
let output = document.getElementById('output')

// クラスの宣言
class Fan {
    // プロパティ
    // 羽根の枚数
    blades
    // 風力
    windPower
    // 電源
    power
    // 首振り
    swing
    // 状態の出力先
    output

    // コンストラクタ(メソッド)の宣言
    // 汎用性をもたせる。(引数とデフォルト引数を利用)
    constructor(output,blades=5) {
        // 各値を初期化
        
        // 引数(output,blades)を代入
        // オブジェクト化されてるときはthisをつける
        this.output = output
        this.blades = blades
        this.windPower = 0
        this.power = false
        this.swing = false
    }

    // メソッド(関数)
    // 首振りボタン押下
    pressSwingButton(){
        output.innerHTML += '首振りボタンが押されました。' + '<br>'
        this.swing = true
    }

}

// インスタンス化
// 羽根の枚数を指定なし
let fan01 = new Fan(output)
// 羽根の枚数を指定あり
let fan02 = new Fan(output,7)

output.innerHTML += fan01.swing + '<br>'
// fan01のメソッドの呼び出し
fan01.pressSwingButton() + '<br>'
output.innerHTML += fan01.swing + '<br>'
output.innerHTML += fan01.blades + '<br>'

output.innerHTML += fan02.swing + '<br>'
// fan02のメソッドの呼び出し
fan02.pressSwingButton() + '<br>'
output.innerHTML += fan02.swing + '<br>'
output.innerHTML += fan01.blades + '<br>'
