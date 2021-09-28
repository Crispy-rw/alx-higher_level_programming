// Adds, removes and clears LI elements from a list when the user clicks:
window.setTimeout(() =>
  $('DIV#add_item').click(() => $('UL.my_list').append('<li>Item</li>'))
);
window.setTimeout(() =>
  $('DIV#remove_item').click(() => $('UL.my_list LI').last().remove())
);
window.setTimeout(() =>
  $('DIV#clear_list').click(() => $('UL.my_list LI').remove())
);
