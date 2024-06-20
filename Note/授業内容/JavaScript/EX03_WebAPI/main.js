// JSONデータの取得方法
// ボタンを押したら犬の画像が出てくる

// 出力準備
let output = document.getElementById('output')

// 遅延実行でもある
// fetchが終わった後に.then.thenを実行する

// 実行する関数(capture)を宣言
// 関数は一連の処理をまとめたもの。ブロック
function capture() {
    // jsonデータ取得前に表示
    output.alt = "画像取得中"

    // fetchはデータの取得(非同期通信)
    // 引数にはデータのURL（相対パス）
    // response(URLから受け取った情報)をjsonに変換
    fetch('https://dog.ceo/api/breeds/image/random')
        // response(urlから受け取った情報)をjsonに変換
        .then(response => response.json())
        // JSONデータを受け取って処理
        .then(json => {
            // コンソールログに表示
            console.log(json)
            // ここに出力する内容
            output.src = json.message
            output.alt = "画像取得完了"
        })
    // function capture()はonclick="capture()"なのでクリックされたら実行
}