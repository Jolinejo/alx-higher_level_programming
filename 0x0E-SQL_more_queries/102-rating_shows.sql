-- rating
SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS rating
FROM tv_shows INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_show_ratings
ON tv_show_ratings.show_id = tv_show_genres.show_id
GROUP BY tv_shows.title
ORDER BY rating DESC;
