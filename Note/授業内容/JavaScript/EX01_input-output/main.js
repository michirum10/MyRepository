// 値が変化する、取得する要素を予め変数に格納しておく
let inName = document.getElementById('inName')
let outName = document.getElementById('outName')
let msg = document.getElementById('msg')

function introduction() {
    // 名前の情報を表示
    // inputタグの値の取得は.valueを利用する
    outName.innerHTML = inName.value
    // メッセージの生成
    msg.innerHTML = '私の名前は' + inName.value + 'です。'
}
