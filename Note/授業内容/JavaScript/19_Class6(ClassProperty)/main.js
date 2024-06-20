// クラスについて
// クラスプロパティ編

// クラスプロパティ
// プロパティ
// コンストラクタ
// メソッド
// 書く場所気をつける

// 出力先の要素を習得
let output = document.getElementById('output')

// クラスの宣言
class Fan {

    // 台数
    // クラスプロパティ(クラス変数)の定義
    // static:静的変数(オブジェクト同士で共通の値)
    static number = 0

    // 風量
    // クラスプロパティ(クラス定数(変数))の定義
    // 定数として大文字で書いてるが、変更可能
    // windPowerの日本語名称の統一用
    // 連想配列
    static POWER_STATUS = { OFF: '切', P1: '弱', P2: '中', P3: '強' }


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
    constructor(output, blades = 5) {
        // クラスプロパティ(クラス変数)のアクセス
        // クラス名.プロパティ名
        // 扇風機を一台追加
        Fan.number++

        // 各値を初期化
        // オブジェクト化されてるときはthisをつける
        this.output = output
        this.blades = blades
        // クラスプロパティ(クラス定数(変数))のアクセス
        // FanクラスのPOWER_STATUSのOFFを呼び出し
        this.windPower = Fan.POWER_STATUS.OFF
        this.power = false
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

// クラスプロパティ(クラス変数)のアクセス
output.innerHTML += `扇風機の台数は全部で${Fan.number}台です。`