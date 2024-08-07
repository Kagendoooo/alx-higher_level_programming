//fetches and prints how to say “Hello” depending on the language
$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    $('DIV#hello').empty();
    const len = $('INPUT#language_code').val();
    $.ajax({
      type: 'GET',
      url: 'https://www.fourtonfish.com/hellosalut/hello/' + len,
      success: function (data) {
        $('DIV#hello').append(data.hello);
      }
    });
  });
});
