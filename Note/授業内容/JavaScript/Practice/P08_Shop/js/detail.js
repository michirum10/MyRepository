// detail.js 商品詳細
// 一つのクリックした商品の情報を表示する
// （商品名と値段、画像、説明を大きく表示する。）
// カートに入れるボタン⇛カートにデータを追加

// カート機能のモジュールをインポート
import Cart from './Cart.js';
// itemDetails関数をインポート
import { itemDetails } from './displayItems.js'; 

// 画面が読み込まれたら実行
// window.onload = function () {

// DOMが読み込まれたら実行（window.onloadより速いらしい）
document.addEventListener('DOMContentLoaded', function () {

    // 出力準備
    const output = document.getElementById('output');

    // セッションストレージから選択された商品情報を取得
    const item = JSON.parse(sessionStorage.getItem('selectedItem'));
    // 商品情報が存在する場合、詳細情報を表示
    if (item) {
        itemDetails(item, output);  //ここにoutput
    } else {
        output.innerHTML = '<p>商品情報が見つかりませんでした。</p>';
    }

    // ページ読み込み時にカート表示を更新
    Cart.updateCartDisplay();
});

// Bootstrap戻るボタン
document.getElementById('back-button').addEventListener('click', () => {
    window.location.href = 'index.html';
});

// displayItems.jsでまとめたので不要

// // 商品の詳細情報を表示する関数
// function itemDetails(item, output) {

//     output.innerHTML = ''; // 初期化

//     // 商品情報を表示するためのBootstrapカードの生成
//     const card = document.createElement('div');
//     card.classList.add('card', 'mb-3', 'item'); // クラスを指定
//     card.style.width = '18rem'; // カードの幅を指定

//     // カードボディの生成
//     const cardBody = document.createElement('div');
//     cardBody.classList.add('card-body'); // クラスを指定

//     // カード画像の生成
//     const cardImg = document.createElement('img');
//     cardImg.src = `../img/${item.img}`; // 画像パスを設定
//     cardImg.alt = `${item.name}の画像`;
//     cardImg.classList.add('card-img-top'); // クラスを指定
//     card.appendChild(cardImg); // カードに画像を追加

//     // 商品名の生成
//     const cardTitle = document.createElement('h5');
//     cardTitle.classList.add('card-title'); // クラスを指定
//     cardTitle.textContent = item.name; // 商品名を設定
//     cardBody.appendChild(cardTitle); // カードボディに商品名を追加

//     // 商品価格の生成
//     const cardText = document.createElement('p');
//     cardText.classList.add('card-text'); // クラスを指定
//     cardText.textContent = `価格: ${item.price}円`; // 商品価格を設定
//     cardBody.appendChild(cardText); // カードボディに価格を追加

//     // 商品説明の生成
//     const cardDetail = document.createElement('p');
//     cardDetail.textContent = item.detail; // 商品説明を設定
//     cardBody.appendChild(cardDetail); // カードボディに商品説明を追加

//     // 購入ボタンの生成
//     const buyButton = document.createElement('button');
//     buyButton.classList.add('btn', 'btn-primary'); // クラスを指定
//     buyButton.textContent = 'カートに追加'; // ボタンのテキストを設定

//     // addEventListenerを使用してクリックイベントを設定
//     buyButton.addEventListener('click', () => {

//         // カートに商品を追加
//         Cart.addItem(item);
//         // カート表示を更新
//         Cart.updateCartDisplay();
//         // 追加されたらpopup表示
//         alert(`${item.name}をカートに追加しました`);
//         window.location.href = 'confirm.html';
//     });

//     // カードボディに購入ボタンを追加
//     cardBody.appendChild(buyButton);

//     // カードにボディを追加
//     card.appendChild(cardBody);

//     // 出力要素にカードを追加
//     output.appendChild(card);
// }