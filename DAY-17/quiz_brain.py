from pickle import FALSE, TRUE


class QuizBrain:
    def __init__(self, qlist):
        self.question_number = 0
        self.question_list = qlist

    def still_hasquestion(self):
        return self.question_number < len(self.question_list)
        #     return TRUE
        # else:
        #     return FALSE

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        input(f"Q.{self.question_number}:{current_question.text} True/False")
