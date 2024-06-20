// comment(入力フォームの内容)、msg(表示内容)を準備
let comment = document.getElementById('comment')
let msg = document.getElementById('msg')

function chat(mode) {
    // Date関数をつかってnow(時刻)を取得
    const now = new Date();
    // now(時刻)をtimestamp(日本の形式)になおす
    const timestamp = now.toLocaleString('ja-JP');

    if(comment.value == ''){
        // 入力フォームが空のときは何もしない
        return;
    }

    // switch-caseを使って分岐　お好みで
    switch (mode) {
        case 'A':
            // Aさん出力部分に入力部分の内容が出力される(赤色)
            // timestamp(取得した時刻)、色変更用のclassを入れたpタグをテンプレートリテラルを使ってむりやり埋め込む
            // msg(表示内容)を追記する
            msg.innerHTML += `<p class="coma">${timestamp} : Aさん<br>${comment.value}</p>`
            // 入力フォームの消去
            comment.value = ''
            break;
        case 'B':
            // Bさん出力部分に入力部分の内容が出力される(青色)  
            // timestamp(取得した時刻)、色変更用のclassを入れたpタグをテンプレートリテラルを使ってむりやり埋め込む
            // msg(表示内容)を追記する
            msg.innerHTML += `<p class="comb">${timestamp} : Bさん<br>${comment.value}</p>`
            // 入力フォームの消去
            comment.value = ''
            break;
        default:
            break;
    }
}
// 入力フォームが空のときは何もしない処理がリセットボタンにまで効いていたので関数をわける
function resetFields(){
        // 入力フォームの消去
        comment.value = ''
        // msg(表示内容)を消去
        msg.innerHTML = ''
}