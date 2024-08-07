//fetches and lists the title for all movies by using a URL
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  console.log(data);
  data.results.forEach(film => {
    $('UL#list_movies').append('<li>' + film.title + '</li>');
  });
});
