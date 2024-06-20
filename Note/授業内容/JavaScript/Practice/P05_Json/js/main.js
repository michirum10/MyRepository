// fetchAPI
// 05 main 従業員一覧

// ウィンドウが完全に読み込まれたらfunctionの中身が実行される
// この中に全部書く
window.onload = function () {

    // 出力準備
    // HTMLのID=outputをJSの変数outputに格納
    let output = document.getElementById('output');

    // json.members情報を取得して表示する準備
    // 実行する関数を宣言
    function empList() {
        // fetchはデータの取得(非同期通信)
        // 引数にはデータのURL(相対パス)
        // "http://192.168.0.32/data/employees"でポケモンJSON
        fetch("../data/data.json")
            // response(URLから受け取った情報)をjsonに変換
            .then(response => response.json())
            // JSONデータを受け取って処理
            .then(json => {
                // コンソールログにJSONデータを表示
                console.log(json);

                // ここからforEachループ
                // 変数membersHTMLを宣言して初期化
                let membersHTML = '';
                // jsonのmembers(member)をそれぞれ取り出す(ループ処理)
                // forEach(function (変数名) {処理})
                json.members.forEach(function (member) {
                    // 説明リストで見た目を整える
                    // 画像データのパスは "../data/${member.img}" にする(相対パス)
                    // "http://192.168.0.32/img/${member.img}"でポケモンJSON
                    // 各変数はjsonを参照
                    // テンプレートリテラル`${}`で囲む
                    // ほとんどのHTMLタグにonclickを付けることができる
                    // onclick="window.location.href = 'URL(相対パス)'"クリックすると詳細画面(index.html)に遷移
                    membersHTML += `
                        <dl onclick="window.location.href = '../html/detail.html'">
                            <dt>名前</dt>
                            <dd>${member.name}</dd>
                            <dt>写真</dt>
                            <dd><img src="../data/${member.img}"></dd>
                        </dl>
                    `;
                // "json.members.forEach"　の　"}" と ")"
                });

                // membersHTMLをoutput.innerHTMLに代入
                output.innerHTML = membersHTML;

            //".then(json　"　の　"}" と ")"
            });

    // "function empList"　の　"}"
    }

    // function empListなのでempList関数を実行する
    // これがないと表示されない
    empList();

// "window.onload = function"　の　"}"
}

// 順番
// window.onload: ページが完全に読み込まれた後に実行される
// function empList: empListを実行する関数
// fetch: JSONデータを取得する
// forEach: JSONデータを一つずつ取り出すループ

// JSONデータの中身は配列の配列
// .は～の～という意味