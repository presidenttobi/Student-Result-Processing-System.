import sqlite3

connection = sqlite3.connect("SchoolResults.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Students (
    StudentID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    Class TEXT NOT NULL,
    Mathematics REAL NOT NULL,
    English REAL NOT NULL,
    ComputerScience REAL NOT NULL
)
""")

connection.commit()


def add_student():
    print("\n--- ADD NEW STUDENT ---")

    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    student_class = input("Enter class: ")
    mathematics = float(input("Enter Mathematics score: "))
    english = float(input("Enter English score: "))
    computer_science = float(input("Enter Computer Science score: "))

    cursor.execute("""
    INSERT INTO Students
    (FirstName, LastName, Class, Mathematics, English, ComputerScience)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (
        first_name,
        last_name,
        student_class,
        mathematics,
        english,
        computer_science
    ))

    connection.commit()

    print("Student record saved successfully!")


def view_students():
    print("\n--- ALL STUDENTS ---")

    cursor.execute("SELECT * FROM Students")
    students = cursor.fetchall()

    if not students:
        print("No student records found.")
        return

    for student in students:
        student_id, first_name, last_name, student_class, mathematics, english, computer_science = student

        total = mathematics + english + computer_science
        average = total / 3

        print("\nStudent ID:", student_id)
        print("Full Name:", first_name, last_name)
        print("Class:", student_class)
        print("Mathematics:", mathematics)
        print("English:", english)
        print("Computer Science:", computer_science)
        print("Total Score:", total)
        print("Average Score:", round(average, 2))


def search_student():
    print("\n--- SEARCH STUDENT ---")

    student_id = int(input("Enter StudentID: "))

    cursor.execute(
        "SELECT * FROM Students WHERE StudentID = ?",
        (student_id,)
    )

    student = cursor.fetchone()

    if student is None:
        print("Student does not exist.")
        return

    student_id, first_name, last_name, student_class, mathematics, english, computer_science = student

    total = mathematics + english + computer_science
    average = total / 3

    print("\nStudent ID:", student_id)
    print("Full Name:", first_name, last_name)
    print("Class:", student_class)
    print("Mathematics:", mathematics)
    print("English:", english)
    print("Computer Science:", computer_science)
    print("Total Score:", total)
    print("Average Score:", round(average, 2))


def update_student():
    print("\n--- UPDATE STUDENT ---")

    view_students()

    student_id = int(input("\nEnter StudentID to update: "))

    cursor.execute(
        "SELECT * FROM Students WHERE StudentID = ?",
        (student_id,)
    )

    student = cursor.fetchone()

    if student is None:
        print("Student does not exist.")
        return

    print("\nWhat would you like to change?")
    print("1. First Name")
    print("2. Last Name")
    print("3. Class")
    print("4. Mathematics Score")
    print("5. English Score")
    print("6. Computer Science Score")

    choice = input("Choose an option: ")

    if choice == "1":
        new_value = input("Enter new first name: ")
        cursor.execute(
            "UPDATE Students SET FirstName = ? WHERE StudentID = ?",
            (new_value, student_id)
        )

    elif choice == "2":
        new_value = input("Enter new last name: ")
        cursor.execute(
            "UPDATE Students SET LastName = ? WHERE StudentID = ?",
            (new_value, student_id)
        )

    elif choice == "3":
        new_value = input("Enter new class: ")
        cursor.execute(
            "UPDATE Students SET Class = ? WHERE StudentID = ?",
            (new_value, student_id)
        )

    elif choice == "4":
        new_value = float(input("Enter new Mathematics score: "))
        cursor.execute(
            "UPDATE Students SET Mathematics = ? WHERE StudentID = ?",
            (new_value, student_id)
        )

    elif choice == "5":
        new_value = float(input("Enter new English score: "))
        cursor.execute(
            "UPDATE Students SET English = ? WHERE StudentID = ?",
            (new_value, student_id)
        )

    elif choice == "6":
        new_value = float(input("Enter new Computer Science score: "))
        cursor.execute(
            "UPDATE Students SET ComputerScience = ? WHERE StudentID = ?",
            (new_value, student_id)
        )

    else:
        print("Invalid option.")
        return

    connection.commit()

    print("Student record updated successfully!")


def delete_student():
    print("\n--- DELETE STUDENT ---")

    view_students()

    student_id = int(input("\nEnter StudentID to delete: "))

    cursor.execute(
        "SELECT * FROM Students WHERE StudentID = ?",
        (student_id,)
    )

    student = cursor.fetchone()

    if student is None:
        print("Student does not exist.")
        return

    print("\nStudent found:")
    print("Student ID:", student[0])
    print("Name:", student[1], student[2])
    print("Class:", student[3])

    confirmation = input("Are you sure you want to delete this student? (yes/no): ")

    if confirmation.lower() == "yes":
        cursor.execute(
            "DELETE FROM Students WHERE StudentID = ?",
            (student_id,)
        )

        connection.commit()

        print("Student deleted successfully!")

    else:
        print("Deletion cancelled.")


while True:
    print("\n==============================")
    print("STUDENT RESULT PROCESSING SYSTEM")
    print("==============================")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank you for using the Student Result Processing System!")
        break

    else:
        print("Invalid option. Please try again.")


connection.close()