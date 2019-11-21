
# coding: utf-8


import nbimporter
from text_processing import *
from train import memoryNetwork
import numpy as np


memory_network = memoryNetwork()
print('Use this Vocabulary to form Questions:\n' + ' , '.join(memory_network.word_id.keys()))
print("Remember, first letter of any name must be in Capital letters along with first letter of the question")

while True:
    story = read_text()
    print('Story: ' + ' '.join(story))
    question = input('ask me anything now:')
    if question == 'done' or question == 'exit':
        break
    story_vector, query_vector = vectorize_ques([(story, tokenize(question))],
                                                  memory_network.word_id, 68, 4)
    prediction = memory_network.model.predict([np.array(story_vector), np.array(query_vector)])
    prediction_word_index = np.argmax(prediction)
    for word, index in memory_network.word_id.items():
        if index == prediction_word_index:
            print('Answer: ',word)

