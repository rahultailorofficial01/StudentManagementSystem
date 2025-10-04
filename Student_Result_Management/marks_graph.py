import sqlite3
import matplotlib.pyplot as plt

# Connect to DB
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Fetch data
cursor.execute("SELECT Roll, Marks FROM student")
data = cursor.fetchall()

# Separate Roll and Marks
roll_nos = [str(row[0]) for row in data]
marks = [row[1] for row in data]

# Plotting the graph
plt.figure(figsize=(10, 6))
plt.bar(roll_nos, marks, color='skyblue')
plt.xlabel("Roll No")
plt.ylabel("Marks")
plt.title("Student Marks Analysis")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

conn.close()
