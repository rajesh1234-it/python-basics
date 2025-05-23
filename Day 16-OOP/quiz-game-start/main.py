from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# print(question_bank[1].text)


quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
# question_book = []
# for quest in question_data:
#     quest_txt = quest["text"]
#     quest_ans = quest["answer"]
#     new_q = Question(quest_txt, quest_ans)
#     question_book.append(new_q)
