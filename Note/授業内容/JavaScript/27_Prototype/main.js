// プロトタイプ
// 後から機能を追加できる

let output = document.getElementById('output')

const robot = {
    hp:100,
    en:100
}
console.log(robot)

robot.move = () => {
    output.innerHTML += '移動しました。<br>'
    this.en -=10
}

console.log(robot)
robot.move()
console.log(robot)

const flight = {
    // en:100,
    fly(){
        output.innerHTML += '空を飛びました。<br>'
        this.en -= 10
    }
}

// console.log(flight)
// flight.fly()
// console.log(flight)

Object.assign(robot,flight)


console.log(robot)
robot.fly()
console.log(robot)
