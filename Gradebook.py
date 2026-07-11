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
           print(f"Student {student_id} enrolled in course {course_code}.")
       else:
           print("Error: student or course not found")

    def add_assessment(self, assessment, course_code):
        if course_code in self.courses:
            self.courses[course_code].assessments.append(assessment)
            print(f"Assessment {assessment.title} added to course {course_code}.")
        else:
            print("Error: course not found.")

    def record_grade(self, student_id, course_code, assessment_title, score):
        if student_id in self.grades and course_code in self.grades[student_id]:
            course = self.courses[course_code]
            valid_titles = [asm.title for asm in course.assessments]

            if assessment_title in valid_titles:
                self.grades[student_id][course_code][assessment_title] = score
                print(f"Grade {score} recorded for {assessment_title} in course {course_code}.")
            else:
                print("Error: This assessment is not defined for this course.")
        else:
            print("Error: Invalid student or course enrollment.")

    def calculate_average(self, student_id, course_code):
        if student_id in self.grades and course_code in self.grades[student_id]:
            student_course_grades = self.grades[student_id][course_code]
            if not student_course_grades:
                return 0
            total = sum(student_course_grades.values())
            count = len(student_course_grades)
            return total / count
        return 0

    def get_result(self, average):
        if average >= self.passing_grade:
            return "Pass"
        return "Fail"

    def search_students(self, keyword):
        found_students = []
        for student_id, student in self.students.items():
            if keyword.lower() in student_id.lower() or keyword.lower() in student.name.lower():
                found_students.append(student)
        return found_students

    def delete_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            if student_id in self.grades:
                del self.grades[student_id]
            print(f"Student {student_id} has successfully deleted.")
        else:
            print(f"Error: student with id {student_id} does not exist.")