-- Write a script that creates the table force_name in a MySQL server.
/*	 force_name description:
		** id INT
		** name VARCHAR(256) NOT NULL
*/
CREATE TABLE IF NOT EXISTS force_name (
	id INT,
	name VARCHAR(256) NOT NULL
);
