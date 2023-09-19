-- create table and add rows
CREATE TABLE IF NOT EXISTS second_table(
	id INT,
	name VARCHAR(256),
	score INT
);
-- insert first row
INSERT INTO second_table (id, name, score) VALUES (1, "John", 10);
-- insert second row
INSERT INTO second_table (id, name, score) VALUES (2, "Alex", 3);
-- insert third row
INSERT INTO second_table (id, name, score) VALUES (3, "Bob", 14);
-- insert fourth row
INSERT INTO second_table (id, name, score) VALUES (4, "George", 8);
