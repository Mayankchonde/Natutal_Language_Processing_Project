
import string

def calculate_average_sentence_length(text):
    # split the text into sentences
    sentences = text.split('.')
    # remove any empty sentences
    sentences = [sentence for sentence in sentences if sentence]
    # calculate the total number of words and sentences
    num_words = sum([len(sentence.split()) for sentence in sentences])
    num_sentences = len(sentences)
    # calculate the average sentence length
    if num_sentences > 0:
        avg_sentence_length = num_words / num_sentences
    else:
        avg_sentence_length = 0
    return avg_sentence_length





for i in text:
    avg_sentence_length = calculate_average_sentence_length(i)
    print(avg_sentence_length)
   