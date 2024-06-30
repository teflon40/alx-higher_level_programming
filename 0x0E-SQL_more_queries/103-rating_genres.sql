/* Write a script that lists all genres in the database hbn_0d_tvshows_rate by their rating. */
--
-- Each record should display: tv_genres.name - rating sum
-- Results must be sorted in descenging order by their rating
--
SELECT tv_genres.name AS genre, SUM(tv_show_ratings.rate) AS rating FROM tv_genres
LEFT JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
LEFT JOIN tv_show_ratings ON tv_show_genres.show_id = tv_show_ratings.show_id
GROUP BY tv_genres.name
ORDER BY rating DESC;
