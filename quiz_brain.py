class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.score = 0

    def next_question(self):
        cq=self.questions_list[self.question_number]
        self.question_number += 1
        ans = input(f"Q.{self.question_number}: {cq.text} (True/False):")
        # print(ans)
        # print(cq.answer)
        if ans.lower() == cq.answer.lower():
            self.score += 1
            print("You got it right")
        else:
            print("You got it wrong")

        print(f"The correct answer was: {cq.answer}.")

        if self.question_number < len(self.questions_list):
            print(f"Your score is: {self.score}/{self.question_number}")
            print("")
            print("")

            self.next_question()
        else:
            print(f"You've completed the quiz. your final score: {self.score}/{len(self.questions_list)}")

