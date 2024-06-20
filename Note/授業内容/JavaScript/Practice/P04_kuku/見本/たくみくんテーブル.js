let table_99 = document.getElementByid('table_99')
// output4にtable/tr(行)th(見出し)を代入する
output4 = '<table><tr><th>';
    // tr = 行の追加(iが1~9の間)
for (let i = 1; i <= 9; i++) {
    output4 += ('<th>' + i + '</th>');
}
    // tr(行)のスタート→i=1から
    // th(左の見出し(th)の追加 = i)
for (let i = 1; i <= 9; i++) {
    output4 += '<tr> <th>' + i + '</th>';
    // th(テーブルデータ要素(td)の追加 = i)
    // j(かけるものが1~9の間、i*jを追加していく(横方向に))
    for (let j = 1; j <= 9; j++) {
    output4 += ('<td>' + (i * j) + '</td>');
    }
    // jのfor文終了時[i=9までいったら]tr(i行)の終了を宣言→改行される
    // 次はiに1(tr=行)を足して繰り返し処理をする[2行目]
    output4 += '</tr>';
}
// すべての99の処理終了時にtableの終了
output4 += '</table>';
// table_99のHTMLに99の表を表示させる
table_99.innerHTML = output4;

