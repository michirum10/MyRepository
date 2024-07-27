// main.js
// 猫は配列に格納されている

// 出力準備
let output = document.getElementById('output');
let fetchButton = document.getElementById('fetchButton');
let loadingIndicator = document.querySelector('.loading');

// 実行する関数(capture)を宣言
function capture() {
    // 画像取得前に表示
    output.alt = "画像取得中";
    output.src = ""; // 画像をクリア
    output.style.display = "none"; // 画像を非表示
    loadingIndicator.style.display = "block"; // ローディングインジケータを表示

    // fetchはデータの取得(非同期通信)
    fetch('https://api.thecatapi.com/v1/images/search')
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
            output.src = json[0].url; // 配列の最初の要素からURLを取得
            output.alt = "猫の画像取得完了";
            output.style.display = "block"; // 画像を表示
        })
        .catch(error => {
            console.error('エラーが発生しました:', error);
            output.alt = "画像の取得に失敗しました";
        })
        .finally(() => {
            loadingIndicator.style.display = "none"; // ローディングインジケータを非表示
        });
}

// ボタンクリック時に猫画像を取得
fetchButton.addEventListener('click', capture);