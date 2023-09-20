-- Dexter genres
SELECT tv_genres.name
FROM tv_shows LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres
ON tv_genres.id = tv_show_genres. genre_id
WHERE tv_shows.title = "Dexter"
ORDER BY tv_genres.name;
