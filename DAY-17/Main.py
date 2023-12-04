from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []  # List of question objects
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
# print(question_bank[0].answer)
quiz = QuizBrain(question_bank)
while quiz.still_hasquestion:
    quiz.next_question()
print("You have completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number}")
