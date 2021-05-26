create database productDB;
CREATE USER 'user'@'%' IDENTIFIED WITH mysql_native_password BY 'user_password';
GRANT ALL ON productDB.* TO 'user'@'%';
FLUSH PRIVILEGES;