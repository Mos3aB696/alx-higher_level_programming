const $ = window.$;

$(function () {
  $('DIV#toggle_header').click(function () {
    if ($('header').hasClass('green')) {
      $('header').removeClass('green').addClass('red');
    } else {
      $('header').removeClass('red').addClass('green');
    }
  });
});
