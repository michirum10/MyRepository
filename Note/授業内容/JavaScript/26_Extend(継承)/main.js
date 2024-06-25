import Fan,{PortableFan} from "./Fan.js"

// 戻り値に対して処理をする事をチェイニングと呼ぶ
document.getElementById('new').addEventListener('click',() => new Fan())
document.getElementById('new2').addEventListener('click',() => new PortableFan())
