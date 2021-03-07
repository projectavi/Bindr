from jsonIO import pyjson
import pandas as pd
import random as rand
#from google.cloud import firestore

df = pd.read_excel("./src/model/engine/spreadsheetsTemp/testCSquestions.xlsx")

terms = df["Terms"].values.tolist()
definitions = df["Definitions"].values.tolist()

questions = []
x_old = -1

for i in range(0, 5):
    x = []
    while len(x) < 4:
        x = [rand.randint(0, len(definitions)-1), rand.randint(0, len(definitions)-1),
        rand.randint(0, len(definitions)-1), rand.randint(0, len(definitions)-1)]
        x = list(set(x))

    index = rand.randint(0, 3)
    while x[index] == x_old:
        index = rand.randint(0, 3)
    if (index == 0): letter = "a"
    elif (index == 1): letter = "b"
    elif (index == 2): letter = "c"
    elif (index == 3): letter = "d"

    choice = rand.randint(0, 9)
    
    if (choice % 2 == 0):
        mcq = {"type": "mcq", "question": "Question " + str(i+1) + ": " + terms[x[index]].capitalize(), 
        "answers": {"a": definitions[x[0]].capitalize(), "b": definitions[x[1]].capitalize(), 
        "c": definitions[x[2]].capitalize(), "d": definitions[x[3]].capitalize()}, 
        "correctAnswer": letter}
    else:
        mcq = {"type": "mcq", "question": "Question " + str(i+1) + ": " + definitions[x[index]].capitalize(), 
        "answers": {"a": terms[x[0]].capitalize(), "b": terms[x[1]].capitalize(), 
        "c": terms[x[2]].capitalize(), "d": terms[x[3]].capitalize()}, 
        "correctAnswer": letter}

    x_old = x[index]

    questions.append(mcq)

for i in range(0, 5):
    x = rand.randint(0, len(terms)-1)

    choice = rand.randint(0, 9)

    if choice % 2 == 0:
        short = {"type": "short", "question": "Question " + str(6+i) + ": Define " + terms[x], 
        "correctAnswer": definitions[x]}
    else:
        short = {"type": "short", "question": "Question " + str(6+i) + ": What term does this define -> " + definitions[x], 
        "correctAnswer": terms[x]}

    questions.append(short)

#Structure of questions
"""
#For MCQ
{
    "type": "mcq",
    "question": "Question 1",
    "answers": {
          "a": "Answer 1",
          "b": "Answer 2",
          "c": "Answer 3"
        },
    "correctAnswer": "c"
}

#For Short Answer
{
    "type": "short",
    "question": "Question 4",
    "correctAnswer": "TestAnswer"
}

#For Long Answer
{
    "type": "long",
    "question": "Question 6",
    "correctAnswer": "Test",
}
"""

# mcq_questions = [{"type": "mcq",
#     "question": "Question " + str(y[0]),
#     "answers": {
#           "a": "Answer 1",
#           "b": "Answer 2",
#           "c": "Answer 3"
#         },
#     "correctAnswer": "c"}, {"type": "mcq",
#     "question": "Question " + str(y[1]),
#     "answers": {
#           "a": "Answer 1",
#           "b": "Answer 2",
#           "c": "Answer 3"
#         },
#     "correctAnswer": "c"}, {"type": "mcq",
#     "question": "Question " + str(y[2]),
#     "answers": {
#           "a": "Answer 1",
#           "b": "Answer 2",
#           "c": "Answer 3"
#         },
#     "correctAnswer": "c"}]



pyjson.write_to(questions, "./src/view/js/json/questions.json")