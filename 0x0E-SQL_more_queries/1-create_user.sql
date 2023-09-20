-- create user and set grants
-- create
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- SET PRIVILAGES
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
