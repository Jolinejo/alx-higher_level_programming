-- alter format
-- alter database
ALTER DATABASE
    hbtn_0c_0
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;
-- alter table
USE hbtn_0c_0;
ALTER TABLE
    first_table
    CONVERT TO CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;
-- alter column
ALTER TABLE
    first_table
    MODIFY COLUMN name
    VARCHAR(256)
    COLLATE utf8mb4_unicode_ci;
