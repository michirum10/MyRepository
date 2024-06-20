// 組み込みオブジェクト

// 出力先の要素を習得
let output = document.getElementById('output')

// Mathオブジェクト
// 計算を行うオブジェクト

// 関数randは「乱数（ランダム）」を表す
function rand(min, max) {
    // floorは小数点以下切り捨てなので、100も表示するためには+１する
    max++
    // floorは小数点以下切り捨て
    return Math.floor(Math.random() * (max - min) + min)
}

// (min0~max100)のランダムな数値を返す
output.innerHTML += rand(0, 100) + '<br>'
// コンピュータは完全な乱数はできない
// 乱数テーブルを使う

// Dateクラス
output.innerHTML += '日付型'

// 現在時刻の取得
// クラス：設計図(属性（プロパティ）と操作（メソッド）を定義したもの)
// インスタンス：設計図をもとにして実際に作った物(クラスをnewしたもの)
// newする:クラスからインスタンスを作る行為
// オブジェクト：モノ（クラスとかインスタンスとかのこと)
// クラスをオブジェクト化(インスタンス化)したモノの事をオブジェクト(インスタンス)と呼ぶ

// let 変数名 = new クラス名();
// todayはオブジェクト

// 現在時刻の取得
let today = new Date()
output.innerHTML += today + '<br>'
// 日本でよく使われる形式に変換
output.innerHTML += today.toLocaleString('ja-JP') + '<br>'

// 日付を指定した日時を取得
let day1 = new Date('2024/06/14')
output.innerHTML += day1.toLocaleString('ja-JP') + '<br>' + '<br>'

// 日付と時刻を指定した日時を取得
// タイムゾーンを勝手に指定してくれる
let day2 = new Date('2024/06/14 18:30')
output.innerHTML += day2.toLocaleString('ja-JP') + '<br>'

// 日付を指定した日を取得
// 月と曜日は0から始まる。配列。教科書入門編p161
// 
let day3 = new Date(2024, 5, 14)
output.innerHTML += day3.toLocaleString('ja-JP') + '<br>'

// 日付を指定した日時を取得
let day4 = new Date(2024, 5, 14, 18, 30)
output.innerHTML += day4.toLocaleString('ja-JP') + '<br>'

// 日付を指定した日時を取得
// unixtimeツールで日時を変換
let day5 = new Date(1718290800.000)
output.innerHTML += day5.toLocaleString('ja-JP') + '<br>'

// JSの時間がいつから始まってるかを知るにはnew Date(0)
let day6 = new Date(0)
output.innerHTML += day6.toLocaleString('ja-JP') + '<br>'

// JavaScriptには日付フォーマットを行う標準クラスは無い
// なので、自作する。

function dateFormat(inputDate) {
    let yyyy = inputDate.getFullYear().toString().padStart(4, '0')
    let MM = (inputDate.getMonth() + 1).toString().padStart(2, '0')
    let dd = inputDate.getDate().toString().padStart(2, '0')
    let hh = inputDate.getHours().toString().padStart(2, '0')
    let mm = inputDate.getMinutes().toString().padStart(2, '0')
    let ss = inputDate.getSeconds().toString().padStart(2, '0')

    // .padStart(4,'0') は4桁で0埋めする処理
    // 表示したい文字は配列で準備
    const elements = ['日', '月', '火', '水', '木', '金', '土']
    let EE = elements[inputDate.getDay()]

    return `${yyyy}/${MM}/${dd} (${EE}) ${hh}:${mm}:${ss}<br>`
}
output.innerHTML += dateFormat(day1)

// 時間の差を計算
output.innerHTML += day2 - day1 + '<br>'
let day7 = new Date(day2 - day1)
// Math.floor切り捨て
// ミリ秒(1/1000)表示なので1000で割って秒に直す
// 分60で割る
// 時間60で割る
// あまりを出す
let hh = Math.floor(day7 / 1000 / 60 / 60).toString().padStart(2,'0')
let mm = Math.floor(day7 / 1000 / 60 % 60).toString().padStart(2,'0')
let ss = Math.floor(day7 / 1000 % 60 ).toString().padStart(2,'0')
output.innerHTML += `${hh}:${mm}:${ss}`


// getFullYear:は4桁の西暦
// getMonth() + 1:月は0から始まるので+1する
// toString:文字に変換
// padStart:paddingの略。埋める。左からスタート。第一引数は何個埋めるか、第二引数は何で埋めるか
// .padStart(4,'0') は4桁で0埋めする処理

// JSはローカルなので、このPCの時刻を取得する
// デバイスの時間を変えると反映される
// のでJSで日時を表示することは少ない
// 別で扱う