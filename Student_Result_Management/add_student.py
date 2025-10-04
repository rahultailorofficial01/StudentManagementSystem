import sqlite3
from tkinter import *
from tkinter import messagebox

# Database connection
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Table banaye agar pehle se na ho
cursor.execute('''
    CREATE TABLE IF NOT EXISTS student (
        roll INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        marks INTEGER NOT NULL
    )
''')
conn.commit()

# Submit function
def submit():
    roll = entry_roll.get()
    name = entry_name.get()
    marks = entry_marks.get()

    if roll == "" or name == "" or marks == "":
        messagebox.showerror("Error", "All fields are required")
    else:
        try:
            cursor.execute("INSERT INTO student (roll, name, marks) VALUES (?, ?, ?)",
                           (roll, name, marks))
            conn.commit()
            messagebox.showinfo("Success", "Student added successfully")
            entry_roll.delete(0, END)
            entry_name.delete(0, END)
            entry_marks.delete(0, END)
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Roll number already exists")

# GUI
root = Tk()
root.title("Add Student")
root.geometry("300x250")

Label(root, text="Roll Number").pack()
entry_roll = Entry(root)
entry_roll.pack()

Label(root, text="Name").pack()
entry_name = Entry(root)
entry_name.pack()

Label(root, text="Marks").pack()
entry_marks = Entry(root)
entry_marks.pack()

Button(root, text="Submit", command=submit).pack(pady=10)

root.mainloop()

# Close DB when done (optional here)
# conn.close()
