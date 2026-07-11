class Gradebook:
    def __init__(self, passing_grade=55):
        self.passing_grade = passing_grade

        self.students = {}

        self.courses = {}

        self.grades = {}

    def add_student(self, student):
        self.students[student.student_id] = student

    def add_course(self, course):
        self.courses[course.course_code] = course

    def enroll_student(self, student_id, course_code):
       if student_id in self.students and course_code in self.courses:
           if student_id not in self.grades:
              self.grades[student_id] = {}
           if course_code not in self.grades[student_id]:
             self.grades[student_id][course_code] = {}
           print(f"Student {student_id} enrolled in course {course_code}")
       else:
           print("Error: student or course not found")

