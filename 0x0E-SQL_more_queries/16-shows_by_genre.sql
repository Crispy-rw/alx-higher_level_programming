-- List all shows and genres linked to thst show from the database hbtn_0d_tvshows
SELECT tv_shows.title AS title, tv_genres.name AS name
FROM tv_shows
LEFT OUTER JOIN tv_show_genres
ON tv_show_genres.show_id = tv_shows.id
LEFT OUTER JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
ORDER BY title ASC, name ASC;
