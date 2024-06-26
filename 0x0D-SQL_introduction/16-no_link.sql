-- Write a script that lists all record of the table second_table of a database.
SELECT score, name FROM second_table
WHERE name != ''
ORDER BY score DESC;
