// 出力準備
// 変数outputを宣言して初期化。HTML ID('output')を取得
const output = document.getElementById('output'); 
// 入力準備
const input = document.getElementById('input');
// 後で変化する可能性がない場合はconstを使う。今回は変化しないのでconst

// 人物分岐用定数、CSSのクラス名と一緒
// switch関数の時定数constを置く
// constは大文字
// Aさんテーマ色:赤
const ASAN = 'A';
// Bさんテーマ色:青
const BSAN = 'B';

// 関数Functionはsendボタンが押されたときに実行する内容
// HTMLで決めたonclick=send
function send(sender) {
    // Date関数をつかってnow(時刻)を取得
    const now = new Date();
    // now(時刻)をtimestamp(日本の形式)になおす
    const timestamp = now.toLocaleString('ja-JP');

    // 変数msgの中身は、HTMLのinputを持ってくる
    // .valueはinputの現在の値を取得
    //  <input type="text" id="input" placeholder="ここに入力してください">
    let msg = input.value;

    // もし、inputがなにもないときは何もしない
    if (input.value === '') {
        return;
    }

    // Switch関数でボタンを押された時の動きを切り替える
    switch (sender) {
        // Aさんの場合
        case 'A':
            // 一番最初の出力準備で作ったoutputに出力する。
            // innerHTMLはHTMLの><の中身に上書き
            // <div id="output">'ここに入る'</div>
            // メッセージを赤色で出力。CSS<div class="ASAN">
            // テンプレートリテラル${}中に変数を入れてまとめられる。
            // outputのinnerHTML に `<div class="ASAN">${timestamp} Aさん: ${msg}</div>`;を代入
            output.innerHTML += `<div class="ASAN">${timestamp} Aさん: ${msg}</div>`;
            break;

        // Bさんの場合
        case 'B':
            // メッセージを青色で出力。CSS<div class="BSAN"> 
            output.innerHTML += `<div class="BSAN">${timestamp} Bさん: ${msg}</div>`;
            break;

        // エラーメッセージ
        default:
            break;
    }

    // 送信したら入力欄をクリア
    // HTMLのボタンがJavaScriptの定数と一致し、メッセージを送信した後に入力フィールドがクリアされる
    // 変数inputの現在の値を取得して''を代入
    input.value = '';
}

// リセットの()はSwitchで分岐しないのでいらない
function reset() {
    // 出力部分をクリア
    // innerHTMLはHTMLの><の中身に上書き
    output.innerHTML = '';
    // 入力欄をクリア
    // .valueは入力フィールドinputの現在の値を取得
    input.value = '';
}
