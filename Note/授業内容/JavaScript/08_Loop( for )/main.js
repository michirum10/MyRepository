// 反復構文

// 出力準備
let output = document.getElementById('output')


// よく使うのはforeach for単体はあまり使わない

// for文
// 無限ループに陥りやすい
// １、let index = 0　初期化式。indexの中に0を入れておく。初回のみ
// ２、index < 10　条件式。indexが10より小さい時にブロック{}が実行される
// ４、index++　加算式(増分式)。ブロック{}実行後に実行。後で条件式で判定する
// ３、{output.innerHTML += index}　{}の中を繰り返す
// 順番は1,2,3,4,2,3,4,...
for (let index = 0; index < 10; index++) {
    output.innerHTML += index
}

// output上書きして改行
output.innerHTML += '<br>'

// while文 ループの最初に条件式を判定(条件によっては一度もループしない)
// 外に書く　let index = 0
// 中に書くと毎回初期化される
let index = 0
// while (index < 10)の()の中に条件式を書く
// {}の中に書いた処理が実行される
while (index < 10) {
    output.innerHTML += index
    index++
}

// output上書きして改行
output.innerHTML += '<br>'

// do-while文 条件に関わらず一回はループを実行し、その後条件式を評価
// 一回は実行doする
// 条件式：条件式の判定がtrueだったとき、ブロックが実行される

// index上書き
index = 0
// 必ず 1 回は繰り返し処理が実行される
do {
    output.innerHTML += index
    index++
} while (index < 10)


// output上書きして改行
output.innerHTML += '<br>'

// break文　ブロックの処理を強制中断する。
// ブロックを抜けるイメージ
// runnerAは0メートル
let runnerA = 0
let runnerB = 100

while (runnerA < runnerB) {
    // runnerAは+3ずつ進む
    runnerA += 3
    // runnerBは+2ずつ進む
    runnerB += 2
    // runnerA:Bを表示
    output.innerHTML += `A${runnerA}:B${runnerB}<br>`

    //ゴール
    // もしrunnerBが200mに達すると
    if (runnerB >= 200) {
        // ゴール！と表示される
        output.innerHTML += 'ゴール！<br>'
        // 最後にブレイクで中断
        break
    }
}

// continue文　現在のブロックの処理を中断し、再度反復処理の判定を行う。
// スキップするイメージ
// 上に戻る continue→for

for (let index = 0; index <= 10; index++) {
    // もしindexが2で割れない時（奇数の時）処理をスキップ
    if (index % 2 == 1) {
        continue
    }
    // 出力
    output.innerHTML += index + ' '
}


// 無限ループになってPCに負荷がかかる
// ブラウザのコンソールログで確認
// while (true) {
//     index++
//     console.log(index)
// }
