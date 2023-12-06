$(document).ready(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: function (data) {
      $.each(data.results, function (i, movies) {
        $('UL#list_movies').append('<li>' + movies.title + '</li>');
      });
    }
  });
});
