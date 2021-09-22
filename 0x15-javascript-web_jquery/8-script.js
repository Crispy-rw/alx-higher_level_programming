$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  for (const movies of data.results) {
    $('UL#list_movies').append(`<li>${movies.title}</li>`);
  }
});
