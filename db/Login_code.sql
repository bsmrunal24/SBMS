CREATE DATABASE supermarket_login;

USE supermarket_login;

/*
This table stores all login credentials and access levels for the store staff
   Id       => A unique, automatically generated number for each staff
   Username => A unique login name of the staff
   Password => user's password
   Role     => 'Admin' or 'Cashier'
*/

CREATE TABLE users
     ( Id INT PRIMARY KEY,
       Username VARCHAR(50),
       Password VARCHAR(64),
       Role enum('Admin','Cashier') Default 'Cashier');

DESCRIBE users;
