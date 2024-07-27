function fetchCatImage() {
    fetch('https://api.thecatapi.com/v1/images/search')
      .then(response => response.json())
      .then(data => {
        if (data && data.length > 0) {
          const imageUrl = data[0].url;
          console.log('猫画像のURL:', imageUrl);
          displayImage(imageUrl);
        } else {
          console.error('猫画像の取得に失敗しました');
        }
      })
      .catch(error => console.error('エラーが発生しました:', error));
  }
  
  function displayImage(url) {
    const imgElement = document.getElementById('catImage');
    imgElement.src = url;
  }
  
  document.getElementById('fetchButton').addEventListener('click', fetchCatImage);