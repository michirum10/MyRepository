let output1 = document.getElementById("output1")
let output2 = document.getElementById("output2")
let output3 = document.getElementById("output3")
let output4 = document.getElementById("output4")
let output5 = document.getElementById("output5")

for (let i = 1; i <= 9; i++) {
   for (let j = 1; j <= 9; j++) {
      output1.textContent += `${i*j} `
   }
}

for (let i = 1; i <= 9; i++) {
   for (let j = 1; j <= 9; j++) {
      output2.innerHTML += `${i}*${j}=${i*j}<br>`
   }
}

for (let i = 1; i <= 9; i++) {
   for (let j = 1; j <= 9; j++) {
      output3.innerHTML += `${i*j} `
   }
   output3.innerHTML += '<br>'
}

for (let i = 1; i <= 9; i++) {
   for (let j = 1; j <= 9; j++) {
      if(i*j>9){
         output4.innerHTML += `${i*j}&nbsp`
      }else{
         output4.innerHTML += `&nbsp&nbsp${i*j}&nbsp`
      }
   }
   output4.innerHTML += '<br>'
}

let html5 = ''
html5 += '<table>'
html5 += '<thead>'
html5 += '<tr>'
for (let i = 0; i <= 9; i++) {
   html5 += `<th>${i}</th>`
}
html5 += '</tr>'
html5 += '</thead>'
html5 += '<tbody>'
for (let i = 1; i <= 9; i++) {
   html5 += '<tr>'
   html5 += `<th>${i}</th>`
   for (let j = 1; j <= 9; j++) {
      html5 += '<td>'
      if(i*j>9){
         html5 += `${i*j}`
      }else{
         html5 += `${i*j}`
      }
      html5 += '</td>'
   }
   html5 += '</tr>'
}
html5 += '</tbody>'
html5 += '</table>'

output5.innerHTML = html5

