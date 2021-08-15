import random
import pandas as pd
from jsonIO import pyjson

import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Dense, Input, GlobalMaxPooling1D
from tensorflow.keras.layers import LSTM, Embedding
from tensorflow.keras.models import Model

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

generatedQuestions = []

for topic in data:
    generatedQuestions = generatedQuestions + generate(data[topic])

model = tf.keras.models.load_model('model.h5')

model.summary();

generatedQuestions = np.array(generatedQuestions)

# Convert sentences to sequences
MAX_VOCAB_SIZE = 20000
tokenizer = Tokenizer(num_words=MAX_VOCAB_SIZE)
tokenizer.fit_on_texts(generatedQuestions)
input = tokenizer.texts_to_sequences(generatedQuestions)

word2idx = tokenizer.word_index
V = len(word2idx)

input = pad_sequences(input)

maxlen = list(np.load("maxlen.npy"))

T=maxlen[0]

input = pad_sequences(input, maxlen=T)

results = model.predict(input)

# Round each value in results
results = np.round(results)

# Get the indices of all the 1s in results
indices = []

for i in range(0, len(results)):
    if results[i] == 1: 
        indices.append(i)

classifiedQuestions = []

for index in indices:
    classifiedQuestions.append(generatedQuestions[index])

print(classifiedQuestions)