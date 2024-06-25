// p5.js
// お絵かき

// 出力先の要素を習得
let output = document.getElementById('output')

window.setup = function(){
    let canvasElement = createCanvas(500, 500)
    canvasElement.parent(output)
    background('#32cd32')
    // 1秒間に60回実行される
    frameRate(60)
}

// 外に書く
let size = 0
let f = false
window.draw = function(){
    // 塗りつぶし
    fill('#ffff00')
    // フチなし
    strokeWeight(0)
    // だ円
    ellipse(250, 250, 300, 300)
    
    // 太さ50
    strokeWeight(50)
    // 白
    stroke('#ffffff')
    // 直線
    line(0,0,500,500)

    // 塗りつぶし
    fill('#0000ff')
    // 増える
    // size++

    // 増えたり 
    if(f){
        size++
    }else{
        size--
    }
    if(size == 500){
        f = false
    }else if(size == -500){
        f = true
    }

    // 円
    circle(250,250,size)

}

