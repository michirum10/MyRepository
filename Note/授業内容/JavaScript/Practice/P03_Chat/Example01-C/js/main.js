// CSSのクラス名、人物分岐用定数
// Asanテーマ色:赤
const Asan = 'Asan'
// Bsanテーマ色:青
const Bsan = 'Bsan'

// チャットの入力欄
const input = document.getElementById('input')
// チャットログ(出力先)
const output = document.getElementById('output')

// チャットを送信する関数
// name:誰のメッセージなのか？ Asan か Bsan
function sendMessage(name){
    // テンプレートリテラル
    // CSSで使うclassの名前を設定
    let className = `${name} msg`
    // let className = name + ' msg'
    // let time = (yyyy+1) + '年' + MM + '月' + dd + '日'
    // let time = `${yyyy+1}年${MM}月${dd}日`

    // CSSのclassの設定とチャットの内容の出力するタグを生成
    let inputStr = `<dd class='${className}'>${input.value}</dd>`

    // 過去のチャットログを残すために加算代入を行っています。
    output.innerHTML += inputStr
    // 入力エリアの削除
    input.value = ''
}

// リセットの関数
function reset(){
    // ログと入力エリアの削除
    output.innerHTML = ''
    input.value = ''
}
