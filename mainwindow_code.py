"Supermarket Management System (SBMS) using Tkinter and MySQL Database"

#Importing required libraries
import tkinter as tk
from tkinter import ttk
import random
from tkinter import messagebox as mb
import mysql.connector as ms
from mysql.connector import Error
from tkcalendar import *
import datetime
import time

#Database Connection
try:
    myconn = ms.connect(
        host="localhost",
        user="root",
        password="**********",
        database="supermarket"
    )
    if myconn.is_connected():
        print("Successfully Connected to Database")
        
except ms.Error:
    mb.showerror("Connection Error", "Error occurred while connecting to the Database")

#Main Window Class
class MainWindow:
    def __init__(this, root):
        this.root = root
        this.root.title("Supermarket Billing Management System (SBMS)")
        this.root.geometry("1366x768")
        this.root.iconbitmap("grocery.ico")
        
        #Variables Used in the Main Window
        this.items = [
        "Milk" ,"Bread" ,"Butter" ,"Cheese" ,"Yogurt" ,"Eggs" ,"Juice" ,"Water" ,"Soda" ,"Tea" ,"Coffee" ,"Cereal" ,"Rice"
        ]

        this.items_cost = {"Milk": 35,"Bread": 20,"Butter": 30,"Cheese": 40,"Yogurt": 10,"Eggs": 25,"Juice": 20,"Water": 10,"Soda": 15,"Tea": 30,"Coffee": 40,"Cereal": 35,"Rice": 20}
         
        this.cart = []   #Billing Cart 
        """Implentation of Cart frame  later check other ver in repo"""

        global today_date
        today_date = datetime.date.today()

        global today_time
        today_time = datetime.datetime.now().time().strftime("%H:%M:%S")

        this.code = this.random_bill_number()

