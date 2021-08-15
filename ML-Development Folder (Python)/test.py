import random
import pandas as pd
from jsonIO import pyjson

generated_questions = []

data = pyjson.read_from("./terms.json")

networks = data["networks"]
oops = data["oops"]

def generate(arr):
    questions = []

    for i in range (0, 50):
        
        qword = arr["q-words"][random.randrange(0, len(arr["q-words"]))]

        between = arr["in-betweens"][random.randrange(0, len(arr["in-betweens"]))]

        subtopic = arr["sub-topics"][random.randrange(0, len(arr["sub-topics"]))]

        while between == "what" and qword == "What is/are":
            qword = arr["q-words"][random.randrange(0, len(arr["q-words"]))]

            between = arr["in-betweens"][random.randrange(0, len(arr["in-betweens"]))]

        if between == "what":
            if subtopic[-1] != "s":
                subtopic += " is"
            else:
                subtopic += " are"

        questions.append(qword + " " + between + " " + subtopic)

        if len(questions) != len(list(set(questions))):
            questions = list(set(questions))
            i = i - 1

    for i in range (0, 30):
        q2word = arr["two-part-q-words"][random.randrange(0, len(arr["two-part-q-words"]))]

        between2 = "what"

        while (between2 == "what"):
            between2 = arr["in-betweens"][random.randrange(0, len(arr["in-betweens"]))]

        subtopic21 = arr["sub-topics"][random.randrange(0, len(arr["sub-topics"]))]

        subtopic22 = arr["sub-topics"][random.randrange(0, len(arr["sub-topics"]))]

        while subtopic21 == subtopic22:
            subtopic22 = arr["sub-topics"][random.randrange(0, len(arr["sub-topics"]))]

        if q2word == "List the advantages of using":
            questions.append(q2word + " " + subtopic21 + " and " + subtopic22)
        else:
            questions.append(q2word + " " + between2 + " " + subtopic21 + " and " + subtopic22)

        if len(questions) != len(list(set(questions))):
            questions = list(set(questions))
            i = i - 1
    
    return questions

generated_questions = generate(networks) + generate(oops)
qgenoutput = pd.DataFrame(generated_questions)

# print(qgenoutput)

    #For xlsx
    # writer = pd.ExcelWriter("qgenerated.xlsx", engine = 'xlsxwriter')
    # qgenoutput.to_excel(writer, sheet_name = "Sheet1", index = False)
    # writer.save();

    #For csv
qgenoutput.to_csv("qgenerated.csv", index = False)