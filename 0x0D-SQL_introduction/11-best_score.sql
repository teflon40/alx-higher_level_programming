-- Write a script that lists all records of with score >= 10 in the table second_table of a database
/*	** Results should display both the score and the name
	** Records should be ordered by score (top first)
*/
SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;
