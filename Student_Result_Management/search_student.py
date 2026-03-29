import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Database connection
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Search function
def search_student():
    keyword = search_entry.get().strip()
    tree.delete(*tree.get_children())  # Clear old results

    if keyword:
        query = "SELECT * FROM student WHERE Roll LIKE ? OR Name LIKE ?"
        cursor.execute(query, ('%' + keyword + '%', '%' + keyword + '%'))
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                tree.insert("", END, values=row)
        else:
            messagebox.showinfo("Not Found", "No student found with given keyword.")
    else:
        messagebox.showwarning("Input Error", "Please enter Roll No or Name to search.")

# GUI setup
root = Tk()
root.title("Search Student")
root.geometry("500x450")

# Search Entry
Label(root, text="Enter Roll No or Name:").pack(pady=10)
search_entry = Entry(root, width=40)
search_entry.pack(pady=5)

search_button = Button(root, text="Search", command=search_student)
search_button.pack(pady=5)

# Treeview
tree = ttk.Treeview(root, columns=("Roll", "Name", "Marks"), show="headings")
tree.heading("Roll", text="Roll No")
tree.column("Roll", width=100)

tree.heading("Name", text="Name")
tree.column("Name", width=200)

tree.heading("Marks", text="Marks")
tree.column("Marks", width=100)

tree.pack(pady=10, fill=BOTH, expand=True)

root.mainloop()
conn.close()
