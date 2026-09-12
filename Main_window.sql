CREATE DATABASE supermarket;
USE supermarket;
/* 
   This table stores all Purchase details of all customers
   Bill_No => A randomly Generated Bill No
   Customer_Name => Name of Customer
   Phone_No => A 10-Digit phone number of the customer
   Date => Current Date
   Time => Current Time
   TotalAmount => Total Amount of all items purchased
   */
   
CREATE TABLE Customer_Details
        (Bill_No VARCHAR(5) PRIMARY KEY ,
         Customer_Name VARCHAR(20),
         Phone_No BIGINT,
         Date DATE,
         Time TIME,
         TotalAmount INT);

DESCRIBE Customer_Details;
        