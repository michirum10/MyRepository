//***************************\\
// ハンバーガーボタン、メニュー \\
//***************************\\
const ham = document.querySelector('#js-hamburger');
const nav = document.querySelector('#js-nav');

let hamburgerAction = function () {
  ham.classList.toggle('active');
  nav.classList.toggle('active');
}

// ハンバーガーメニューのボタンとナビにクリックアクションを追加
//***修正ポイント***//
nav.addEventListener('click',hamburgerAction);
// nav.addEventListener('click', hamburgerAction);
// ナビゲーションの略
// . ～の
// ()丸括弧がつくとメソッド、関数fanction.動詞になる
// ナビゲーションのアドベントリストを行うという意味

// ''で囲むと文字として認識される
// ;は任意
// 途中まで打つと候補が出てくる。コード補完、snippet。ctrl+スペースで続きからかける
ham.addEventListener('click',hamburgerAction)
// ham.addEventListener('click', hamburgerAction);


//***********\\
// スクロール \\
//***********\\
//スクロールした際の動きを関数でまとめる

//定義する時
function PageTopAnime() {
  var scroll = $(window).scrollTop();
  //上から200pxスクロールしたら表示されるように修正
  //スクロールの量によってトップへ移動するボタンが表示される
  //***修正ポイント***//
  if (scroll >= 200){
    //#page-topについているRightMoveというクラス名を除く
    $('#page-top').removeClass('RightMove');
    //#page-topについているLeftMoveというクラス名を付与
    $('#page-top').addClass('LeftMove');
  }else{
    //すでに#page-topにLeftMoveというクラス名がついていたら
    if($('#page-top').hasClass('LeftMove')){
      //LeftMoveというクラス名を除き
      $('#page-top').removeClass('LeftMove');
      //RightMoveというクラス名を#page-topに付与
      $('#page-top').addClass('RightMove');
    }
  }
}

// 画面をスクロールをしたら動かしたい場合の記述
// 実行する時
$(window).scroll(function () {
  // スクロールした際の動きの関数を呼ぶ
  //***修正ポイント***//
  // PageTopAnime();
  PageTopAnime();
});

// ページが読み込まれたらすぐに動かしたい場合の記述
$(window).on('load', function () {
  // スクロールした際の動きの関数を呼ぶ
  //***修正ポイント***//
  // PageTopAnime();
});

// #page-topをクリックした際の設定
$('#page-top').click(function () {
  $('body,html').animate(
  {
        //ページトップまでスクロール
        scrollTop: 0
    },
  // ページトップスクロールの速さ。数字が大きいほど遅くなる
  // どのくらいの時間をかけてアニメーションを実行するか？
  // ちょうど良い速度に調整してください。
  //***調整ポイント***//
  // 数字が小さいほど早い。ミリ秒
  500
);
//リンク自体の無効化
  return false;
});
//*******\\
// slick \\
//*******\\
$('.slider').slick({
  //左右の矢印はなし
  arrows: true,
  //自動的に動き出すか。初期値はfalse。
  autoplay: true,
  //***調整ポイント***//
  //自動的に動き出す待ち時間。
  // ちょうど良い速度に調整してください。
  autoplaySpeed: 3500,
  //***調整ポイント***//
  // ちょうど良い速度に調整してください。
  //スライドのスピード。
  speed: 800,
//スライドをループさせるかどうか。初期値はtrue。
  infinite: true,
//オンマウスでスライドを一時停止させるかどうか。初期値はtrue。
  pauseOnHover: true,
//フォーカスした際にスライドを一時停止させるかどうか。初期値はtrue。
  pauseOnFocus: false,
  //***調整ポイント***//
  //動き方。初期値はeaseですが、スムースな動きで見せたいのでlinear
  // 好きなモードを選んでください
  // cssEase: 'ease-in',
  // cssEase: 'ease',
  cssEase: 'linear',
  //スライドを画面に3枚見せる
  slidesToShow: 2,
  //1回のスライドで動かす要素数
  slidesToScroll: 2,
});
