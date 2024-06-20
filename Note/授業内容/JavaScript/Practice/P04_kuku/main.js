// 出力準備1
let output1 = document.getElementById('output1')

// 1から9までの間、1ずつ増やす。行(横)
for (let num1 = 1; num1 <= 9; num1++) {
    // 1から9までの間、1ずつ増やす。列(縦)
    for (let num2 = 1; num2 <= 9; num2++) {
        // &nbspは半角スペース（空白）タグ
        // 変数なので、`${}`で囲む
        output1.innerHTML += `${num1 * num2}&nbsp`
    }
}

// 出力準備2
output2 = document.getElementById('output2')
for (let num1 = 1; num1 <= 9; num1++) {
    for (let num2 = 1; num2 <= 9; num2++) {
        // 変数なので、`${}`で囲む
        // 式全体を``で囲む。各変数は${}で囲む
        // 最後に改行<br>すると見やすい
        output2.innerHTML += `${num1} X ${num1} = ${num1 * num2}<br>`
    }
}

// 出力準備3
output3 = document.getElementById('output3')
// 1から9までの間、1ずつ増やす。行
for (let num1 = 1; num1 <= 9; num1++) {
    // 1から9までの間、1ずつ増やす。列
    for (let num2 = 1; num2 <= 9; num2++) {
        // 変数なので、`${}`で囲む
        // &nbsp;はHTMLの半角スペース（空白）
        output3.innerHTML += `${num1 * num2}&nbsp`
    }
    // 新しい行を作成
    // 1~9までで改行する
    output3.innerHTML += '<br>'
}

// 出力準備4
output4 = document.getElementById('output4')
// テーブル関数使う
// 変数(table)の宣言
// 変数の名前は何でもいいので分かりやすい名前をつける
// 変数(table)に<table>タグを代入して初期化
let table = '<table>';
// <tr>横方向のヘッダーを追加
table += "<tr>";
// 空のヘッダーセルを準備
table += "<th></th>";
// ループ１
// 1行目に1~9のヘッダーを作る
for (let i = 1; i <= 9; i++) {
    table += `<th>${i}</th>`;
}
// 1から9まで1ずつ増やすループ２
// i は配列 index
for (let i = 1; i <= 9; i++) {
    // 外側のforループ２は行（横の列、<tr>）を生成
    // 変数(table)に行(横)を追加
    table += "<tr>";
    // 行の最初にヘッダーセル(テーブルヘッド)を追加
    table += `<th>${i}</th>`;
    // 内側のループ３はセル（縦の列、<td>テーブルデータ）を生成
    // j はiの次の番号。for分増えるとi,j,k,l...となる
    for (let j = 1; j <= 9; j++) {
        // 掛け算の結果を表示するセル（<td>）を繰り返し生成
        table += `<td>${i * j}</td>`;
    }
    // 1行分のセルが終わったら</tr>タグで行を閉じる
    table += "</tr>";
}
// 全ての行の生成が終わったら</table>タグでテーブルを閉じる
table += '</table>';
// output3に上記で作成したtableを代入して表示
output4.innerHTML = table;


// while文 繰り返す回数決まってない時に使う
output5 = document.getElementById('output5')
// 初期値外に書く
let num1 = 1
while (num1 <= 9) {
    // 内側のループ書く
    let num2 = 1
    while (num2 <= 9) {
        output5.innerHTML += `${num1 * num2}`
        num2++
    }
    num1++
}

// 九九の式を表示
// output5.innerHTML += `${num1} × ${num1} = ${num1 * num2}<br>`

// 九九表を表示
// 内側の{}にoutput5.innerHTML += `${num1 * num2}&nbsp;`
// 外側の{}に output5.innerHTML += '<br>'