import random
import pandas as pd

questions = []

networks = {"q-words": ["Identify", "Describe", "Explain", "Define", "What is/are", "State", "Outline", "Suggest"],
            "in-betweens": ["the functions of","the requirements of","the use of","what","the functionality of","the threats to","the security concerns of","the features of","the advantages of","the benefits of","the disadvantages of","the term(s)","the technology required for","the sources of risk to","the importance of", "the strengths of", "the weaknesses of"],
            "sub-topics": ["a VPN","an extranet","a wired network","a wireless network","a LAN","a WLAN","a PAN","a SAN","WPA","WEP","WPA-2","a server","a network","a router","the network topologies"],
            "two-part-q-words": ["Distinguish between","Compare and Contrast","What are the Similarities and Differences between","List the advantages of using"]};

for i in range (0, 50):
    
    qword = networks["q-words"][random.randrange(0, len(networks["q-words"]))]

    between = networks["in-betweens"][random.randrange(0, len(networks["in-betweens"]))]

    subtopic = networks["sub-topics"][random.randrange(0, len(networks["sub-topics"]))]

    while between == "what" and qword == "What is/are":
        qword = networks["q-words"][random.randrange(0, len(networks["q-words"]))]

        between = networks["in-betweens"][random.randrange(0, len(networks["in-betweens"]))]

    if between == "what":
        if subtopic.find("a ") != -1 or subtopic.find("an ") != -1:
            subtopic += " is"
        else:
            subtopic += " are"

    questions.append(qword + " " + between + " " + subtopic)

    if len(questions) != len(list(set(questions))):
        questions = list(set(questions))
        i = i - 1

for i in range (0, 30):
    q2word = networks["two-part-q-words"][random.randrange(0, len(networks["two-part-q-words"]))]

    between2 = networks["in-betweens"][random.randrange(0, len(networks["in-betweens"]))]

    subtopic21 = networks["sub-topics"][random.randrange(0, len(networks["sub-topics"]))]

    subtopic22 = networks["sub-topics"][random.randrange(0, len(networks["sub-topics"]))]

    while subtopic21 == subtopic22:
        subtopic22 = networks["sub-topics"][random.randrange(0, len(networks["sub-topics"]))]

    if q2word == "List the advantages of using":
        questions.append(q2word + " " + subtopic21 + " and " + subtopic22)
    else:
        questions.append(q2word + " " + between2 + " " + subtopic21 + " and " + subtopic22)

    if len(questions) != len(list(set(questions))):
        questions = list(set(questions))
        i = i - 1

qgenoutput = pd.DataFrame(questions)

#For xlsx
# writer = pd.ExcelWriter("qgenerated.xlsx", engine = 'xlsxwriter')
# qgenoutput.to_excel(writer, sheet_name = "Sheet1", index = False)
# writer.save();

#For csv
qgenoutput.to_csv("qgenerated.csv", index = False)