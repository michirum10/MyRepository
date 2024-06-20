let num1 = document.getElementById("num1")

const ASAN = 1
const BSAN = 2
const RESET = -1
let asanm = ''
let bsanm = ''
let resetm = ''


// let msg = `${counter}`  
// output.textContent = msg
function btn(mode) {
    let anum1 = num1.value
    let now = new Date();
    now = now.toLocaleString()
    switch (mode) {
        case ASAN:
            asanm = anum1
            asanm = `${asanm}<br><hr>`
            break;
        case BSAN:
            bsanm = anum1
            bsanm = `${bsanm}<br><hr>`
            break;
        case RESET:
            resetm = ''
            break;

        default:
            break;
    }

    if(mode == 1 && anum1 != 0){
        let msg = `${asanm}`  
        output.innerHTML += `<span class="asan01">${now}：Aさん<br>${msg}</span>`
        num1.value = ''
    }else if(mode == 2 && anum1 != 0){
        let msg = `${bsanm}`  
        output.innerHTML += `<span class="bsan01">${now}：Bさん<br>${msg}</span>`
        num1.value = ''
    }else if(mode == -1){
        let msg = `${resetm}`
        output.innerHTML = ''
    }else{
        alert('入力が空です')
    }



    // if(mode == 1 && anum1 != 0){
    //     let msg = `${asanm}`  
    //     output.innerHTML += `<span class="asan01">${now}：Aさん<br>${msg}</span>`
    //     num1.value = ''
    // }else if(mode == 2 && anum1 != 0){
    //     let msg = `${bsanm}`  
    //     output.innerHTML += `<span class="bsan01">${now}：Bさん<br>${msg}</span>`
    //     num1.value = ''
    // }else if(mode == -1){
    //     let msg = `${resetm}`
    //     output.innerHTML = ''
    // }else{
    //     alert('入力が空です')
    // }

}




