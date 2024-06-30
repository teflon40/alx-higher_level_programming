/* Write a script that lists all shows without the genre Comedy in the database */
--
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the title
--
SELECT tv_shows.title FROM tv_shows
WHERE tv_shows.id NOT IN
	(SELECT tv_show_genres.show_id FROM tv_show_genres
	 JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
	 WHERE tv_genres.name LIKE 'Comedy')
ORDER BY tv_shows.title;
