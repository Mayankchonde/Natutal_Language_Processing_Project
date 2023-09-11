# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 16:07:42 2023

@author: mayan_izchdl9
"""

import re
import textstat

def calculate_avg_words_per_sentence(text):
    # split the text into sentences
    sentences = re.split('[.!?]', text)

    # count the total number of words and sentences
    total_words = 0
    total_sentences = 0
    for sentence in sentences:
        words = sentence.split()
        total_words += len(words)
        total_sentences += 1

    # calculate the average number of words per sentence
    avg_words_per_sentence = total_words / total_sentences

    return avg_words_per_sentence


for i in text:
    avg_words_per_sentence = calculate_avg_words_per_sentence(i)
    print(avg_words_per_sentence)
    

