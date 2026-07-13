class Gradebook:
    def __init__(self, passing_grade=55):
        self.passing_grade = passing_grade
        self.students = {}
        self.courses = {}
        self.grades = {}
        self.attendance = {}

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
            self.courses[course_code].add_assessment(assessment)
            print(f"Assessment {assessment.title} added to course {course_code}.")
        else:
            print("Error: course not found.")

    def record_grade(self, student_id, course_code, assessment_title, score):
        if student_id in self.grades and course_code in self.grades[student_id]:
            course = self.courses[course_code]
            assessment = course.find_assessment(assessment_title)

            if assessment:
               if score < 0 or score > assessment.max_score:
                   print(f"Error: Score most be between 0 and {assessment.max_score}")
                   return
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
            course = self.courses.get(course_code)
            count = 0
            total_average = 0

            for exam_title, score in student_course_grades.items():
                assesment = course.find_assessment(exam_title) if course else None

                if assesment:
                    total_average += assesment.calculate_average(score)
                else:
                    total_average += (score / 100) * 100
                count += 1
            return total_average / count if count > 0 else 0
        return 0
    def get_result(self, average):
        if average >= self.passing_grade:
            return "Pass"
        return "Fail"

    def get_letter_grade(self, percentage):
        if percentage >= 95:
            return "Grade: A+"
        elif percentage >= 80:
            return "Grade: A"
        elif percentage >= 70:
            return "Grade: B"
        elif percentage >= 50:
            return "Grade: C"
        else:
            return "Needs more practice"

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

    def show_report(self, student_id):
        if student_id not in self.students:
            print("Error: student not found.")
            return
        student = self.students[student_id]
        print("==== Student Report ====")
        print(f"Student ID: {student_id}")
        print(f"Name: {student.name}")
        print(f"Email: {student.email}")

        if student_id not in self.grades or not self.grades[student_id]:
            print("No course enrollments or grades recorded for this student.")
            return

        for course_code, assessment in self.grades[student_id].items():
            course = self.courses.get(course_code)
            print(f"Course:{course_code} - {course.course_name}")

            if student_id in self.attendance and course.course_code in self.attendance[student_id]:
                records = self.attendance[student_id][course.course_code]
                p_count = list(records.values()).count("Present")
                a_count = list(records.values()).count("Absent")
                print(f"Present:{p_count} Absent:{a_count}")

            print("Grades:")
            total_percentage = 0
            count = 0
            for exam_title, score in assessment.items():
                assessment = course.find_assessment(exam_title)
                if assessment:
                    percentage = assessment.calcute_percentage(score)
                    max_score = assessment.max_score
                else:
                    max_score = 100
                    percentage = (score / max_score) * 100
                total_percentage += percentage
                count += 1

                print(f"{exam_title}: {int(score)}/{int(max_score)} = {int(percentage)}%")

                if assessment:
                    msg = assessment.grade_message(score)
                    print(f"Comment: {msg}")
            avg = total_percentage / count if count > 0 else 0
            result = self.get_result(avg)
            print(f"Average: {avg:2f}%")
            print(f"Result: {result}")

    def show_dashboard(self):
        print("==== Dashboard ====")
        print(f"Total Students Registered: {len(self.students)}")
        print("Total Courses: {len(self.courses)}")
        total_assessments = 0
        for course in self.courses.values():
            total_assessments += len(course.assessments)
        print(f"Total Assessments: {total_assessments}")

    def show_ranking(self, course_code):
        if course_code not in self.courses:
            print("Error: course not found.")
            return
        print(f"==== Ranking for course {course_code} ====")
        rank_list = []
        for student_id in self.students:
            if student_id in self.grades and course_code in self.grades[student_id]:
                avg = self.calculate_average(student_id, course_code)
                student_name = self.students[student_id].name
                rank_list.append([student_name, avg])
        rank_list.sort(key=lambda x: x[1], reverse=True)
        if not rank_list:
            print("No student ranked for this course yet.")
            return
        for rank, (name, avg) in enumerate(rank_list, start=1):
            letter = self.get_letter_grade(avg)
            print(f"{rank}. {name} | Average:{avg:.2f}%  ({letter})")

    def record_attendance(self, student_id, course_code, date, status):
        if student_id not in self.students or course_code not in self.courses:
            print("Error: course not found.")
            return
        status = status.capitalize()
        if status not in ["Present", "Absent"]:
            print("Error: status must be 'Present' or 'Absent'")
            return
        if student_id not in self.attendance:
            self.attendance[student_id] = {}
        if course_code not in self.attendance[student_id]:
            self.attendance[student_id][course_code] = {}

        self.attendance[student_id][course_code][date] = status
        print(f" '{status}' recorded for {student_id} on {date}. ")


