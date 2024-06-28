-- Write a script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on a MySQL server
/*	states descript:
		id INT unique, auto generated, can't be null and it's a primary key
		name VARCHAR(256) can't be null
*/
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id)
);
