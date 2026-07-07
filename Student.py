import re


class Student:
    def __init__(self, student_id, name, email):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.courses = []

    def get_id(self):
        return self.student_id

    def get_name(self):
        return self.name

    def set_email(self, email):
        email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if re.match(email_pattern, email):
            self.email = email
            print(f"Email successfully set as {self.email}")
        else:
            print(f"Error: Email address not valid")

    def enroll_course(self, course_code):
        if course_code not in self.courses:
            self.courses.append(course_code)
            print(f"successfully enrolled in course {course_code}")
        else:
            print(f"already enrolled in course {course_code}")

    def display_info(self):
        print("\n---- Student Information----")
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Enrolled course: {self.courses}")
        print("--------------------------------")
