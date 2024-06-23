import Cart from './Cart.js';

window.onload = function () {
    const output = document.getElementById('output');

    // JSONデータを取得
    fetch('../data/data.json')
        .then(response => response.json())
        .then(json => {
            displayItems(json.items);
        });

    function displayItems(items) {
        output.innerHTML = ''; // 初期化

        items.forEach((item, index) => {
            // Bootstrapカードの生成
            let card = document.createElement('div');
            card.classList.add('card', 'mb-3', 'item');
            card.style.width = '18rem';
            card.style.cursor = 'pointer'; // カーソルをポインターに変更;

            // カード全体のクリックイベント
            card.addEventListener('click', function () {
                // 詳細画面に遷移
                goToDetailPage(item);
            });

            // カード画像の生成
            let cardImg = document.createElement('img');
            cardImg.src = `../img/${item.img}`;
            cardImg.classList.add('card-img-top');
            card.appendChild(cardImg);

            // カードボディの生成
            let cardBody = document.createElement('div');
            cardBody.classList.add('card-body');

            // 商品名
            let cardTitle = document.createElement('h5');
            cardTitle.classList.add('card-title');
            cardTitle.textContent = item.name;
            cardBody.appendChild(cardTitle);

            // 商品価格
            let cardText = document.createElement('p');
            cardText.classList.add('card-text');
            cardText.textContent = `価格: ${item.price}円`;
            cardBody.appendChild(cardText);

            // 詳細ボタンの生成
            const detailBtn = document.createElement('button');
            detailBtn.classList.add('btn', 'btn-primary');
            detailBtn.textContent = '詳細';
            // カードに詳細ボタンを追加
            cardBody.appendChild(detailBtn);
            
            // カードにボディを追加
            card.appendChild(cardBody);

            // 出力要素にカードを追加
            output.appendChild(card);
        });
    }

    // 詳細ページに遷移する関数
    function goToDetailPage(item) {
        sessionStorage.setItem('selectedItem', JSON.stringify(item));
        window.location.href = '../html/detail.html';
    }

    // 購入確認ページへ
    document.getElementById('confirm-button').addEventListener('click', () => {
        window.location.href = 'confirm.html';
    });

    // カート表示の更新
    Cart.updateCartDisplay();
}
