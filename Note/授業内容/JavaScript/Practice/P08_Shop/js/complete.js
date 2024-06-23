// js/complete.js

function redirectToIndex() {
    window.location.href = 'index.html';
}
// いい感じの戻るボタン
document.getElementById('back-button').addEventListener('click', () => {
    window.location.href = 'index.html';
});
