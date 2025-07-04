from question_model import Question
from data import questions_data
from quiz_brain import QuizBrain


question_bank = []

for q in questions_data:
    question_text = q["question"]
    question_answer = q["answer"]
    new_question = Question(q_text= question_text, q_answer= question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")