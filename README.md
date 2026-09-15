# Supermarket Billing System (SBMS)

**Note: The following project is still in development and new features are going to be added soon and some are going to be removed**

A Supermarket Billing System made for small retail businesses to scan their customer's items , print the total bill and also store the customer's info in order to give offers for the next visit 

This Software was made so that it makes it simple enough for the small businesses to use a free and open source software rather than paying or using complex ones 

## Prerequisities for running this program
If u want to execute this program in your device 

1) Make sure u have __Python 3.x__ , __MySQL__ and __mysqlconnector__ installed in your device .

2) Download and Execute the code from [Database Code](db) in the MySQL Command Line Client to create the tables required for this program

3) Download the python code from [Source Code](src) and then change the User and password in the database connection to ur set password in MySQL

4) Then execute the code to run the program


## Login Screen

   
   <img width="422" height="312" alt="Login Screen" src="https://github.com/user-attachments/assets/d6e91f8b-76a3-4bac-a91f-2637706f6859" />

   Here is the login screen to the Billing system that takes username and password as the input ,
   this ensures only admin and cashiers can use this system and nobody has access to this.

   ### After Successful Login

   
   <img width="422" height="312" alt="Login Success" src="https://github.com/user-attachments/assets/23b9fe6c-a774-47b0-a5ae-2aef8ed92648" />

   <img width="422" height="312" alt="Login Success 2" src="https://github.com/user-attachments/assets/fd76fb7e-02d8-49b1-9816-f4dd94dd9429" />

## Billing Screen

  This is the SBMS software where it makes the retailers job easier as it has so many features to help them like :
  1) calendar to display current date 
  2) database view table to show all the records of the previous customers that shopped in the store before
  3) Bill display to show the bill before printing it out
  4) Auto-randomized unique code that is provided to each customer , which they can use to avail for discounts for next purchase

     ### Entering Customer Details and scanning the cart items

     
     <img width="1359" height="729" alt="Scanning Items_Adding items" src="https://github.com/user-attachments/assets/ac2c4725-7cf0-4972-857c-7fb23f5dc545" />


     ### Saving the customer details in the database after scanning of products

     
     <img width="1366" height="728" alt="Saving items to database" src="https://github.com/user-attachments/assets/0bfeb4ba-64b2-4360-b100-82512b25b466" />

     ### Printing the bill
       You can also see that the entered customer details is saved to a database and is being displayed in the table

     <img width="1366" height="728" alt="Printed Bill" src="https://github.com/user-attachments/assets/d7395488-dada-4b30-8594-9a5f3ff19ca6" />

     ### Customer details in the database

     <img width="979" height="512" alt="Database Changed" src="https://github.com/user-attachments/assets/955da2b5-53ca-4d60-a69a-812e1a662427" />


## Upcoming Features 

   1) QR code generated for UPI payments
   2) Shopping cart viewer of customer
   3) Scanned items viewer with prices
   4) Discounts for previously visited customers
   5) Removal of Calendar and adding a digital date day time
   6) Printing the Bill in .pdf and .png format and can be exported to a printer

      Deciding to add more .....................

   






