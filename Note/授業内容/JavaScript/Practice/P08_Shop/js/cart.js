// js/Cart.js

export default class Cart {
    // カート内の商品リストを取得する
    static getItems() {
        const cartData = sessionStorage.getItem('cart');
        return cartData ? JSON.parse(cartData) : [];
    }

    // カートに商品を追加する
    static addItem(item) {
        const items = Cart.getItems();
        items.push(item);
        sessionStorage.setItem('cart', JSON.stringify(items));
    }

    // カートから特定の商品を削除する
    static removeItem(index) {
        const items = Cart.getItems();
        items.splice(index, 1);
        sessionStorage.setItem('cart', JSON.stringify(items));
    }

    // カートをクリアする
    static clearCart() {
        sessionStorage.removeItem('cart');
    }

    // カートの合計金額を取得する
    static getTotal() {
        return Cart.getItems().reduce((total, item) => total + item.price, 0);
    }

    // カートの商品リストを表示する
    static displayCart(container) {
        const items = Cart.getItems();
        container.innerHTML = items.map((item, index) => `
            <li class="list-group-item d-flex justify-content-between align-items-center">
                <div>
                    <img src="../img/${item.img}" alt="${item.name}" style="width: 50px; height: 50px; object-fit: cover;">
                    <span>${item.name}</span>
                </div>
                <span>${item.price}円</span>
                <button onclick="Cart.removeItem(${index}); Cart.displayCart(this.closest('ul'));" class="btn btn-danger btn-sm">削除</button>
            </li>
        `).join('');
    }

    // カート表示の更新
    static updateCartDisplay() {
        const cartCountElement = document.getElementById('cart-count');
        if (cartCountElement) {
            cartCountElement.textContent = Cart.getItems().length;
        }
    }
}
