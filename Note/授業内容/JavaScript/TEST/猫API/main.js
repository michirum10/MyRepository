// 出力準備
let output = document.getElementById('output');

// 実行する関数(capture)を宣言
function capture() {
    // 画像取得前に表示
    output.alt = "画像取得中";
    output.src = ""; // 画像をクリア

    // fetchはデータの取得(非同期通信)
    fetch('https://api.thecatapi.com/v1/images/search')
        .then(response => response.json())
        .then(json => {
            // コンソールログに表示
            console.log(json);
            // The Cat APIは配列を返すので、最初の要素を使用
            if (json.length > 0) {
                output.src = json[0].url;
                output.alt = "猫の画像";
            } else {
                output.alt = "画像が見つかりませんでした";
            }
        })
        .catch(error => {
            console.error('エラーが発生しました:', error);
            output.alt = "画像の取得に失敗しました";
        });
}

// ボタンにイベントリスナーを追加
document.getElementById('captureButton').addEventListener('click', capture);