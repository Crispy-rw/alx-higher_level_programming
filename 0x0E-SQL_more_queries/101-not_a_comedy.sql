-- List all shows without the genre comedy in the database hbtn_0d_tvshows
SELECT DISTINCT tv_shows.title AS title
FROM tv_shows
LEFT OUTER JOIN tv_show_genres
ON tv_show_genres.show_id = tv_shows.id
LEFT OUTER JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_shows.title NOT IN
      		          (SELECT tv_shows.title
			     FROM tv_shows
			     INNER JOIN tv_show_genres
			     ON tv_show_genres.show_id = tv_shows.id
			     INNER JOIN tv_genres
			     ON tv_genres.id = tv_show_genres.genre_id
			     WHERE tv_genres.name = "Comedy")
ORDER BY title ASC;
