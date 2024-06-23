// Cart.js - カート機能を提供するクラス

// Cartクラスをエクスポート
export default class Cart {

    // カート内の商品リストを取得する
    static getItems() {
        // セッションストレージからカートデータを取得
        const cartData = sessionStorage.getItem('cart');

        // カートデータが存在する場合はJSONを返し、存在しない場合は空配列を返す
        const items = cartData ? JSON.parse(cartData) : [];
        console.log('[Cart] getItems: items:', items);

        return items;
    }

    // カートに商品を追加する
    static addItem(item) {
        console.log('[Cart] addItem: item:', item);
        // 現在のカート内容を取得
        const items = Cart.getItems();
        // 新しい商品をカートに追加
        items.push(item);
        // 更新されたカート内容をセッションストレージに保存
        sessionStorage.setItem('cart', JSON.stringify(items));
        console.log('[Cart] addItem: cart data saved:', sessionStorage.getItem('cart'));
    }

    // カートから商品を削除する
    static removeItem(index) {
        // 現在のカート内容を取得
        const items = Cart.getItems();
        // 指定されたインデックスの商品を削除
        items.splice(index, 1);
        console.log('[Cart] removeItem: updated cart:', items);
        // 更新されたカート内容をセッションストレージに保存
        sessionStorage.setItem('cart', JSON.stringify(items));
        // カートを再描画する
        // カートリストの要素を取得
        const cartList = document.getElementById('cart-list');
        // 削除後のカート内容を再度表示
        Cart.displayCart(cartList);
    }

    // カートをクリアする（商品を削除）
    static clearCart() {
        // セッションストレージからカートデータを削除
        sessionStorage.removeItem('cart');
    }

    // カートの合計金額を計算する
    static getTotal() {
        // カート内の全商品の価格を合計して返す
        return Cart.getItems().reduce((total, item) => total + item.price, 0);
    }

    // カートの商品リストを表示する
    static displayCart(container) {

        // カート内の商品を取得
        const items = Cart.getItems();
        console.log('[Cart] displayCart: items:', items);

        // 各商品をHTML形式で表示
        // BootStrapのリスト化を使う
        // 削除ボタンを追加(confirm.jsのイベントリスナーで削除)
        // data-index="${index}:削除するindexを指定
        container.innerHTML = items.map((item, index) => `
        <li class="list-group-item d-flex align-items-center">
            <img src="../img/${item.img}" alt="${item.name}" style="width: 50px; height: 50px; object-fit: cover;">
            <span class="ms-3 flex-grow-1">${item.name}</span>
            <span class="me-3">${item.price}円</span>
            <button class="btn btn-danger btn-sm btn-delete" data-index="${index}">削除</button>
        </li>
         `).join('');  // join？
    }

    // カート表示の更新（カート内の商品数を表示）
    static updateCartDisplay() {
        // カート内の商品数を表示する要素を取得
        const cartCountElement = document.getElementById('cart-count');
        if (cartCountElement) {
            // カート内の商品数を設定
            const cartItems = Cart.getItems();
            cartCountElement.textContent = cartItems.length;
            console.log('[Cart] updateCartDisplay: cartItems:', cartItems);
        }
    }
}
