
// 画面が読み込まれたら表示
window.onload = function () {
    // 出力準備
    let output = document.getElementById('output');

    function itemList() {
        // jsonデータを取得
        fetch('../data/data.json')
            .then(response => response.json())
            .then(json => {

                // console.log(#itemlist)
                console.log(json);

                // ID=itemsを取得
                let itemDiv = '';
                // json.itemsのそれぞれのitemを取得してループ   
                // json.items.forEach(function (item) {
                    // divタグの生成をしたい

                    // bootstrapカードの生成
                    let card = document.createElement('div');
                    // クラスを指定
                    card.classList.add('card', 'mb-3', 'item');
                    card.style.width = '18rem';

                    // カード画像の生成
                    let cardImg = document.createElement('img');
                    // 相対パスで画像を取得
                    cardImg.src = `../img/${item[index].img}`
                    cardImg.classList.add('card-img-top');
                    card.appendChild(cardImg);

                    // カードボディ(大枠)の生成
                    let cardBody = document.createElement('div');
                    cardBody.classList.add('card-body');

                    // 商品名
                    let cardTitle = document.createElement('h5');
                    cardTitle.classList.add('card-title');
                    cardTitle.textContent = item[index].name;
                    cardBody.appendChild(cardTitle);

                    // 商品価格
                    let cardText = document.createElement('p');
                    cardText.classList.add('card-text');
                    cardText.textContent = `価格: ${item[index].price}円`;
                    cardBody.appendChild(cardText);

                    // 購入ボタン追加
                    let buyButton = document.createElement('button');
                    buyButton.classList.add('btn', 'btn-primary');
                    buyButton.textContent = 'カートに追加';
                    buyButton.onclick = function () {
                        cart.addItem(item);
                        alert(`${item.name}をカートに追加しました`);
                        // カートに追加したら購入確認画面に遷移
                        // window.location.href = 
                    };

                    // カードボディ(親)に購入ボタンを追加
                    cardBody.appendChild(buyButton);

                    // カード(親)にボディを追加
                    card.appendChild(cardBody);

                    // 出力要素(親)にカードを追加
                    output.appendChild(card);

                    // カード押したら詳細画面に遷移
                    card.addEventListener('click', function() {
                        window.location.href = `detail.html?id=${item.detail}`;
                    });
                    
                // });
            });
    }

    itemList()
}