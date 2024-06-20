
// 関数
// プログラム(処理)の塊のこと
// function　関数のこと。関数は自分で名前をつける。
// 紐づける。関連付ける。
// HTMLで決めたclick1という関数に{}の中身を代入している
function click1() {
    // HTMLからp1を取得してHTMLp1にテキストを表示
    document.getElementById('p1').textContent = '実行ボタンが押されました。'
}
function click2() {
    document.getElementById('p2').textContent = '実行ボタンが押されました。'
}
// 文字を上書きしてリセットにみせる
function reset1() {
    document.getElementById('p1').textContent = '１つ目の内容'
}
function reset2() {
    document.getElementById('p2').textContent = '２つ目の内容'
}

// 両方リセット
// resetが押されたら実行される
function reset() {
    // 省略して書ける
    reset1()
    reset2()
}