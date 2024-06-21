// confirm.js

import Cart from './Cart.js';

console.log('Debug cart:', JSON.parse(sessionStorage.getItem('debugCart')));

window.onload = function() {
    console.log('Cart contents:', cart.itemList);

    const cart = new Cart();
    const output = document.getElementById('output');

    if (cart.itemList.length === 0) {
        output.innerHTML = '<p>カートは空です。</p>';
    } else {
        let totalPrice = 0;
        const itemList = document.createElement('ul');
        itemList.classList.add('list-group');

        cart.itemList.forEach(item => {
            const listItem = document.createElement('li');
            listItem.classList.add('list-group-item', 'd-flex', 'justify-content-between', 'align-items-center');
            
            const itemInfo = document.createElement('div');
            itemInfo.innerHTML = `
                <img src="../img/${item.img}" alt="${item.name}" style="width: 50px; height: 50px; object-fit: cover;">
                <span>${item.name}</span>
            `;
            
            const itemPrice = document.createElement('span');
            itemPrice.textContent = `${item.price}円`;

            listItem.appendChild(itemInfo);
            listItem.appendChild(itemPrice);
            itemList.appendChild(listItem);

            totalPrice += item.price;
        });

        output.appendChild(itemList);

        const totalElement = document.createElement('div');
        totalElement.classList.add('mt-3', 'text-right');
        totalElement.innerHTML = `<strong>合計: ${totalPrice}円</strong>`;
        output.appendChild(totalElement);

        const purchaseButton = document.createElement('button');
        purchaseButton.classList.add('btn', 'btn-primary', 'mt-3');
        purchaseButton.textContent = '購入する';
        purchaseButton.addEventListener('click', function() {
            alert('購入が完了しました！');
            cart.purchase(); // カートをクリア
            window.location.href = 'index.html';
        });
        output.appendChild(purchaseButton);
    }
};
