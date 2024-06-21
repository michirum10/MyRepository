// Cart.js

export default class Cart {
    // 商品リスト配列
    #itemList = [];

    // コンストラクタ(メソッド)の宣言
    constructor(itemList = []) {
        this.loadCart(); // コンストラクタでカートをロード
    }

    // メソッド:商品一覧取得
    get itemList() {
        return this.#itemList;
    }

    // メソッド:商品追加
    addItem(item) {
        this.#itemList.push(item);
        this.saveCart(); // 商品追加後にカートを保存
    }

    // メソッド:商品購入
    purchase() {
        this.#itemList = [];
        this.saveCart(); // 購入後にカートをクリアして保存
    }

    //  メソッド: カートをsessionStorageに保存
    saveCart() {
        sessionStorage.setItem('cart', JSON.stringify(this.#itemList));
    }

    // メソッド: カートをsessionStorageからロード
    loadCart() {
        const cartData = sessionStorage.getItem('cart');
        if (cartData) {
            this.#itemList = JSON.parse(cartData);
        }
    }
}
