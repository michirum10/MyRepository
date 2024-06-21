// detail.js 商品詳細
// 一つのクリックした商品の情報を表示する
// （商品名と値段、画像、説明を大きく表示する。）
// カートに入れるボタン⇛カートにデータを追加

// カート機能のモジュールをインポート
import Cart from './Cart.js';

// カートのインスタンスを作成（グローバルで使用）
let cart;

// ページが完全に読み込まれた後に実行される関数
window.onload = function () {

    // カートの初期化
    resetCart();

    // カート表示の更新
    updateCartDisplay();

    // 出力準備
    const output = document.getElementById('output');

    // 現在のURLを取得
    const url = new URL(window.location.href);
    // 現在のURLからGETパラメータ（index）を取得
    const index = url.searchParams.get('index');
    //  デバッグ用: indexの値をコンソールに出力
    console.log('Received index:', index);

    // sessionStorageから保存された商品データを取得
    let storedData = sessionStorage.getItem('products');

    // sessionStorageにデータがあるかどうかを確認
    if (storedData) {
        // sessionStorageにデータがある場合、そのデータを解析して詳細表示関数を呼び出す
        const data = JSON.parse(storedData);
        // デバッグ用: 取得したデータをコンソールに出力
        console.log('Stored data:', data);
        displayItemDetails(data, index, output);
    } else {
        // sessionStorageにデータがない場合、fetchを使用してデータを取得し、保存してから詳細表示関数を呼び出す
        fetch('../data/data.json')
            .then(response => response.json()) // 取得したデータをJSONに変換
            .then(data => {
                sessionStorage.setItem('products', JSON.stringify(data)); // 取得したデータをsessionStorageに保存
                console.log('Fetched data:', data);
                displayItemDetails(data, index, output); // 詳細表示関数を呼び出す
            })
            .catch(error => console.error('Error fetching the JSON data:', error)); // エラーが発生した場合にコンソールに出力
    }


    // 商品詳細を表示する関数
    function displayItemDetails(data, index, output) {
        const itemIndex = parseInt(index); // indexパラメータを整数に変換

        // インデックスが有効範囲内であるか確認
        // ここを修正: itemIndex が null でないことと、有効な範囲内であることを確認
        if (itemIndex != null && itemIndex >= 0 && itemIndex < data.items.length) {
            const item = data.items[itemIndex];
            itemDetails(item, output);
        } else {
            output.innerHTML = '<p>商品情報が見つかりませんでした。</p>';
        }
    }

    // 商品の詳細情報を取得する関数
    function itemDetails(item, output) {
        output.innerHTML = ''; // 初期化

        // 商品情報を表示するためのBootstrapカードの生成
        const card = document.createElement('div');
        card.classList.add('card', 'mb-3', 'item'); // クラスを指定
        card.style.width = '18rem'; // カードの幅を指定

        // カードボディの生成
        const cardBody = document.createElement('div');
        cardBody.classList.add('card-body'); // クラスを指定

        // カード画像の生成
        const cardImg = document.createElement('img');
        cardImg.src = `../img/${item.img}`; // 画像パスを設定
        cardImg.alt = `${item.name}の画像`;
        cardImg.classList.add('card-img-top'); // クラスを指定
        card.appendChild(cardImg); // カードに画像を追加

        // 商品名の生成
        const cardTitle = document.createElement('h5');
        cardTitle.classList.add('card-title'); // クラスを指定
        cardTitle.textContent = item.name; // 商品名を設定
        cardBody.appendChild(cardTitle); // カードボディに商品名を追加

        // 商品価格の生成
        const cardText = document.createElement('p');
        cardText.classList.add('card-text'); // クラスを指定
        cardText.textContent = `価格: ${item.price}円`; // 商品価格を設定
        cardBody.appendChild(cardText); // カードボディに価格を追加

        // 商品説明の生成
        const cardDetail = document.createElement('p');
        cardDetail.textContent = item.detail; // 商品説明を設定
        cardBody.appendChild(cardDetail); // カードボディに商品説明を追加

        // 購入ボタンの生成
        const buyButton = document.createElement('button');
        buyButton.classList.add('btn', 'btn-primary'); // クラスを指定
        buyButton.textContent = 'カートに追加'; // ボタンのテキストを設定
        // addEventListenerを使用してクリックイベントを設定
        buyButton.addEventListener('click', function () {
            addToCart(item);
        });

        // カードボディに購入ボタンを追加
        cardBody.appendChild(buyButton);

        // カードにボディを追加
        card.appendChild(cardBody);

        // 出力要素にカードを追加
        output.appendChild(card);
    }
    // カートの初期化
    function resetCart() {
        // sessionStorageからカートデータを取得
        const cartData = sessionStorage.getItem('cart');
        if (cartData) {
            cart = new Cart(JSON.parse(cartData));
        } else {
            cart = new Cart();
        }
    }

    // カートに商品を追加する関数
    function addToCart(item) {
        cart.addItem(item);
        alert(`${item.name}をカートに追加しました`);
        // カートの内容をsessionStorageに保存
        sessionStorage.setItem('cart', JSON.stringify(cart.itemList));
        // カートの内容を表示（オプション）
        console.log('カートの中身:', cart.itemList);
        // カートに商品を追加した後、表示を更新
        updateCartDisplay();
        // カートに追加したら購入確認画面に遷移
        // window.location.href = 'confirm.html';
    }

    function updateCartDisplay() {
        const cartCountElement = document.getElementById('cart-count');
        if (cartCountElement) {
            cartCountElement.textContent = cart.itemList.length;
        }
    }
};
