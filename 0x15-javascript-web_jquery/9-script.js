// fetches from URL and displays the value of hello 
// from that fetch in the HTML tag DIV#hello.
$('document').ready(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=f', function (data) {
    $('DIV#hello').text(data.hello);
  });
});
