// index.js
// 商品名と値段、画像を表示(ローカルのdata.jsonからデータを取得する)
// それらをクリックすると商品詳細画面へ遷移(新しくウィンドウを開く)
// 購入ボタン⇛購入確認画面へ遷移

// カート機能のモジュールをインポート
import Cart from './Cart.js';
// displayItems関数をインポート
import { displayItems } from './displayItems.js'; // displayItems関数をインポート

// // 画面が読み込まれたら実行
// window.onload = function () {

// DOMが読み込まれたら実行（window.onloadより速いらしい）
document.addEventListener('DOMContentLoaded', function () {

    // 出力準備
    const output = document.getElementById('output');

    // JSONデータを取得
    fetch('../data/data.json')
        .then(response => response.json())
        .then(json => {
            // 商品一覧を表示
            displayItems(json.items, output);  //ここにoutput
        });
        

    // 購入確認ページへ
    document.getElementById('confirm-button').addEventListener('click', () => {
        window.location.href = 'confirm.html';
    });

    // カート表示の更新
    Cart.updateCartDisplay();

});

// displayItems.jsでまとめたので不要

// // 商品一覧を表示
// function displayItems(items) {
//     // 初期化
//     output.innerHTML = '';

//     items.forEach((item, index) => {

//         // Bootstrapカードの生成
//         let card = document.createElement('div');
//         card.classList.add('card', 'mb-3', 'item');
//         card.style.width = '18rem';
//         card.style.cursor = 'pointer'; // カーソルをポインターに変更;

//         // カード全体のクリックイベント
//         card.addEventListener('click', function () {
//             // 詳細画面に遷移
//             goToDetailPage(item);
//         });

//         // カードボディの生成
//         let cardBody = document.createElement('div');
//         cardBody.classList.add('card-body');

//         // カード画像の生成
//         let cardImg = document.createElement('img');
//         cardImg.src = `../img/${item.img}`;
//         cardImg.classList.add('card-img-top');
//         card.appendChild(cardImg);

//         // 商品名
//         let cardTitle = document.createElement('h5');
//         cardTitle.classList.add('card-title');
//         cardTitle.textContent = item.name;
//         cardBody.appendChild(cardTitle);

//         // 商品価格
//         let cardText = document.createElement('p');
//         cardText.classList.add('card-text');
//         cardText.textContent = `価格: ${item.price}円`;
//         cardBody.appendChild(cardText);

//         // 詳細ボタンの生成
//         const detailBtn = document.createElement('button');
//         detailBtn.classList.add('btn', 'btn-primary');
//         detailBtn.textContent = '詳細';

//         // カードに詳細ボタンを追加
//         cardBody.appendChild(detailBtn);

//         // カードにボディを追加
//         card.appendChild(cardBody);

//         // 出力要素にカードを追加
//         output.appendChild(card);
//     });
// }

// // 詳細ページに遷移
// function goToDetailPage(item) {
//     sessionStorage.setItem('selectedItem', JSON.stringify(item));
//     window.location.href = '../html/detail.html';
// }