// js/complete.js
// 購入完了画面

import Cart from './Cart.js';

document.addEventListener('DOMContentLoaded', () => {
    // 戻るボタンのイベントリスナーを設定
    document.getElementById('back-button').addEventListener('click', () => {
        if (window.opener && !window.opener.closed) {
            // ポップアップウィンドウの場合
            // 元のウィンドウのカートをクリアする
            window.opener.Cart.clearCart();
            window.opener.location.reload(); // 元のウィンドウをリロードしてカートの表示を更新
            window.close(); // 現在のウィンドウを閉じる
        } else {
            // 通常の画面遷移の場合
            Cart.clearCart(); // 現在のページのカートをクリア
            window.location.href = 'index.html'; // index.htmlに戻る
        }
    });
});
