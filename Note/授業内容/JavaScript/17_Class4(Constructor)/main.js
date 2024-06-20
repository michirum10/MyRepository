// クラスについて
// コンストラクタ１編(メソッド)

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
    // プロパティを初期化するのが目的のメソッド(undefined出ないようにする)
    // 首振りオフなのでfalseと表示
    constructor() {
        // オブジェクト化されてるときはthisをつける
        this.output = document.getElementById('output')
        // 羽5枚
        this.blades = 5
        // 風力0(オフ)
        this.windPower = 0
        // 電源オフ
        this.power = false
        // 首振りオフ
        this.swing = false
    }

    // メソッド(関数)
    // 首振りボタン押下
    pressSwingButton() {
        output.innerHTML += '首振りボタンが押されました。' + '<br>'
        this.swing = true
    }

}

// インスタンス化
let fan01 = new Fan()
let fan02 = new Fan()

output.innerHTML += fan01.swing + '<br>'
// fan01のメソッドの呼び出し
fan01.pressSwingButton() + '<br>'
output.innerHTML += fan01.swing + '<br>'

output.innerHTML += fan02.swing + '<br>'
// fan02のメソッドの呼び出し
fan02.pressSwingButton() + '<br>'
output.innerHTML += fan02.swing + '<br>'
