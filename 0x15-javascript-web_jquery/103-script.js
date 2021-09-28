// Fetches and prints how to say “Hello” depending on the language
const fourtonfish = 'https://www.fourtonfish.com/hellosalut/';

$(document).ready(() => {
  $('INPUT#language_code').keypress((e) => {
    if (e.keyCode === 13) {
      $('INPUT#btn_translate').click();
    }
  });
  $('INPUT#btn_translate').click(() => {
    const value = $('INPUT#language_code').first().val();
    $.getJSON(`${fourtonfish}?lang=${value}`).done((data) =>
      $('DIV#hello').text(data.hello).show()
    );
  });
});
