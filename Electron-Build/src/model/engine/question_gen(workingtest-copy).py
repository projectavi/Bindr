from jsonIO import pyjson

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

mcq = {
    "type": "mcq",
    "question": "Question 1",
    "answers": {
          "a": "Answer 1",
          "b": "Answer 2",
          "c": "Answer 3"
        },
    "correctAnswer": "c"
}

print(mcq)

pyjson.write_to(mcq, "mcq.json")