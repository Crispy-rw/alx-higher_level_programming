-- MYSQL script that creates the table id_not_null on your MySQL server
-- Description: id INT with the default value 1 and name VARCHAR(256)
CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));
