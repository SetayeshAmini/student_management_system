from Student import Student
from Course import Course
from Exam import Exam
from Project import Project
from Assesment import Assesment
from Quiz import Quiz
from Gradebook import Gradebook

def main():
    manager = Gradebook(passing_grade=55)

    while True:
        print("\n ==== Student Gradebook Manager ====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Add Course")
        print("4. Enroll Student in Course")
        print("5. Add Assessment")
        print("6. Record Grade")
        print("7. View Student Report")
        print("8. Advanced Options (Attendance, Rankings, Dashboard, Delete, Search)")
        print("0. Exit")

        choice = input("Choice an option: ").strip()

        if not choice.isdigit() or not (0 <= int(choice) <= 8):
           print("Error: Invalid choice Please choose a valid option.")
           continue

        choice = int(choice)

        if choice == 0:
            print("Exiting... Goodbye!")
            break

        elif choice == 1:
            s_id = input("Enter Student ID: ").strip()
            s_name = input("Enter Student Name: ").strip()
            email = input("Enter Student Email: ").strip()
            if not s_id or not s_name or not email:
                print("Error: All fields are required.")
                continue
            manager.add_student(Student(s_id, s_name, email))

