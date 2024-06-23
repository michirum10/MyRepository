import Cart from './Cart.js';

document.addEventListener('DOMContentLoaded', () => {

    const cartList = document.getElementById('cart-list');
    const totalPriceElement = document.getElementById('total-price');
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
