// itemDisplay.js
import Cart from './Cart.js';

const cart = new Cart();

export function displayItemDetails(data, index, output) {
    
    const itemIndex = parseInt(index);
    if (itemIndex !== null && itemIndex >= 0 && itemIndex < data.items.length) {
        const item = data.items[itemIndex];
        itemDetails(item, output);
    } else {
        output.innerHTML = '<p>商品情報が見つかりませんでした。</p>';
    }
}

function itemDetails(item, output) {
    output.innerHTML = '';

    const card = document.createElement('div');
    card.classList.add('card', 'mb-3', 'item');
    card.style.width = '18rem';

    const cardImg = document.createElement('img');
    cardImg.src = `../img/${item.img}`;
    cardImg.alt = `${item.name}の画像`;
    cardImg.classList.add('card-img-top');
    card.appendChild(cardImg);

    const cardBody = document.createElement('div');
    cardBody.classList.add('card-body');

    const cardTitle = document.createElement('h5');
    cardTitle.classList.add('card-title');
    cardTitle.textContent = item.name;
    cardBody.appendChild(cardTitle);

    const cardText = document.createElement('p');
    cardText.classList.add('card-text');
    cardText.textContent = `価格: ${item.price}円`;
    cardBody.appendChild(cardText);

    const cardDetail = document.createElement('p');
    cardDetail.textContent = item.detail;
    cardBody.appendChild(cardDetail);

    const buyButton = createBuyButton(item);
    cardBody.appendChild(buyButton);

    card.appendChild(cardBody);
    output.appendChild(card);
}

// 購入ボタン作成関数
function createBuyButton(item) {
    const buyButton = document.createElement('button');
    buyButton.classList.add('btn', 'btn-primary');
    buyButton.textContent = 'カートに追加';
    buyButton.setAttribute('aria-label', `${item.name}をカートに追加`);
    buyButton.addEventListener('click', (event) => {
        event.stopPropagation();
        addToCart(item);
    });
    return buyButton;
}

// カートに商品を追加する関数
function addToCart(item) {
    cart.addItem(item);
    alert(`${item.name}をカートに追加しました。\nカート内の商品数: ${cart.getItemCount()}`);
    updateCartDisplay();
console.log(cart.itemList);
}

// カート表示を更新する関数
function updateCartDisplay() {
    const cartCountElement = document.getElementById('cart-count');
    if (cartCountElement) {
        cartCountElement.textContent = cart.getItemCount();
    }
}

// 商品一覧表示関数（新規追加）
export function displayItemList(items, output) {
    output.innerHTML = '';

    items.forEach((item, index) => {
        const card = createItemCard(item);
        card.style.cursor = 'pointer';
        card.addEventListener('click', () => {
            window.location.href = `detail.html?index=${index}`;
        });
        output.appendChild(card);
    });
}

// 商品カード作成関数（共通部分を抽出）
function createItemCard(item) {
    const card = document.createElement('div');
    card.classList.add('card', 'mb-3', 'item');
    card.style.width = '18rem';

    const cardImg = document.createElement('img');
    cardImg.src = `../img/${item.img}`;
    cardImg.alt = `${item.name}の画像`;
    cardImg.classList.add('card-img-top');
    card.appendChild(cardImg);

    const cardBody = document.createElement('div');
    cardBody.classList.add('card-body');

    const cardTitle = document.createElement('h5');
    cardTitle.classList.add('card-title');
    cardTitle.textContent = item.name;
    cardBody.appendChild(cardTitle);

    const cardText = document.createElement('p');
    cardText.classList.add('card-text');
    cardText.textContent = `価格: ${item.price}円`;
    cardBody.appendChild(cardText);

    card.appendChild(cardBody);
    return card;
}

// 初期表示時にカート表示を更新
updateCartDisplay();

export { updateCartDisplay };