#Creating GUI widgets with tkinter      
        #Background Frames
        Frame_root = tk.Frame(this.root, bd=10, relief=tk.RAISED)
        Frame_root.pack(fill=tk.BOTH, expand=True)

        Frame_main = tk.Frame(Frame_root, bd=9, bg="#d1d1d1", relief=tk.GROOVE)
        Frame_main.pack(fill=tk.BOTH, expand=True)
        
        #Title Frame
        Title_Label = tk.Label(
            Frame_main,
            font=("Segoe UI", 18, "bold"),
            text="Supermarket Billing Management System (SBMS)",
            bd=7,
            relief=tk.RAISED,
            bg="light blue"
            )
        Title_Label.pack(fill=tk.X)

        #Details Frame
        Customer_details_Frame = tk.LabelFrame(
            Frame_main,
            text="Customer Details",
            font=("Segoe UI",14, "bold"),
            bd=7,
            relief=tk.GROOVE,
            bg="#da9aff"
        )
        Customer_details_Frame.place(x=0, y=50, relwidth=1)

        Customer_details_Label1 = tk.Label(
            Customer_details_Frame,
            font=("Segoe UI", 13, "bold"),
            text="Customer Name :",
            fg = "Black",
            bg="#da9aff"
        )
        Customer_details_Label1.grid(row=0, column=0, padx=20, pady=5)
        this.Customer_name_entry = tk.Entry(Customer_details_Frame, width=50 , relief=tk.GROOVE, bd = 4 )
        this.Customer_name_entry.grid(row=0, column=1, padx=10, pady=5)

        Customer_details_Label2 = tk.Label(
            Customer_details_Frame,
            font=("Segoe UI", 14, "bold"),
            text="Phone Number :",
            fg = "Black",
            bg="#da9aff"
        )
        Customer_details_Label2.grid(row=0, column=2, padx=20, pady=5)

        this.Phone_number_entry = tk.Entry(Customer_details_Frame, width=50 , relief=tk.GROOVE, bd = 4 )
        this.Phone_number_entry.grid(row=0, column=3, padx=10, pady=5)

        Customer_details_Label3 = tk.Label(
            Customer_details_Frame,
            font=("Segoe UI", 14, "bold"),
            text=f"Bill Number : {this.code}", 
            fg = "Black",
            bg="#da9aff"
        )
        Customer_details_Label3.grid(row=0, column=4, padx=20, pady=5)

        #Calendar Frame
        """Removing calender in next ver as it is a waste of space Add mabye upcoming vers"""
        Calender_Frame = tk.LabelFrame(
            Frame_main,
            text="Calender",
            font=("Segoe UI", 12, "bold"),
            bd=7,
            relief=tk.GROOVE,
            bg="#f1ea87"
        )
        Calender_Frame.place(x=0, y=120, width=270, height=230)
        cal = Calendar(Calender_Frame, selectmode='day', day = today_date.day , month = today_date.month, year = today_date.year, date_pattern = 'dd-mm-yyyy')
        cal.grid(row = 0 , column = 2 , padx = 0 , pady = 10)
        
        #Items Frame
        Selection_Box_Frame = tk.LabelFrame(
            Frame_main,
            text="Items Selection ",
            font=("Segoe UI", 12, "bold"),
            bd=7,
            relief=tk.GROOVE,
            bg="#6afa87"
        )
        Selection_Box_Frame.place(x=275, y=120, width=719, height=230)

        Label1_Spinbox1 = tk.Label(
            Selection_Box_Frame,
            font=("Segoe UI", 13, "bold"),
            text="Item :",
            bg="#6afa87"
        )
        Label1_Spinbox1.grid(row=0, column=1, padx=10, pady=10)

        this.Item_Combobox = ttk.Combobox(
            Selection_Box_Frame,
            font=("Segoe UI", 11, "bold"),
            width=15,
            state="readonly"
        )
        this.Item_Combobox['values'] = this.items
        this.Item_Combobox.grid(row=0, column=2, padx=10, pady=10)
        this.Item_Combobox.current(0)

        Label2_Spinbox2 = tk.Label(
            Selection_Box_Frame,
            font=("Segoe UI", 13, "bold"),
            text="Quantity :",
            bg="#6afa87"
        )
        Label2_Spinbox2.grid(row=1, column=1, padx=10, pady=10)
        this.Quantity_Spinbox = tk.Spinbox(
            Selection_Box_Frame,
            from_=1,
            to=20,
            width=13,
            font=("Segoe UI", 12, "bold")
        )
        this.Quantity_Spinbox.grid(row=1, column=2, padx=10, pady=10)

        Add_Item_Button = tk.Button(
            Selection_Box_Frame,
            text="Add Item",
            width=15,
            bg="light green",
            font=("Segoe UI", 10, "bold"),
            command = lambda : this.Add_item_to_cart(this.Item_Combobox.get(), int(this.Quantity_Spinbox.get())
        ))

        Add_Item_Button.grid(row=2, column= 0, padx = 10, pady=20)

        Delete_Item_of_Cart_Button = tk.Button(
            Selection_Box_Frame,
            text="Delete Last Cart Item",
            width=20,
            bg="light green",
            font=("Segoe UI", 10, "bold"),
            command = lambda: this.Delete_Last_item())
        Delete_Item_of_Cart_Button .grid(row=2, column=1, padx = 10, pady=20)

        Print_Bill_Button = tk.Button(
            Selection_Box_Frame,
            text="Print Bill",
            width=15,
            bg="light green",
            font=("Segoe UI", 10, "bold"),
            command = this.Bill_Display
        )
        Print_Bill_Button.grid(row=2, column=2, padx = 10, pady=20)

        #Display bill frame
        Bill_Slip_Frame = tk.LabelFrame(
            Frame_main,
            text="Bill Slip",
            font=("Segoe UI", 12, "bold"),
            bd=7,
            relief=tk.GROOVE,
            bg="#ffffff"
        )
        Bill_Slip_Frame.place(x=1000, y=120, width=325, height=550)

        scroll_y_dir = tk.Scrollbar(Bill_Slip_Frame, orient=tk.VERTICAL)
        scroll_y_dir.pack(side=tk.RIGHT, fill=tk.Y)

        this.bill_text = tk.Text(
            Bill_Slip_Frame,
            font=("Segoe UI", 10, "bold"),
            yscrollcommand=scroll_y_dir.set
        )
        this.bill_text.pack(fill=tk.BOTH, expand=True)
        scroll_y_dir.config(command=this.bill_text.yview)

        #Summary Frame
        Customer_Summary_frame = tk.LabelFrame(
            Frame_main,
            text = "Billing Database View",
            font=("Segoe UI", 12, "bold"),
            bd=7,
            relief=tk.GROOVE,
            bg="#ff8686"  
        )

        Customer_Summary_frame.place(x=0, y=350, width=1000, height=320)

        scrlbar = ttk.Scrollbar(Customer_Summary_frame, 
                           orient ="vertical")
        scrlbar.pack(side=tk.RIGHT, fill=tk.Y)

        Customer_Summary_View = ttk.Treeview(
            Customer_Summary_frame,
            columns=("bill", "name", "phone", "date", "time", "total"),
            show="headings",
            yscrollcommand= scrlbar.set,
            
        )
        this.Customer_Summary_View = Customer_Summary_View

        Customer_Summary_View.heading("bill", text="Bill No")
        Customer_Summary_View.heading("name", text="Customer Name")
        Customer_Summary_View.heading("phone", text="Phone")
        Customer_Summary_View.heading("date", text="Date")
        Customer_Summary_View.heading("time", text="Time")
        Customer_Summary_View.heading("total", text="Total Amount")

        Customer_Summary_View.column("bill", width=100)
        Customer_Summary_View.column("name", width=200)
        Customer_Summary_View.column("phone", width=150)
        Customer_Summary_View.column("date", width=150)
        Customer_Summary_View.column("time", width=150)
        Customer_Summary_View.column("total", width=100)

        this.Customer_Summary_View.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrlbar.config(command = Customer_Summary_View.yview)

        Save_Button = tk.Button(
        Selection_Box_Frame,
        text="Save to Database",
        width=20,
        bg="light green",
        font=("Segoe UI", 10, "bold"),
        command=this.Add_to_Database
        )
        Save_Button.grid(row=2, column=3, padx=10, pady=20)

        this.Load_Database()
        

