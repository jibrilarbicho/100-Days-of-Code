from pickle import FALSE, TRUE


class QuizBrain:
    def __init__(self, qlist):
        self.question_number = 0
        self.question_list = qlist
        self.score = 0

    def still_hasquestion(self):
        return self.question_number < len(self.question_list)
        #     return TRUE
        # else:
        #     return FALSE

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}:{current_question.text} True/False")
        self.check_answer(answer, current_question.answer)

    def check_answer(self, answer, correct):
        if answer.lower() == correct.lower():
            print("Tou got it that is right")
            self.score += 1
        else:
            print("That's Wrong")
        print(f"the correct answer was {correct}")
        print(f"Your Current score is {self.score}/{self.question_number}")
        print("\n")
