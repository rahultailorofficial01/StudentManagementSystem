import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Database connect
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Fetch data function
def fetch_data():
    cursor.execute("SELECT * FROM student")
    rows = cursor.fetchall()
    for row in rows:
        tree.insert("", END, values=row)

# Delete student function
def delete_student():
    selected_item = tree.selection()
    if selected_item:
        roll_no = tree.item(selected_item)["values"][0]
        print(f"Deleting student with Roll No: {roll_no}")  # Debugging line
        cursor.execute("DELETE FROM student WHERE Roll=?", (roll_no,))
        conn.commit()
        tree.delete(selected_item)
        messagebox.showinfo("Success", f"Student with Roll No {roll_no} has been deleted.")
    else:
        messagebox.showwarning("Selection Error", "Please select a student to delete.")



# GUI setup
root = Tk()
root.title("View Students")
root.geometry("500x400")

# Treeview Table
tree = ttk.Treeview(root, columns=("Roll", "Name", "Marks"), show="headings")
tree.heading("Roll", text="Roll No")
tree.column("Roll", width=100)

tree.heading("Name", text="Name")
tree.column("Name", width=200)

tree.heading("Marks", text="Marks")
tree.column("Marks", width=100)

tree.pack(fill=BOTH, expand=True)

# Delete Button
delete_button = Button(root, text="Delete Selected Student", command=delete_student)
delete_button.pack(pady=10)

fetch_data()

root.mainloop()

conn.close()
