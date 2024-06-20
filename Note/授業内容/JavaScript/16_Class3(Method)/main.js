// クラスについて
// メソッド編

// 出力先の要素を習得
let output = document.getElementById('output')

// クラスの宣言
class Fan {
    // プロパティ(属性、状態)
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

    // メソッド(関数)
    // メソッドはfuctionいらない
    // 代入できる

    // 首振りボタンが押された時
    // 引数、戻り値無しのメソッド
    // 関数とは違いfunctionは書かなくて良い
    
    pressSwingButton() {
        output.innerHTML += '首振りボタンが押されました。'
        // thisは自分自身(オブジェクト(インスタンス))を示す
        this.swing = true
    }

}

// インスタンス化
// fan01,fan02はそれぞれ状態を持ってる(別物)
let fan01 = new Fan()
let fan02 = new Fan()

// swingは初期化されてないのでundefined(未定義)
output.innerHTML += fan01.swing + '<br>'

// fan01のメソッドの呼び出し
// 首振りボタンを押したのでtrueになった
fan01.pressSwingButton() + '<br>'
output.innerHTML += fan01.swing + '<br>'

// fan02のメソッドの呼び出し
output.innerHTML += fan02.swing + '<br>'
fan02.pressSwingButton() + '<br>'
output.innerHTML += fan02.swing + '<br>'


// エラー
// null　型が決まってるけど中身がない
// void リターンがない
// enpty 空