
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector


def run_query():
	
	query = query_entry.get()
	
	if query == "":
		messagebox.showerror("ERROR!" , "query field is required")
	else:
	
		conn = mysql.connector.connect(
			host ="localhost",
			user ="YOUR-USERNAME",
			passwd ="YOUR-PASSWORD",
			database ="YOUR-DATABASE"
			)
		
		cursorObject = conn.cursor()
		try:
			cursorObject.execute(query)
			if cursorObject.description is not None:
				result = cursorObject.fetchall()
				messagebox.showinfo("Query Result", result)
			else:
				conn.commit()
				messagebox.showinfo("Query Result", "Query executed successfully")
		except Exception as e:
			messagebox.showerror("Error", str(e))

    		# Close the connection
		conn.close()
		
		

root = tk.Tk()
root.geometry("750x300")
root.title("MySQL query tool")

#Define the third row (query)
lblthrdrow = tk.Label(root, text ="Query : ")
lblthrdrow.place(x = 50, y = 80)
 
query_entry = tk.Entry(root, width = 35)
query_entry.place(x = 150, y = 80, width = 550)

button = Button(root, text="Run Query", bg='#cc6600' , command=run_query)
button.pack()

root.mainloop()





#insert into nmapscan(IP,Port,Service_name,Port_status) VALUES ("127.0.0.1",80,"http","open");







