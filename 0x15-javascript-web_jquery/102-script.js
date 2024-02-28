const $ = window.$;
$(() => {
  $('#btn_translate').click(function () {
    const languageCode = $('#language_code').val();
    const url = 'https://www.fourtonfish.com/hellosalut/hello/' + languageCode;

    $.get(url, (data) => {
      $('#hello').text(data);
    });
  });
});
