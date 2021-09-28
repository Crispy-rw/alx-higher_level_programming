// Fetches and prints how to say “Hello” depending on the language
const fourtonfish = 'https://www.fourtonfish.com/hellosalut/';

$(document).ready(() => {
  $('INPUT#btn_translate').on('click', () => {
    const value = $('INPUT#language_code').first().val();
    $.getJSON(`${fourtonfish}?lang=${value}`).done((data) =>
      $('DIV#hello').text(data.hello).show()
    );
  });
})
