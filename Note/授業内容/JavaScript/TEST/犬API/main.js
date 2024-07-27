// main.js
// 出力準備
let output = document.getElementById('output');
let fetchButton = document.getElementById('fetchButton');

// 実行する関数(capture)を宣言
function capture() {
    // jsonデータ取得前に表示
    output.alt = "画像取得中";
    output.src = ""; // 画像をクリア

    // fetchはデータの取得(非同期通信)
    fetch('https://dog.ceo/api/breeds/image/random')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(json => {
            // コンソールログに表示
            console.log(json);
            // ここに出力する内容
            output.src = json.message;
            output.alt = "画像取得完了";
        })
        .catch(error => {
            console.error('エラーが発生しました:', error);
            output.alt = "画像の取得に失敗しました";
        });
}

// ボタンクリック時に犬画像を取得
fetchButton.addEventListener('click', capture);

// ページ読み込み時に初期画像を取得
document.addEventListener('DOMContentLoaded', capture);