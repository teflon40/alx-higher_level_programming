/* Write a script that lists all the genres of the tv_show Dexter in the database */
--
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
--
SELECT tv_genres.name FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title LIKE 'Dexter'
ORDER BY tv_genres.name;
