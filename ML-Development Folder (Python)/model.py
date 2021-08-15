import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Dense, Input, GlobalMaxPooling1D
from tensorflow.keras.layers import LSTM, Embedding
from tensorflow.keras.models import Model

df = pd.read_csv("marked.csv")

questions = np.array(df["Questions"].tolist())
classifications = np.array(df["Classifications"].tolist())

print("")

print(type(questions))

print(type(classifications))

q_train, q_test, c_train, c_test = train_test_split(questions, classifications, test_size=0.3)

# Convert sentences to sequences
MAX_VOCAB_SIZE = 20000
tokenizer = Tokenizer(num_words=MAX_VOCAB_SIZE)
tokenizer.fit_on_texts(q_train)
sequences_train = tokenizer.texts_to_sequences(q_train)
sequences_test = tokenizer.texts_to_sequences(q_test)

word2idx = tokenizer.word_index
V = len(word2idx)
print('Found %s unique tokens.' % V)

# pad sequences so that we get a N x T matrix
data_train = pad_sequences(sequences_train)
print('Shape of data train tensor:', data_train.shape)

# get sequence length
T = data_train.shape[1]

print(T)

to_save = np.array([T])
np.save("maxlen.npy", to_save)

data_test = pad_sequences(sequences_test, maxlen=T)
print('Shape of data test tensor:', data_test.shape)

# Create the model

# We get to choose embedding dimensionality
D = 40

# Hidden state dimensionality
M = 25

# Note: we actually want to the size of the embedding to (V + 1) x D,
# because the first index starts from 1 and not 0.
# Thus, if the final index of the embedding matrix is V,
# then it actually must have size V + 1.

i = Input(shape=(T,))
x = Embedding(V + 1, D)(i)
x = LSTM(M, return_sequences=True)(x)
x = GlobalMaxPooling1D()(x)
x = Dense(1, activation='sigmoid')(x)

model = Model(i, x)

# Compile and fit
model.compile(
  loss='binary_crossentropy',
  optimizer='adam',
  metrics=['accuracy']
)

# Change the learning rate to 0.01
model.optimizer.lr.assign(0.015)

print('Training model...')
r = model.fit(
  data_train,
  c_train,
  epochs=100,
  validation_data=(data_test, c_test)
)

# Plot loss per iteration
plt.plot(r.history['loss'], label='loss')
plt.plot(r.history['val_loss'], label='val_loss')
plt.legend()
plt.show()

# Plot accuracy per iteration
plt.plot(r.history['accuracy'], label='acc')
plt.plot(r.history['val_accuracy'], label='val_acc')
plt.legend()
plt.show()

# Save model to file
model.save("model.h5")