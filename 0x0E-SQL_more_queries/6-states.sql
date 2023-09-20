-- create table id def 1
-- create db
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- create table
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256)
);
