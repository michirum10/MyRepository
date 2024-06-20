// 遅延実行

// 出力先の要素を習得
let output = document.getElementById('output')

// setTimeout(関数,時間)
// 『''』か『""』は統一する
function greeting() {
    output.innerHTML += 'こんにちは！' + '<br>'
}
// setTimeout(実行する関数,待ち時間(単位ミリ秒))
// 3秒後になったら表示される(1回だけ)
setTimeout(greeting, 3000)


// setInterval(関数,時間)
// 現在時刻を表示
function sayTime() {
    output.innerHTML += new Date()
}
// 1秒毎に実行
let sayTimeID = setInterval(sayTime, 1000)
// stopSayTime関数をつくて10秒後に止める
function stopSayTime() {
    clearInterval(sayTimeID)
}
setTimeout(stopSayTime, 10000)

