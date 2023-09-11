import re
import textstat

def calculate_complex_words_percentage(text):
    # count number of words with three or more syllables
    complex_words = 0
    for word in text.split():
        if textstat.syllable_count(word) >= 3:
            complex_words += 1

    # calculate percentage of complex words
    total_words = len(text.split())
    complex_words_percentage = (complex_words / total_words) * 100

    return complex_words_percentage

def calculate_fog_index(text):
    # calculate average sentence length
    avg_sentence_length = textstat.avg_sentence_length(text)

    # calculate percentage of complex words
    complex_words_percentage = calculate_complex_words_percentage(text)

    # calculate FOG Index
    fog_index = 0.4 * (avg_sentence_length + complex_words_percentage)

    return fog_index

# example usage
for i in text:
    fog_index = calculate_fog_index(i)
    print(fog_index)
