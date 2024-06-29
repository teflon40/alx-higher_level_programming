/* Write a script that lists all the comedy series in the database */
--
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the series title
--
SELECT tv_shows.title FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name LIKE 'Comedy'
ORDER BY tv_shows.title;
