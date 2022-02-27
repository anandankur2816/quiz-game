from question_model import  Question
from  data import question_data
from quiz_brain import  QuizBrain

question_bank = []
# print(question_bank)
for i in question_data:
    nq = Question(i["text"], i["answer"])
    question_bank.append(nq)
# print(question_bank)

quiz_brain=QuizBrain(question_bank)
quiz_brain.next_question()
