import sqlite3
from tkinter import *
from tkinter import ttk

# Database connect
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Fetch data
def fetch_data():
    cursor.execute("SELECT * FROM student")
    rows = cursor.fetchall()
    for row in rows:
        tree.insert("", END, values=row)

# GUI
root = Tk()
root.title("View Students")
root.geometry("400x300")

# Treeview Table
tree = ttk.Treeview(root, columns=("Roll", "Name", "Marks"), show="headings")
tree.heading("Roll", text="Roll No")
tree.column("Roll", width=100)

tree.heading("Name", text="Name")
tree.column("Name", width=200)

tree.heading("Marks", text="Marks")
tree.column("Marks", width=100)

tree.pack(fill=BOTH, expand=True)

fetch_data()

root.mainloop()
