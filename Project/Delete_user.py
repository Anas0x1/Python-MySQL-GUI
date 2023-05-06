
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector


def delete_user():
	
	user = user_entry.get()
	
	if user == "":
		messagebox.showerror("ERROR!" , "Username and host are required")
	else:
		conn = mysql.connector.connect(
			host ="localhost",
			user ="YOUR-USERNAME",
			passwd ="YOUR-PASSWORD"
			)
	
	
		cursorObject = conn.cursor()
		cursorObject.execute("DROP USER {}@localhost;".format(user))
	
		cursorObject.close()
		conn.close()
	
		messagebox.showinfo("Congratulations" , "Username deleted successfully")
		print("\nQuery Executed Successfully\n###################################")
	
	
root = tk.Tk()
root.geometry("400x300")
root.title("Delete User")

#Define the first row (user)
lblfrstrow = tk.Label(root, text ="Username : ")
lblfrstrow.place(x = 30, y = 80)
 
user_entry = tk.Entry(root, width = 35)
user_entry.place(x = 150, y = 80, width = 150)


#Defining delete button
button = Button(root, text="Delete", bg='#867979' , command=delete_user)
button.pack()

root.mainloop()

