"""Login Page Code for a Supermarket Billing Management System (SBMS) using Tkinter and MySQL."""

#Importing required libraries for the project
import tkinter as tk
from tkinter import messagebox as mb
import mysql.connector as ms
from mainwindow_code import MainWindow

#Database Connection
try:
    myconn = ms.connect(
        host="localhost",
        user="root",
        password="Mrunalsri6-", #Hiding the password cus uk password is password 
        database="supermarket_login"
    )
    if myconn.is_connected():
        print("Successfully connected to the database")
    Cur = myconn.cursor()

except ms.Error:
     mb.showerror("Connecting Error!!!!!", "Error occurred while connecting to the Database")


#Class
class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page for SBMS")
        self.Center_LoginWindow(420, 280)
        self.root.resizable(False, False)

        #GUI Elements
        title_label = tk.Label(self.root, text="LOGIN", font=("Segoe UI", 18, "bold"))
        title_label.pack(pady=10)

        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        username_label = tk.Label(frame, text="Username :", font=("Segoe UI", 10, "bold"))
        username_label.grid(row=0, column=0, padx=0, pady=10)
        self.username_entry = tk.Entry(frame)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        password_label = tk.Label(frame, text="Password :", font=("Segoe UI", 10, "bold")) # Password isn't hidden but will come next time 
        password_label.grid(row=1, column=0, padx=0, pady=10)
        self.password_entry = tk.Entry(frame) 
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        login_button = tk.Button(
            self.root,
            text="Login",
            command=self.login_function,
            width=10,
            bg="light green",
            font=("Segoe UI", 10, "bold")
        )
        login_button.pack(pady=10)

    #Functions
    def login_function(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "" or password == "":
            mb.showerror("Error!!!!!!", "All fields are required!!!!!!")
        else:
            try:
                query = "SELECT * FROM users WHERE username = %s AND password = %s"
                Cur.execute(query, (username, password))
                result = Cur.fetchone()

                if result:
                    mb.showinfo("Success", "Login Successful")
                    if username.startswith("adm"):
                        mb.showinfo("Admin Login", "Welcome Admin to the Supermarket Billing Management System (SBMS)")  # SBMS to access admin login is still pending so upcoming ver it will include 
                    else:
                        mb.showinfo("User Login", "Welcome User to the Supermarket Billing Management System (SBMS)")
     
                    # Closes the login window
                    self.root.destroy()

                    # Creates a new main window and opens the MainWindow class
                    new_root = tk.Tk()
                    MainWindow(new_root)
                    new_root.mainloop()

                else:
                    mb.showerror("Error", "Invalid Username or Password")

            except ms.Error:
                mb.showerror("Error", "An error occurred while connecting to the Database")
     
     #Centers Login Window
    def Center_LoginWindow(self, wt, ht):
        screenw = self.root.winfo_screenwidth()
        screenh = self.root.winfo_screenheight()
        x = (screenw - wt) // 2
        y = (screenh - ht) // 2
        self.root.geometry(f"{wt}x{ht}+{x}+{y}")


#Main Program
if __name__ == "__main__":
    root = tk.Tk()
    app = LoginPage(root)
    root.mainloop()


        

        
            
            
            
            

        
