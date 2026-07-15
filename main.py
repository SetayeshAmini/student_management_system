from Student import Student
from Course import Course
from Exam import Exam
from Project import Project
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
        print("8. Advanced Options (Attendance, Rankings, Dashboard, Update/Delete, Search)")
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

        elif choice == 2:
            manager.view_students()

        elif choice == 3:
            c_code = input("Enter Course Code: ").strip()
            c_name = input("Enter Course Name: ").strip()
            if not c_code or not c_name:
                print("Error: All fields are required.")
                continue
            manager.add_course(Course(c_code, c_name))

        elif choice == 4:
            s_id = input("Enter Student ID: ").strip()
            c_code = input("Enter Course Code: ").strip()
            manager.enroll_student(s_id, c_code)

        elif choice == 5:
            c_code = input("Enter Course Code: ").strip()
            if c_code not in manager.courses:
                print("Error: Course not found.")
                continue
            print("Type: 1. Exam | 2. Project | 3. Quiz")
            type = input("Select type: ").strip()
            title = input("Enter Assignment Title: ").strip()
            try:
                max_score = int(input("Enter max score: "))
            except ValueError:
                print("Error: max score must be an integer.")
                continue


            if type == "1": ass = Exam(title, max_score)
            elif type == "2": ass = Project(title, max_score)
            elif type == "3": ass = Quiz(title, max_score)
            else:
                print("Error: Invalid type .")
                continue
            manager.add_assessment(ass, c_code)

        elif choice == 6:
            s_id = input("Enter Student ID: ").strip()
            c_code = input("Enter Course Code: ").strip()
            title = input("Enter Assessment Title: ").strip()
            try:
                score = float(input("Enter score: "))

            except ValueError:
                print("Error: score must be number.")
                continue
            manager.record_grade(s_id, c_code, title, score)

        elif choice == 7:
            s_id = input("Enter Student ID: ").strip()
            manager.show_report(s_id)

        elif choice == 8:
            print("\n ====Advanced Options ====")
            print("1. Record Attendance")
            print("2. View Course Rankings")
            print("3. View System Dashboard")
            print("4. Search Students")
            print("5. Update Student ")
            print("6. Delete Student")
            sub_choice = input("Choice an option: ").strip()
            if sub_choice == "1":
                s_id = input("Enter Student ID: ").strip()
                c_code = input("Enter Course Code: ").strip()
                date = input("Enter Date (YYYY-MM-DD): ").strip()
                status = input("Enter status: ").strip()
                manager.record_attendance(s_id, c_code, date, status)
            elif sub_choice == "2":
                c_code = input("Enter Course Code: ").strip()
                manager.show_ranking(c_code)
            elif sub_choice == "3":
                manager.show_dashboard()
            elif sub_choice == "4":
                keyword = input("Enter Keyword: ").strip()
                result = manager.search_students(keyword)
                for s in result: print(f"ID: {s.student_id} | Name: {s.name} | Email: {s.email}")
            elif sub_choice == "5":
                s_id = input("Enter Student ID: ").strip()
                s_name = input("Enter New Name: ").strip()
                email = input("Enter New Email: ").strip()
                manager.update_student(s_id, s_name if s_name else None, email if email else None)
            elif sub_choice == "6":
                s_id = input("Enter Student ID: ").strip()
                manager.delete_student(s_id)
            else:
                print("Error: Invalid choice.")

if __name__ == "__main__":
    main()