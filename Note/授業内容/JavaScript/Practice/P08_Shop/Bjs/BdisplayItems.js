// displayItems.js

// カート機能のモジュールをインポート
import Cart from './Bcart.js';


/**
 * 商品情報からBootstrapのカード要素を生成する関数。
 * @param {object} item - 商品情報を含むオブジェクト。
 * @param {boolean} withDetailButton - 詳細ボタンを生成するかどうかのフラグ。デフォルトはfalse。
 * @param {boolean} withCartButton - カート追加ボタンを生成するかどうかのフラグ。デフォルトはfalse。
 * @returns {HTMLElement} 生成されたカード要素。
 */

// index.js,detail.js共通カード生成関数(createCard)
function createCard(item, withDetailButton = false, withCartButton = false) {
    // Bootstrapカードの生成
    const card = document.createElement('div');
    card.classList.add('card', 'mb-3', 'item'); // カードにBootstrapのクラスを追加
    card.style.width = '18rem'; // カードの幅を設定

    // カードボディの生成
    const cardBody = document.createElement('div');
    cardBody.classList.add('card-body'); // カードボディにBootstrapのクラスを追加

    // カード画像の生成
    const cardImg = document.createElement('img');
    cardImg.src = `../img/${item.img}`; // 画像のソースを設定
    cardImg.classList.add('card-img-top'); // 画像にBootstrapのクラスを追加
    card.appendChild(cardImg); // カードに画像を追加

    // 商品名
    const cardTitle = document.createElement('h5');
    cardTitle.classList.add('card-title'); // 商品名にBootstrapのクラスを追加
    cardTitle.textContent = item.name; // 商品名を設定
    cardBody.appendChild(cardTitle); // カードボディに商品名を追加

    // 商品価格
    const cardText = document.createElement('p');
    cardText.classList.add('card-text'); // 商品価格にBootstrapのクラスを追加
    cardText.textContent = `価格: ${item.price}円`; // 商品価格を設定
    cardBody.appendChild(cardText); // カードボディに商品価格を追加

    // 商品説明（詳細ページのみ）
    if (item.detail && withDetailButton) {
        const cardDetail = document.createElement('p');
        cardDetail.textContent = item.detail; // 商品説明を設定
        cardBody.appendChild(cardDetail); // カードボディに商品説明を追加
    }

    // 詳細ボタン
    if (withDetailButton) {
        const detailBtn = document.createElement('button');
        detailBtn.classList.add('btn', 'btn-primary'); // 詳細ボタンにBootstrapのクラスを追加
        detailBtn.textContent = '詳細'; // ボタンのテキストを設定
        detailBtn.addEventListener('click', () => {
            sessionStorage.setItem('selectedItem', JSON.stringify(item)); // 商品情報をセッションストレージに保存
            window.open('detail.html', '_blank', 'width=1200, height=1000'); // 新しいwindowで詳細ページを開く
        });
        cardBody.appendChild(detailBtn); // カードボディに詳細ボタンを追加
    }

    // カートに追加ボタン（詳細ページのみ）
    if (withCartButton) {
        const buyButton = document.createElement('button');
        buyButton.classList.add('btn', 'btn-primary'); // カート追加ボタンにBootstrapのクラスを追加
        buyButton.textContent = 'カートに追加'; // ボタンのテキストを設定

        buyButton.addEventListener('click', () => {
            Cart.addItem(item); // カートに商品を追加
            Cart.updateCartDisplay(); // カート表示を更新
            alert(`${item.name}をカートに追加しました`); // 追加完了のアラートを表示

            // 元のウィンドウのカートを更新
        if (window.opener && !window.opener.closed) {
            window.opener.Cart.updateCartDisplay();
            // window.opener.location.reload(); // 元のウィンドウをリロードしてカートの表示を更新
        }
    
        window.close(); // 現在のポップアップウィンドウを閉じる
        });
        cardBody.appendChild(buyButton);
    }

    card.appendChild(cardBody); // カードにボディを追加

    return card; // 生成したカードを返す
}

// 商品一覧を表示(index.jsで使う)
export function displayItems(items, output) {
    output.innerHTML = ''; // 初期化

    items.forEach(item => {
        // Bootstrapグリッド
        const col = document.createElement('div');
        col.classList.add('col');

        const card = createCard(item, true, false); // 詳細ボタン付きのカードを生成
        card.style.cursor = 'pointer'; // カーソルをポインターに変更
        card.addEventListener('click', () => {
            sessionStorage.setItem('selectedItem', JSON.stringify(item)); // 商品情報をセッションストレージに保存
            window.open('detail.html', '_blank', 'width=1200, height=1000'); // 新しいwindowで詳細ページを開く
        });
        col.appendChild(card);
        output.appendChild(col); // 出力要素にカードを追加
    });
}

// 商品の詳細情報を表示(detail.jsで使う)
export function itemDetails(item, output) {
    output.innerHTML = ''; // 初期化
    const card = createCard(item, false, true); // カート追加ボタン付きのカードを生成
    output.appendChild(card); // 出力要素にカードを追加
}


// 購入確認ボタンを生成する関数
// export function createConfirmButton() {
//     const confirmButton = document.createElement('button');
//     confirmButton.classList.add('btn', 'btn-primary', 'confirm-button');
//     // confirmButton.className = 'btn btn-primary';
//     confirmButton.textContent = '購入確認';
//     confirmButton.addEventListener('click', () => {
//         // 新しいウィンドウで購入確認ページを開く
//         window.open('confirm.html', 'confirmWindow', 'width=600,height=400');
//     });
//     return confirmButton;
// }