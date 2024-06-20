// クラスについて
// プロパティ(属性)編

// 出力先の要素を習得
let output = document.getElementById('output')

// クラスの宣言
class Fan {
    // プロパティ(状態)
    // そのオブジェクトが持つ状態(変数)の事

    // 羽根の枚数(何枚)
    blades
    // 風力(強/弱)
    windPower
    // 電源(ON/OFF)
    power
    // 首振り(縦横)
    swing
    // 状態の出力先(どこに出力するか)
    output

}

// インスタンス化
let fan01 = new Fan()

// プロパティへのアクセス方法

// 代入
// 基本的にはプロパティ(属性)に値を直接入力しない
// fan01の羽根の枚数が7枚である事を示す
fan01.blades = 7
// fan01の風力を1(弱)にする。
fan01.windPower = 1

// 取得
output.innerHTML += fan01.blades + '<br>'
output.innerHTML += fan01.windPower + '<br>'