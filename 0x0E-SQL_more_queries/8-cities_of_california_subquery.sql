-- Write a script that lists all the cities of California that can be found in the database hbtn_0d_usa
/*	Result must be sorted in ascending order
	One must not use the JOIN keyword
*/
SELECT id, name FROM cities
WHERE state_id =
	(SELECT id FROM states
	 WHERE name LIKE 'California')
ORDER BY cities.id ASC;
