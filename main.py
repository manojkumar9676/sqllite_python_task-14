import sqlite3

# Connect to database (creates file if not exists)
conn = sqlite3.connect("students.db")

# Create cursor object
cursor = conn.cursor()

print("Database connected successfully!")

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    branch TEXT
)
""")

print("Table created successfully!")

cursor.execute(
    "INSERT INTO students (name, age, branch) VALUES (?, ?, ?)",
    ("Manoj", 21, "ECE")
)

conn.commit()
print("Record inserted successfully!")


cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

print("\nStudent Records:")
for row in rows:
    print(row)



cursor.execute(
    "UPDATE students SET age = ? WHERE name = ?",
    (22, "Manoj")
)

conn.commit()
print("Record updated successfully!")


cursor.execute(
    "DELETE FROM students WHERE name = ?",
    ("Manoj",)
)

conn.commit()
print("Record deleted successfully!")


conn.close()
print("Database connection closed.")
