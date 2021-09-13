class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def get_score(self):
        return self.score
    def display_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{(self.question_number)}: {question.get_text()}. (True / False)?: ")
        self.check_answer(user_answer, question.get_answer())

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, question_answer):
        if user_answer.lower() == question_answer.lower():
            print("You got it right!")
            self.score += 1
            print(f"Your current score is: {self.score}/{self.question_number}")
        else:
            print("You got it wrong.")
        self.question_number -= 1
        print(f"The correct answer was: {self.question_list[self.question_number].get_answer()}")
        self.question_number += 1



