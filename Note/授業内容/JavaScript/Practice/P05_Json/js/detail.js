// 05 detail　従業員詳細
// 配列
// 画面遷移。ループしない。クリックしたら同じスライムが表示される

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
        // "../data/data.json"でスライム
        fetch("../data/data.json")
            // response(URLから受け取った情報)をjsonに変換
            .then(response => response.json())
            // JSONデータを受け取って処理
            .then(json => {
                // コンソールログに表示
                console.log(json);

                // 変数membersHTMLを宣言して初期化
                let membersHTML = '';

                // ループ処理を外すjson.members.forEach(function (member){
                // 各変数をmenbersにする
                // 変数名はjsonを参照

                // 説明リストで見た目を整える
                // 画像データのパスは "../data/${member.img}" にする(相対パス)
                // テンプレートリテラル`${}`で囲む

                // 配列を参照するときはjson.JSONの変数[配列番号].個別の変数名
                // json.members[0].name　→　jsonのmembersの[0]番目のname
                // members情報の何番目を参照するか指定する[0]、[1]、[2]...
                // それぞれを参照するtときは[index]と置く
                membersHTML += `
                        <dl>
                            <dt>名前</dt>
                            <dd>${json.members[0].name}</dd>
                            <dt>年齢</dt>
                            <dd>${json.members[0].age}</dd>
                            <dt>写真</dt>
                            <dd><img src="../data/${json.members[0].img}"></dd>
                            <dt>詳細</dt>
                            <dd>${json.members[0].detail}</dd>
                        </dl>
                    `;

                // "json.members.forEach"　の　"}" と ")"
                // });

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
// .で続ける