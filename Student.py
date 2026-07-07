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

