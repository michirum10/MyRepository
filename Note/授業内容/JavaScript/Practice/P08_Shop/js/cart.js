export default class art {
    // 商品リスト配列
    #itemList = [];

    // コンストラクタ(メソッド)の宣言
    constructor(itemList = []) {
        this.#itemList = itemList;
    }

    // メソッド:商品一覧取得
    get itemList() {
        return this.#itemList;
    }

    // メソッド:商品追加
    addItem(item) {
        this.#itemList.push(item);
    }

    // メソッド:商品購入
    purchase() {
        this.#itemList = [];
    }
}
