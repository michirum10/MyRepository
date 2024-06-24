// confirm.js - 購入確認画面

import Cart from './Cart.js';

// DOMが読み込まれたら実行
document.addEventListener('DOMContentLoaded', () => {

    // DOM要素の取得
    const cartList = document.getElementById('cart-list'); // カート内の商品表示エリア
    const totalPriceElement = document.getElementById('total-price'); // 合計金額表示エリア
    const buyButton = document.getElementById('buy-button'); // 購入ボタン

    // カート内の商品を表示する
    Cart.displayCart(cartList);

    // 合計金額を表示する
    const totalPrice = Cart.getTotal();
    totalPriceElement.textContent = totalPrice;

    // 購入ボタンのクリックイベント
    buyButton.addEventListener('click', () => {
        // カートをクリアする
        Cart.clearCart();
        // 購入完了画面に遷移する
        window.location.href = '../html/complete.html';
    });


    // 戻るボタンのイベントリスナー
    document.getElementById('back-button').addEventListener('click', () => {
        window.history.back();
    });

    // 削除ボタンのクリックイベント
    cartList.addEventListener('click', (event) => {
        // クリックされた要素が削除ボタン（btn-deleteクラスを持つボタン）かどうかを確認
        if (event.target.classList.contains('btn-delete')) {
            // クリックされた削除ボタンのdata-index属性から、削除する商品のインデックスを取得
            const index = parseInt(event.target.dataset.index);

            // カートから商品を削除
            Cart.removeItem(index);

            // 合計金額を更新
            const updatedTotalPrice = Cart.getTotal();
            totalPriceElement.textContent = `${updatedTotalPrice}円`;
        }
    });


});
