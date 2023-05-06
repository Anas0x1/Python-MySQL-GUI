import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
import subprocess

#MySQL credentials
correct_user = "YOUR-USERNAME"
correct_pass = "YOUR-PASSWORD"

#Register function	
def create_user():
	subprocess.call(["python" , "create_user.py"])
	
#Register function	
def delete_user():
	subprocess.call(["python" , "delete_user.py"])
	
#Query function
def run_query():
	subprocess.call(["python" , "query.py"])
		
#create database function
def create_db():
	subprocess.call(["python" , "create_db.py"])
	
#Delete database function
def delete_db():
	subprocess.call(["python" , "delete_db.py"])
	
#List databases function
def list_db():
	conn = mysql.connector.connect(
		host = "localhost",
		user = "YOUR-USERNAME",
		passwd = "YOUR-PASSWORD"
		)	
	query = """ show databases; """
	cursorObject = conn.cursor()
	cursorObject.execute(query)
	
	myresult = cursorObject.fetchall()
	messagebox.showinfo("Query results " , str(myresult))
	conn.close()
	
#List databases function
def list_users():
	conn = mysql.connector.connect(
		host = "localhost",
		user = "YOUR-USERNAME",
		passwd = "YOUR-PASSWORD"
		)	
	query = """ select user from mysql.user; """
	cursorObject = conn.cursor()
	cursorObject.execute(query)
	
	myresult = cursorObject.fetchall()
	messagebox.showinfo("Query results " , str(myresult))
	conn.close()

# Check if the username and password are correct
def login(username, password):
	if username == "" or password == "":
		messagebox.showerror("Error!","All fields are required")
	elif username == correct_user and password == correct_pass:
		create_new_window(username)
	else:
		messagebox.showerror("Error", "Invalid username or password")
		

######################################################################

# Create a Toplevel window to show the other functions
def create_new_window(user):
	new_window = Toplevel()
	new_window.geometry("600x300")
	new_window.title("DBMS Functions")
	
	#Defining the third row (user)
	lblthrdrow = tk.Label(new_window, text ="User : ")
	lblthrdrow.place(x = 50, y = 50)
	
	#Defining the forth row (database)
	lblthrdrow = tk.Label(new_window, text ="Database : ")
	lblthrdrow.place(x = 50, y = 100)
	
	#Defining the sixth row (query)
	lblthrdrow = tk.Label(new_window, text ="Query : ")
	lblthrdrow.place(x = 50, y = 150)
	
	# Add buttons and labels to the new window
	button1 = tk.Button(new_window, text="Create User", bg="green", command=create_user)
	button1.place(x=150, y=50, width=120)
	button2 = tk.Button(new_window, text="Delete User", bg="#66ff66", command=delete_user)
	button2.place(x=300, y=50, width=120)
	button3 = tk.Button(new_window, text="List Users", bg="#c2c2d6", command=list_users)
	button3.place(x=450, y=50, width=120)
	button4 = tk.Button(new_window, text="Create Database", bg="#800080", command=create_db)
	button4.place(x=150, y=100, width=120)
	button5 = tk.Button(new_window, text="Delete Database", bg="#ff99ff", command=delete_db)
	button5.place(x=300, y=100, width=120)
	button6 = tk.Button(new_window, text="List Databases", bg="#b3b3ff", command=list_db)
	button6.place(x=450, y=100, width=120)
	button7 = tk.Button(new_window, text="Run Query", bg="#cc6600", command=run_query)
	button7.place(x=150, y=150, width=420)
	logout_button = tk.Button(new_window, text="Logout", command=new_window.destroy)
	logout_button.place(x=10, y=10)
	welcome_label = tk.Label(new_window, text="Welcome, " + user + "!", font=("Arial", 16))
	welcome_label.place(x=220, y=200)


# Create the login window
def login_window():
	login_window = tk.Tk()
	login_window.geometry("400x300")
	login_window.title("DBMS Login")
	# Add labels and entry fields to the login window
	label1 = tk.Label(login_window, text="Username", font=("Arial", 14))
	label1.place(x=50, y=50)
	username_entry = tk.Entry(login_window, font=("Arial", 14))
	username_entry.place(x=50, y=80, width=300)
	label2 = tk.Label(login_window, text="Password", font=("Arial", 14))
	label2.place(x=50, y=120)
	password_entry = tk.Entry(login_window, show="*", font=("Arial", 14))
	password_entry.place(x=50, y=150, width=300)
	# Add a button to submit the login information
	login_button = tk.Button(login_window, text="Login", bg="blue", fg="white", command=lambda: login(username_entry.get(), password_entry.get()))
	login_button.place(x=150, y=220, width=100)
	login_window.mainloop()

login_window()











