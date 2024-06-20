// 値が変化する、取得する要素を予め変数に格納しておく
// よく使うから上(カッコの外)に書いておく
let output = document.getElementById('output')

//定数 は全部大文字
// 意味は殆どない
// 可読性を上げるために定数を利用。
const PLUS = 1
const MINUS = 2
const RESET = -1

// 上に書いておくとゼロからカウントしてくれる
let counter = 0
// 出力文字列の生成(テンプレートリテラル)
// 最適化
output.textContent = `カウンター：${counter}`
// let書く
// 書き忘れると勝手にvarになる
// ↓ちょっと重くなる
// let msg = `カウンター：${counter}`
// output.textContent = msg

// どのボタンを押されたのか
// モードで書くときはSwitchにする
// 黄色(mode)は仮引数(ただの変数)
// 後で確定する
function btn(mode) {
    switch (mode) {

        // ++ 押すたびに1足す
        case PLUS:
            counter++
            break;
        // -- 押すたびに1引く
        case MINUS:
            counter--
            break;
        //  ゼロを入力してリセットに見せる
        case RESET:
            counter = 0
            break;
        default:
            break;
    }

// 出力文字列の生成(テンプレートリテラル)
// バッククォーテーション。@のとこShift押しながら
// $でいい感じにしてくれる
// スコープ中のletが優先される
// letない場合ややこしい
// このときだけ使う
// メッセージとして'カウンター'とcounter関数を表示する
    let msg = `カウンター：${counter}`
    output.textContent = msg
}
