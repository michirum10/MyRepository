// index.js
// 商品名と値段、画像を表示(ローカルのdata.jsonからデータを取得する)
// それらをクリックすると商品詳細画面へ遷移(新しくウィンドウを開く)
// 購入ボタン⇛購入確認画面へ遷移

// index.js: 商品一覧を表示し、カート機能を初期化する

import Cart from './Cart.js';
// import { displayItems } from './displayItems.js';

// カート
// let cart

// 配列を持ってくる
// セッションストレージからカートの商品リストを読み込み、Cartオブジェクトとして返す
// if(window.sessionStorage.getItem('cartItems')){
// cartItemsの中が存在する時
//   // カートのインスタンス化
//   cart = new Cart(JSON.parse(window.sessionStorage.getItem('cartItems')))
// }else{
// cartItemsの中が存在しない時
//   // カートのインスタンス化
//   cart = new Cart()
// }
// Cart.jsのコンストラクタの中でインスタンス化する
// constructor(itemList=[]){
//     this.#itemList = itemList
// }

// DOMが読み込まれたら実行（window.onloadより速いらしい）
document.addEventListener('DOMContentLoaded', function () {

    const output = document.getElementById('output'); // 商品一覧を表示する要素

    // ローカルのdata.jsonから商品データを取得して表示
    fetch('../data/data.json')
        .then(response => response.json())
        .then(json => {
            displayItems(json.items, output); // 商品データを取得して表示
        });

    // 購入確認ボタンのイベントリスナーを設定
    const confirmButton = document.getElementById('confirm-button');
    if (confirmButton) {
        confirmButton.addEventListener('click', () => {
            window.location.href = 'confirm.html'; // 購入確認ページに遷移
        });
    }

    // カート表示の更新
    Cart.updateCartDisplay(); // カートの表示を更新

    // 親ウィンドウでCartクラスの静的メソッドを定義しておく
    window.Cart = Cart;
    
});


// 商品一覧を表示
function displayItems(items) {
    // 初期化
    output.innerHTML = '';

    items.forEach((item, index) => {

        // Bootstrapカードの生成
        let card = document.createElement('div');
        card.classList.add('card', 'mb-3', 'item');
        card.style.width = '18rem';
        card.style.cursor = 'pointer'; // カーソルをポインターに変更;

        // カード全体のクリックイベント
        card.addEventListener('click', function () {
            // 詳細画面に遷移
            goToDetailPage(item);
        });

        // カードボディの生成
        let cardBody = document.createElement('div');
        cardBody.classList.add('card-body');

        // カード画像の生成
        let cardImg = document.createElement('img');
        cardImg.src = `../img/${item.img}`;
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

        // カードに詳細ボタンを追加
        cardBody.appendChild(detailBtn);

        // カードにボディを追加
        card.appendChild(cardBody);

        // 出力要素にカードを追加
        output.appendChild(card);
    });
}

// 詳細ページに遷移
function goToDetailPage(item) {
    sessionStorage.setItem('selectedItem', JSON.stringify(item));
    window.location.href = '../html/detail.html';
}