-- Write a script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on a MySQL server
/*	cities description:
		id INT unique, auto generated, can’t be null and is a primary key
		state_id  INT, can’t be null and must be a FOREIGN KEY that references to id of the states table
		name VARCHAR(256) can’t be null
*/
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT UNIQUE NOT NULL AUTO_INCREMENT,
	state_id INT NOT NULL,
	name VARCHAR(25) NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (state_id) REFERENCES cities(id)
);
