from question_model import Question
from data import questions_data

question_bank = []

for q in questions_data:
    question_text = q["question"]
    question_answer = q["answer"]
    new_question = Question(q_text= question_text, q_answer= question_answer)
    question_bank.append(new_question)


print(question_bank[2].answer)