
# Author = Niraj Dev Pandey


import re
from nltk.tokenize import word_tokenize
from keras.preprocessing.sequence import pad_sequences
import numpy as np


def lib_check(): 
    import tensorflow as tf
    if (tf.__version__) != '1.2.0':
        print("you must need tensorflow 1.2.0 to use this project")
        print("you are running on tensorflow {} version".format(tf.__version__))
    import numpy as np
    if (np.__version__) != '1.13.0':
        print("you must need numpy 1.13.0 to use this project")
        print("you are running on numpy {} version".format(np.__version__))
    import keras
    if (keras.__version__) != '2.0.2':
        print("you must need keras 2.0.2 to use this project")
        print("you are running on keras {} version".format(keras.__version__))
    else:
        print("congratulations...! you already have all the correct dependencies installed")

lib_check() 



def tokenize(sentence):
    return word_tokenize(sentence)


def vectorize_ques(data, word_id, test_max_length, ques_max_length):
    X = []
    Xq = []
    for subtext, question in data:
        x = [word_id[w] for w in subtext]
        xq = [word_id[w] for w in question]
        # let's not forget that index 0 is reserved
        X.append(x)
        Xq.append(xq)
    return (pad_sequences(X, maxlen=test_max_length),
            pad_sequences(Xq, maxlen=ques_max_length))


# Y: array[] of zero's with "1" corresponding to word representing correct answer
def vectorize_text(data, word_id, text_max_length, ques_max_length):
    X = []
    Xq = []
    Y = []
    for subtext, question, answer in data:
        x = [word_id[w] for w in subtext]
        # Save the ID of Questions using SubText
        xq = [word_id[w] for w in question]
        # Save the answers for the Questions in "Y" as "1"
        y = np.zeros(len(word_id) + 1)
        y[word_id[answer]] = 1
        X.append(x)
        Xq.append(xq)
        Y.append(y)
    return (pad_sequences(X, maxlen=text_max_length),
            pad_sequences(Xq, maxlen=ques_max_length),
            np.array(Y))



def read_text():
    text = []
    input_line = input('Story, leave blank to stop: ')
    while input_line != '':

        if not input_line.endswith('.'):
            input_line += '.'
        text.extend(tokenize(input_line))
        input_line = input('Tell me a Story:')
        
    return text

