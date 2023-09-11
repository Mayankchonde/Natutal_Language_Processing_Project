

import textstat

def calculate_syllables_per_word(text):
    # split the text into words
    words = text.split()

    # count the total number of syllables and words
    total_syllables = 0
    total_words = len(words)
    for word in words:
        total_syllables += textstat.syllable_count(word)

    # calculate the syllables per word
    syllables_per_word = total_syllables / total_words

    return syllables_per_word

for i in text:
    syllables_per_word = calculate_syllables_per_word(i)
    print(syllables_per_word)
