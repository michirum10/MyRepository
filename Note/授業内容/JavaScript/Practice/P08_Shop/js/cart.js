// Cartクラス: カート機能を提供するクラス
// インスタンス化したオブジェクトを操作する
// クラスメソッドは静的メソッド

export default class Cart {
    #itemList = []; // プライベートフィールドとして商品リストを保持する

    /**
     * コンストラクタ: カートを初期化する
     * @param {Array} itemList 初期の商品リスト
     */
    constructor(itemList = []) {
        this.#itemList = itemList;
    }

    /**
     * itemListのgetter: 現在のカート内の商品リストを取得する
     * @returns {Array} 現在の商品リスト
     */
    // アクセサ
    get itemList() {
        return this.#itemList;
    }

    /**
     * 商品をカートに追加する
     * @param {object} item 追加する商品オブジェクト
     */
    addItem(item) {
        this.#itemList.push(item);
        this.saveToSessionStorage(); // カートの状態をセッションストレージに保存
    }

    /**
     * インデックスを指定して商品をカートから削除する
     * @param {number} index 削除する商品のインデックス
     */
    removeItem(index) {
        this.#itemList.splice(index, 1);
        this.saveToSessionStorage(); // カートの状態をセッションストレージに保存
    }

    /**
     * カート内の商品を全て削除する
     */
    clearCart() {
        this.#itemList = [];
        this.saveToSessionStorage(); // カートの状態をセッションストレージに保存
    }

    /**
     * カート内の商品の合計金額を計算する
     * @returns {number} 合計金額
     */
    getTotal() {
        return this.#itemList.reduce((total, item) => total + item.price, 0);
    }

    /**
     * カートの商品リストをセッションストレージに保存する
     */
    saveToSessionStorage() {
        sessionStorage.setItem('cartItems', JSON.stringify(this.#itemList));
    }

    /**
     * セッションストレージからカートの商品リストを読み込み、Cartオブジェクトとして返す
     * @returns {Cart} セッションストレージから読み込んだCartオブジェクト
     */
    static loadFromSessionStorage() {
        const storedItems = sessionStorage.getItem('cartItems');
        return new Cart(storedItems ? JSON.parse(storedItems) : []);
    }

    /**
     * カートの表示を更新する静的メソッド
     * カート内の商品数と合計金額を更新して表示する
     */
    static updateCartDisplay() {
        const cartCountElement = document.getElementById('cart-count');
        if (cartCountElement) {
            const items = Cart.getItems();
            cartCountElement.textContent = items.length; // カート内の商品数を表示
        }

        const cartList = document.getElementById('cart-list');
        if (cartList) {
            Cart.displayCart(cartList); // カート内の商品をHTMLとして表示
        }

        const totalPriceElement = document.getElementById('total-price');
        if (totalPriceElement) {
            totalPriceElement.textContent = `${Cart.getTotal()}円`; // カート内の合計金額を表示
        }
    }

    /**
     * カート内の商品をHTMLとして表示する
     * @param {HTMLElement} container 商品リストを表示するHTML要素
     */
    static displayCart(container) {
        const items = Cart.getItems(); // カート内の商品を取得
        container.innerHTML = items.map((item, index) => `
        <li class="list-group-item d-flex align-items-center">
            <img src="../img/${item.img}" alt="${item.name}" style="width: 50px; height: 50px; object-fit: cover;">
            <span class="ms-3 flex-grow-1">${item.name}</span>
            <span class="me-3">${item.price}円</span>
            <button class="btn btn-danger btn-sm btn-delete" data-index="${index}">削除</button>
        </li>
         `).join(''); // 商品リストをHTMLとして生成し、コンテナに表示
    }
}
