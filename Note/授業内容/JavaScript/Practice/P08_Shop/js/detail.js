import Cart from './Cart.js';

// 画面が読み込まれたら表示
window.onload = function () {
    // 出力準備：HTMLの出力先要素を取得
    let output = document.getElementById('output');

    // GETパラメータの取得
    // 現在のURLを取得
    let url = new URL(window.location.href);
    // URLの検索パラメータを取得
    let params = url.searchParams;
    // 検索パラメータから'index'の値を取得
    let index = params.get('index');

    // sessionStorageから選択された商品のインデックスを取得
    let itemIndex = JSON.parse(sessionStorage.getItem('itemIndex'));
    console.log(itemIndex);

    // sessionStorageから事前に保存されたJSONデータを取得
    let storedData = sessionStorage.getItem('products');

    if (storedData) {
        // sessionStorageにデータがある場合
        let data = JSON.parse(storedData);
        // 動作確認用のログ出力
        console.log(data);
        // インデックスが有効範囲内であるか確認し、詳細表示関数を呼び出す
        if (index !== null && index >= 0 && index < data.items.length) {
            itemDetails(data.items[index]);
        } else {
            output.innerHTML = '<p>商品情報が見つかりませんでした。</p>';
        }
    } else {
        // sessionStorageにデータがない場合、データをfetchで取得
        fetch('../data/data.json')
            .then(response => response.json())
            .then(data => {
                // データをsessionStorageに保存
                sessionStorage.setItem('products', JSON.stringify(data));
                console.log(data);
                // インデックスが有効範囲内であるか確認し、詳細表示関数を呼び出す
                if (index !== null && index >= 0 && index < data.items.length) {
                    itemDetails(data.items[index]);
                } else {
                    output.innerHTML = '<p>商品情報が見つかりませんでした。</p>';
                }
            })
            .catch(error => console.error('Error fetching the JSON data:', error));
    }

    // 商品詳細を表示する関数
    function itemDetails(item) {
        // 既存の内容をクリア
        output.innerHTML = '';

        // bootstrapカードの生成
        let card = document.createElement('div');
        card.classList.add('card', 'mb-3', 'item');
        card.style.width = '18rem';

        // カード画像の生成
        let cardImg = document.createElement('img');
        cardImg.src = `../img/${item.img}`;
        cardImg.classList.add('card-img-top');
        card.appendChild(cardImg);

        // カードボディの生成
        let cardBody = document.createElement('div');
        cardBody.classList.add('card-body');

        // 商品名の生成
        let cardTitle = document.createElement('h5');
        cardTitle.classList.add('card-title');
        cardTitle.textContent = item.name;
        cardBody.appendChild(cardTitle);

        // 商品価格の生成
        let cardText = document.createElement('p');
        cardText.classList.add('card-text');
        cardText.textContent = `価格: ${item.price}円`;
        cardBody.appendChild(cardText);

        // 商品説明の生成
        let cardDetail = document.createElement('p');
        cardDetail.textContent = item.detail;
        cardBody.appendChild(cardDetail);

        // 購入ボタンの生成
        let buyButton = document.createElement('button');
        buyButton.classList.add('btn', 'btn-primary');
        buyButton.textContent = 'カートに追加';
        // 購入ボタンのクリックイベント
        buyButton.onclick = function () {
            // カートのインスタンスを作成
            const cart = new Cart();
            // 商品をカートに追加
            cart.addItem(item);
            alert(`${item.name}をカートに追加しました`);
            // カートの内容をsessionStorageに保存
            sessionStorage.setItem('cart', JSON.stringify(cart.itemList));
        };

        // カードボディに購入ボタンを追加
        cardBody.appendChild(buyButton);

        // カードにボディを追加
        card.appendChild(cardBody);

        // 出力要素にカードを追加
        output.appendChild(card);
    }
}
