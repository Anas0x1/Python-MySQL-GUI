
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector


def create_db():
	
	db_name = db_name_entry.get()
	
	if db_name == "":
		messagebox.showerror("ERROR!" , "Database name is required")
	else:
		conn = mysql.connector.connect(
			host ="localhost",
			user ="YOUR-USERNAME",
			passwd ="YOUR-PASSWORD"
			)
	
	
		cursorObject = conn.cursor()
		cursorObject.execute("CREATE DATABASE IF NOT EXISTS {};".format(db_name))
	
		cursorObject.close()
		conn.close()
	
		messagebox.showinfo("Congratulations" , "Database created successfully")
		print("\nQuery Executed Successfully\n###################################")
	
	
root = tk.Tk()
root.geometry("400x300")
root.title("Create Database")

#Define the third row (query)
lblfrstrow = tk.Label(root, text ="Database Name : ")
lblfrstrow.place(x = 30, y = 80)
 
db_name_entry = tk.Entry(root, width = 35)
db_name_entry.place(x = 150, y = 80, width = 150)

button = Button(root, text="Create", bg='#99b9ff' , command=create_db)
button.pack()

root.mainloop()

