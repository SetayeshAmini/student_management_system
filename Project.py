from Assesment import Assesment
class Project(Assesment):

    def __init__(self, title, max_score):
        super().__init__(title, max_score)

    def display_info(self):
        print(f"Project: {self.title} - Max Score: {self.max_score}")

    def grade_message(self, score):
        percentage = self.calculate_percentage(score)
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