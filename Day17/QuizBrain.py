class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = input("Q." + str(self.question_number) + " " + current_question.text
                      + ". (True/False)")
        self.question_number += 1
        self.check_answer(user_answer, current_question)


    def has_next_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, current_question):
        if user_answer.lower() == current_question.answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {current_question.answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
