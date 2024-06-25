import Cart from './Bcart.js';

// DOMが読み込まれたら実行(window.onloadより速いらしい)
document.addEventListener('DOMContentLoaded', () => {

    // 商品表示準備
    const cartList = document.getElementById('cart-list');
    // 合計金額表示準備
    const totalPriceElement = document.getElementById('total-price');
    // 購入ボタン
    const buyButton = document.getElementById('buy-button');
    // 戻るボタン
    const backButton = document.getElementById('back-button');

    // カート内の商品を表示する
    Cart.displayCart(cartList);

    // 合計金額を表示する
    const totalPrice = Cart.getTotal();
    totalPriceElement.textContent = totalPrice;

    // 購入ボタンのイベントリスナー
    buyButton.addEventListener('click', () => {
        // カートをクリアする
        Cart.clearCart();
        // 購入完了画面に遷移する
        window.location.href = '../html/complete.html';
    });

    // 商品一覧へ戻る
    backButton.addEventListener('click', () => {
        window.location.href = 'index.html';
    });


});