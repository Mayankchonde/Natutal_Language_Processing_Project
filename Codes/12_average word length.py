
import nltk

nltk.download("punkt")


average_word_lengths = []
for i in text:
    words = nltk.word_tokenize(i)
    total_word_length = 0
    for word in words:
        total_word_length += len(word)
    average_word_length = total_word_length / len(words)
    average_word_lengths.append(average_word_length)


for j in average_word_lengths:
    print(j)