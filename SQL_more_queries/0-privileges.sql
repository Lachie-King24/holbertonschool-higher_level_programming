-- 0-privileges.sql
-- Create users if they don't exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';

-- Optionally grant minimal privileges so SHOW GRANTS works
GRANT USAGE ON *.* TO 'user_0d_1'@'localhost';

FLUSH PRIVILEGES;

-- Show the privileges for both users
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
