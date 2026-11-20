from database import connect_db

print("===== STUDENT MANAGEMENT SYSTEM =====")

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Student Name: ")
        roll = input("Enter Roll Number: ")
        course = input("Enter Course: ")

        conn = connect_db()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                INSERT INTO students (name, roll, course)
                VALUES (?, ?, ?)
            """, (name, roll, course))

            conn.commit()
            print("Student Added Successfully!")

        except Exception as e:
            print("Error:", e)

        finally:
            conn.close()

    elif choice == "2":
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()

        if not students:
            print("No Students Found")
        else:
            print("\n===== STUDENT DETAILS =====")

            for student in students:
                print("ID:", student[0])
                print("Name:", student[1])
                print("Roll Number:", student[2])
                print("Course:", student[3])
                print("----------------------")

        conn.close()

    elif choice == "3":
        search_roll = input("Enter Roll Number: ")

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM students WHERE roll = ?",
            (search_roll,)
        )

        student = cursor.fetchone()

        if student:
            print("Student Found!")
            print("Name:", student[1])
            print("Roll Number:", student[2])
            print("Course:", student[3])
        else:
            print("Student Not Found!")

        conn.close()

    elif choice == "4":
        delete_roll = input("Enter Roll Number to Delete: ")

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM students WHERE roll = ?",
            (delete_roll,)
        )

        conn.commit()

        if cursor.rowcount > 0:
            print("Student Deleted Successfully!")
        else:
            print("Student Not Found!")

        conn.close()

    elif choice == "5":
        update_roll = input("Enter Roll Number to Update: ")
        new_name = input("Enter New Name: ")
        new_course = input("Enter New Course: ")

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE students
            SET name = ?, course = ?
            WHERE roll = ?
        """, (new_name, new_course, update_roll))

        conn.commit()

        if cursor.rowcount > 0:
            print("Student Updated Successfully!")
        else:
            print("Student Not Found!")

        conn.close()

    elif choice == "6":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid Choice!")