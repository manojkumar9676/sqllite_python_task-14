📘 Student Database Management System (SQLite + Python)
📌 Project Description

This project is a simple Student Database Management System built using Python and SQLite.

It performs basic database operations like:

Connecting to SQLite database

Creating tables programmatically

Inserting records dynamically

Fetching records using SELECT queries

Updating records

Deleting records

Using parameterized queries (to prevent SQL Injection)

Properly committing and closing connections

Displaying results neatly

🛠 Technologies Used

Python 3.x

SQLite (Built-in Python module: sqlite3)

VS Code (recommended)

📂 Project Structure
sqlite_project/
│
├── main.py
├── students.db   (auto-created)
└── README.md

⚙ How to Run the Project
Step 1: Clone or Download Project

Download the folder or create it manually.

Step 2: Open Terminal in Project Folder

In VS Code:

Right Click → Open in Integrated Terminal

Step 3: Run the Program
python main.py

🧩 Features Implemented
1️⃣ Connect to Database
conn = sqlite3.connect("students.db")


Creates database file if not exists.

2️⃣ Create Table Programmatically
CREATE TABLE IF NOT EXISTS students (...)


Ensures table is created only once.

3️⃣ Insert Records (Parameterized Query)
cursor.execute(
    "INSERT INTO students (name, age, branch) VALUES (?, ?, ?)",
    (name, age, branch)
)


✅ Prevents SQL Injection
✅ Safe and secure

4️⃣ Fetch Records
SELECT * FROM students


Displays all stored student records.

5️⃣ Update Records
UPDATE students SET age = ? WHERE id = ?

6️⃣ Delete Records
DELETE FROM students WHERE id = ?

7️⃣ Commit & Close Connection
conn.commit()
conn.close()


Ensures data is saved and connection is properly closed.

🔐 Why Parameterized Queries Are Important?

Instead of:

"INSERT INTO students VALUES (" + name + ")"


We use:

"INSERT INTO students VALUES (?, ?, ?)"


This prevents SQL Injection attacks and makes the application secure.

🎯 Learning Outcomes

After completing this project, you understand:

How relational databases work

CRUD operations (Create, Read, Update, Delete)

SQL fundamentals

Secure query execution

Database connection handling

Practical Python backend concepts

🚀 Future Improvements

Add GUI using Tkinter

Convert into Web App using Flask

Add search functionality

Add login authentication

Connect to MySQL/PostgreSQL

👨‍💻 Author

Manoj
B.Tech (ECE) – 3rd Year
Learning Python & Backend Development
