import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Database connect
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Update student function
def update_student():
    selected_item = tree.selection()
    if selected_item:
        roll_no = tree.item(selected_item)["values"][0]
        new_name = name_entry.get()
        new_marks = marks_entry.get()

        if new_name and new_marks:
            try:
                cursor.execute("UPDATE student SET Name=?, Marks=? WHERE Roll=?", (new_name, new_marks, roll_no))
                conn.commit()
                tree.item(selected_item, values=(roll_no, new_name, new_marks))
                messagebox.showinfo("Success", "Student data updated successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to update: {e}")
        else:
            messagebox.showwarning("Input Error", "Please fill both Name and Marks fields.")
    else:
        messagebox.showwarning("Selection Error", "Please select a student to update.")

# Load data to Treeview
def fetch_data():
    tree.delete(*tree.get_children())
    cursor.execute("SELECT * FROM student")
    rows = cursor.fetchall()
    for row in rows:
        tree.insert("", END, values=row)

# On row select, fill form
def on_select(event):
    selected_item = tree.selection()
    if selected_item:
        values = tree.item(selected_item)["values"]
        name_entry.delete(0, END)
        marks_entry.delete(0, END)
        name_entry.insert(0, values[1])
        marks_entry.insert(0, values[2])

# GUI setup
root = Tk()
root.title("Update Student")
root.geometry("500x500")

# Treeview
tree = ttk.Treeview(root, columns=("Roll", "Name", "Marks"), show="headings")
tree.heading("Roll", text="Roll No")
tree.column("Roll", width=100)

tree.heading("Name", text="Name")
tree.column("Name", width=150)

tree.heading("Marks", text="Marks")
tree.column("Marks", width=100)

tree.bind("<<TreeviewSelect>>", on_select)
tree.pack(pady=10, fill=BOTH, expand=True)

# Form fields
form_frame = Frame(root)
form_frame.pack(pady=10)

Label(form_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
name_entry = Entry(form_frame)
name_entry.grid(row=0, column=1, padx=5)

Label(form_frame, text="Marks:").grid(row=1, column=0, padx=5, pady=5)
marks_entry = Entry(form_frame)
marks_entry.grid(row=1, column=1, padx=5)

# Update Button
update_btn = Button(root, text="Update Student", command=update_student)
update_btn.pack(pady=10)

fetch_data()

root.mainloop()
conn.close()
