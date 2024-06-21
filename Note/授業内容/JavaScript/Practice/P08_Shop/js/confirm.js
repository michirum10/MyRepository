// js/confirm.js

import Cart from './Cart.js';

let cart;

window.onload = function () {
    resetCart();
    displayCartItems();
    
    const purchaseButton = document.getElementById('purchaseButton');
    purchaseButton.addEventListener('click', handlePurchase);
};

function displayCartItems() {
    const cartContents = document.getElementById('cartContents');
    cart.getItems().forEach(item => {
        const cartItem = document.createElement('div');
        cartItem.textContent = `${item.name} - 価格: ${item.price}円`;
        cartContents.appendChild(cartItem);
    });
}

function handlePurchase() {
    cart.purchase();
    sessionStorage.removeItem('cart');
    console.log('購入が完了しました。カートの中身を空にしました。');

    window.location.href = 'complete.html';
}

function resetCart() {
    const cartData = sessionStorage.getItem('cart');
    cart = cartData ? new Cart(JSON.parse(cartData)) : new Cart();
}
