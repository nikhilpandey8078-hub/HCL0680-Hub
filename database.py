import sqlite3
import csv

def connect_db():
    return sqlite3.connect("students.db")

def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            roll TEXT UNIQUE NOT NULL,
            course TEXT NOT NULL,
            email TEXT,
            phone TEXT,
            marks REAL
        )
    """)

    conn.commit()
    conn.close()

def import_dataset():
    conn = connect_db()
    cursor = conn.cursor()

    with open("students_dataset.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            cursor.execute("""
                INSERT OR IGNORE INTO students
                (name, roll, course, email, phone, marks)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                row["name"],
                row["roll"],
                row["course"],
                row["email"],
                row["phone"],
                float(row["marks"]) if row["marks"] else None
            ))

    conn.commit()
    conn.close()
    print("Dataset Imported Successfully!")

    

if __name__ == "__main__":
    create_table()
    import_dataset()
