# 產生問題的 API：https://opentdb.com/

from day017_question_model import Question
from day017_data import question_data
from day017_quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    q = Question(question["text"], question["answer"])
    question_bank.append(q)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions(): # if quiz still has questions remaining
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
