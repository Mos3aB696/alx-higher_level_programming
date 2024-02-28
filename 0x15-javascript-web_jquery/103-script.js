const $ = window.$;
$(() => {
  // Function to fetch and display the translation
  function fetchTranslation () {
    const languageCode = $('#language_code').val();
    const url = 'https://www.fourtonfish.com/hellosalut/hello/' + languageCode;

    $.get(url, function (data) {
      $('#hello').text(data);
    });
  }

  // Trigger fetchTranslation on button click
  $('#btn_translate').click(function () {
    fetchTranslation();
  });

  // Trigger fetchTranslation on ENTER key press in the input field
  $('#language_code').keypress(function (e) {
    if (e.which === 13) {
      // 13 is the key code for ENTER
      fetchTranslation();
    }
  });
});
