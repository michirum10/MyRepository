// 配列(実用)

// 出力準備
let output = document.getElementById('output')

// 配列の生成
let member = ['木内', '有田', '林', '藤井', '前村', '三田', '森', '森藤', '山崎']


// 一人ずつ出力する。(for文)
// 出力準備
output.innerHTML += member + '<br>'
// 縦に並べたいときは一人づつ出力することを繰り返す
for (let index = 0; index < member.length; index++) {
    output.innerHTML += member[index] + '<br>';
}


// 一人ずつ出力する。(for-each文)
// こっちの方がよく使う
// 以下基本形

// 出力準備
output.innerHTML += '<br>'
// 無名関数
// 配列の要素(member)一つずつがエレメントに入る
member.forEach(function (element) {
    // outputに代入して出力
    output.innerHTML += element + '<br>'
});


// 従業員生成
let emp01 = {
    name: '従業員A',
    age: 33,
    gender: 0
}
let emp02 = {
    name: '従業員B',
    age: 42,
    gender: 1
}
let emp03 = {
    name: '従業員C',
    age: 25,
    gender: 0
}
let emp04 = {
    name: '従業員D',
    age: 33,
    gender: 3
}
let emp05 = {
    name: '従業員E',
    age: 31,
    gender: 1
}

// 従業員配列の生成(for-eachループ)
// 5人の従業員のデータが配列としてemployeesに入る
let employees = [emp01, emp02, emp03, emp04, emp05]
// employeesの中身を１つ取り出すので単数形(employee)
employees.forEach(function (employee) {

    // <dl><dt><dd>をhtmlに書いてからコピペすると綺麗に書ける
    // テンプレートリテラル``で囲む
    // outHtmlを宣言して初期化
    let outHtml = `
    <dl>
        <dt>名前</dt>
        <dd>${employee.name}</dd>
        <dt>年齢</dt>
        <dd>${employee.age}</dd>
        <dt>性別</dt>
        <dd>${employee.gender == 0 ? '男' :
            employee.gender == 1 ? '女' : '!?'}</dd>
    </dl>
`
// outputに代入して出力
    output.innerHTML += outHtml
})

// 三項演算子
// エクセルのif関数みたいな感じ
// ：で区切る
// 条件　employee.gender　
// 男の時　0 ? '男'　　
// 条件　employee.gender
// 女の時　1 ? '女' 
// どちらでもない時　'!?'