#Functions
    def Item_Code (this):
        c = chr(random.randint(65,90))+str(random.randint(0,13))
        return c

    def random_bill_number(this):
        bill_number = chr(random.randint(65,90))+str(random.randint(1000, 9999))
        return bill_number
        
    def generate_bill_no(this):
        this.code = this.random_bill_number()
        print(this.code)
    
    def Delete_Last_item(this):
       if len(this.cart) > 0:
            this.cart.pop()
       else:
            mb.showinfo("Cart Empty", "No items left to delete.")

    def Add_to_Database(this):
        try:
            CustName = this.Customer_name_entry.get().strip()
            PhNo = this.Phone_number_entry.get().strip()

            if CustName == "" or PhNo == "":
                mb.showwarning("Missing Data", "Enter customer name and phone number before saving.")
                return
            
            date_str = today_date.strftime("%Y-%m-%d")
            time_str = today_time
            Cur = myconn.cursor()
            query = ("INSERT INTO Customer_Details (Bill_No, Customer_Name, Phone_No, Date, Time, TotalAmount)VALUES (%s, %s, %s, %s, %s, %s)")
            values = (this.code,CustName,PhNo,date_str,time_str,this.Total())

            Cur.execute(query, values)

            myconn.commit()

            Cur.close()

            mb.showinfo("Saved", "Cart items saved to database!")

            this.Customer_Summary_View.insert("", tk.END,values=(this.code, CustName, PhNo, date_str, time_str, this.Total()))

        except ms.Error as e:
            mb.showerror("Database Error", "Error Ocurred while Inserting Records into Database")


    def Add_item_to_cart(this, item, quantity):
        global price 
        price = this.items_cost[item] * quantity
        this.cart.append([item,quantity,price])
    
    def Total(this):
        Total_price = 0
        for i in range(len(this.cart)):
            Total_price += this.cart[i][2]
        return Total_price
    
    def Load_Database(this):
        try:
            Cur = myconn.cursor()
            Cur.execute("SELECT * FROM customer_details")

            rows = Cur.fetchall()

            this.Customer_Summary_View.delete(*this.Customer_Summary_View.get_children())

            for row in rows:
                this.Customer_Summary_View.insert("", tk.END, values=row)
        
        except ms.Error as e:
            mb.showerror("Database Error", str(e))
            print(e)
    
    def Bill_Display(this):
        this.bill_text.insert(tk.END, "\t        SUPERMARKET BILL \n")
        this.bill_text.insert(tk.END, "\n")
        this.bill_text.insert(tk.END, "Address :     Reliance Fresh, Plot No. 45,\n")
        this.bill_text.insert(tk.END, "               Link Road, Malad West, Mumbai\n")
        this.bill_text.insert(tk.END, "\n")
        this.bill_text.insert(tk.END, "Contact No.:  +91 9876543210\n")
        this.bill_text.insert(tk.END, "\n")
        this.bill_text.insert(tk.END, f"Date :  {today_date}                    Time : {today_time}\n" ) 
        this.bill_text.insert(tk.END, "\n")
        this.bill_text.insert(tk.END, "================================\n")
        this.bill_text.insert(tk.END, f"Bill Number: {this.code} \n")
        this.bill_text.insert(tk.END, f"Customer Name: {this.Customer_name_entry.get()}\n")
        this.bill_text.insert(tk.END, f"Customer Phone No: {this.Phone_number_entry.get()}\n")
        this.bill_text.insert(tk.END, "\n")
        this.bill_text.insert(tk.END, "   Item No     Item Name      Quantity       Price\n")
        this.bill_text.insert(tk.END, "---------------------------------------------------------\n")
        item = this.Item_Combobox.get()
        quantity = int(this.Quantity_Spinbox.get())
        for k in range(len(this.cart)):
            this.bill_text.insert(tk.END, f"    {this.Item_Code():<20} {this.cart[k][0]: <20} {this.cart[k][1] : <8}  ₹{this.cart[k][2] :<20}\n")  
            if len(this.cart)==0:
                mb.showinfo("Empty Cart", "No items in the cart to display.")
                break
            else:
                pass

        this.bill_text.insert(tk.END, "---------------------------------------------------------\n")
        this.bill_text.insert(tk.END, f"Total: ₹{this.Total()}\n")
        this.bill_text.insert(tk.END, "================================\n")
        this.bill_text.insert(tk.END, "             Thank you for shopping with us!\n")
        this.bill_text.insert(tk.END, "                            Visit Again!\n")

#Main Program
if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()

