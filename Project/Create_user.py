
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector

def create_user():
	
	user = user_entry.get()
	passw = passw_entry.get()
	
	if user == "" or passw == "":
		messagebox.showerror("ERROR!" , "All fields are required")
	
	
	else:
		conn = mysql.connector.connect(
			host ="localhost",
			user ="YOUR-USERNAME",
			passwd ="YOUR-PASSWORD"
			)
		cursorObject = conn.cursor()
	
		cursorObject.execute("CREATE USER {}@localhost identified by '{}';".format(user,passw))
	
		conn.commit()
		conn.close()
	
		messagebox.showinfo("Registration Successful", "You are now registered in MySQL database.")

root = tk.Tk()
root.geometry("500x500")
root.title("Create user Page")

 
# Defining the first row (user)
lblfrstrow = tk.Label(root, text ="User : ", )
lblfrstrow.place(x = 50, y = 20)
 
user_entry = tk.Entry(root, width = 35)
user_entry.place(x = 150, y = 20, width = 100)

 
# Defining the second row (Password)
lblscndrow = tk.Label(root, text ="Password : " )
lblscndrow.place(x = 50, y = 50)
 
passw_entry = tk.Entry(root, width = 75)
passw_entry.place(x = 150, y = 50, width = 100)

#Defining the Registeration button
button = tk.Button(root, text ="Create", bg ='green' , command = create_user)
button.place(x = 150, y = 110, width = 100)

root.mainloop()
















