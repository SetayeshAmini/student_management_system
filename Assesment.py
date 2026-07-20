class Assesment:
    def __init__(self, title, max_score):
        self.title = title
        self.max_score = max_score

    def calculate_percentage(self, score):
        if self.max_score == 0:
            return 0.0
        return (score / self.max_score) * 100

    def grade_message(self, score):
        percentage = self.calculate_percentage(score)
        if percentage >= 50:
            return f"Exam passed! result for {self.title} is {percentage:.1f}%"
        else:
            return f"Exam failed! result for {self.title} is {percentage:.1f}%"

    def display_info(self):
        print(f"{self.title} - Max score: {self.max_score}.")

