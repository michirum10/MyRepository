// index.js 商品一覧

//  商品名と値段、画像を表示(ローカルのdata.jsonからデータを取得する)
// それらをクリックすると商品詳細画面へ遷移(新しくウィンドウを開く)
// 購入ボタン⇛購入確認画面へ遷移

// indexには商品一覧をJSONデータから取得して表示

// // cartクラスをインポートする
// import cart from './Cart.js'
// import { itemList } from './itemDisplay.js';

// // let 変数名 = new クラス名();
// const cart = new Cart();

// 画面が読み込まれたら表示
window.onload = function () {
    // 出力準備
    let output = document.getElementById('output');

    function itemList() {
        // jsonデータを取得
        fetch('../data/data.json')
            .then(response => response.json())
            .then(json => {

                // console.log(#itemlist)
                console.log(json);

                // ID=itemsを取得
                // let itemDiv = '';
                // json.itemsのそれぞれのitemを取得してループ   
                json.items.forEach(function (item, index) {
                    // divタグの生成をしたい

                    // bootstrapカードの生成
                    let card = document.createElement('div');
                    // クラスを指定
                    card.classList.add('card', 'mb-3', 'item');
                    card.style.width = '18rem';

                    // カード全体のクリックイベント
                    card.addEventListener('click', function () {
                        // 新しいウィンドウで詳細画面を開く
                        window.open(`../html/detail.html?index=${index}`, '_blank');
                    });

                    // カードボディ(大枠)の生成
                    let cardBody = document.createElement('div');
                    cardBody.classList.add('card-body');

                    // カード画像の生成
                    let cardImg = document.createElement('img');
                    // 相対パスで画像を取得
                    cardImg.src = `../img/${item.img}`
                    cardImg.classList.add('card-img-top');
                    card.appendChild(cardImg);

                    // 商品名
                    let cardTitle = document.createElement('h5');
                    cardTitle.classList.add('card-title');
                    cardTitle.textContent = item.name;
                    cardBody.appendChild(cardTitle);

                    // 商品価格
                    let cardText = document.createElement('p');
                    cardText.classList.add('card-text');
                    cardText.textContent = `価格: ${item.price}円`;
                    cardBody.appendChild(cardText);

                    // 詳細ボタンの生成
                    const detailBtn = document.createElement('button');
                    detailBtn.classList.add('btn', 'btn-primary');
                    detailBtn.textContent = '詳細';

                    // 詳細ボタン押したら詳細画面に遷移
                    detailBtn.addEventListener('click', function () {
                        // 新しいウィンドウで詳細画面を開く
                        window.open(`../html/detail.html?index=${index}`, '_blank');
                    });

                    // カードボディ(親)に購入ボタンを追加
                    cardBody.appendChild(detailBtn);

                    // カード(親)にボディを追加
                    card.appendChild(cardBody);

                    // 出力要素(親)にカードを追加
                    output.appendChild(card);

                });

            });
    }
    itemList()
}

// // イベント指定
// btn.addEventListener('click')
// divタグの生成
// let block = document.createElement('div')
// addEventListenerを使用してクリックイベントを設定
// detailBtn.addEventListener('click', function () {
//     addToCart(item);
// });