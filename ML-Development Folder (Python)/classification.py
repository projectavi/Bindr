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

model = tf.keras.models.load_model('model.h5')

model.summary();

df = pd.read_csv("test.csv")

questions = np.array(df["Questions"].tolist())

print(questions)

# Convert sentences to sequences
MAX_VOCAB_SIZE = 20000
tokenizer = Tokenizer(num_words=MAX_VOCAB_SIZE)
tokenizer.fit_on_texts(questions)
input = tokenizer.texts_to_sequences(questions)

word2idx = tokenizer.word_index
V = len(word2idx)

input = pad_sequences(input)

T=17

input = pad_sequences(input, maxlen=T)

results = model.predict(input)

# Round each value in results
results = np.round(results)

# Get the indices of all the 1s in results
indices = []

for i in range(0, len(results)):
    if results[i] == 1: 
        indices.append(i)

for index in indices:
    print(questions[index])