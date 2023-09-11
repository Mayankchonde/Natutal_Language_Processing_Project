def calculate_complex_word_count(text):
    # count the number of words with three or more syllables
    complex_word_count = 0
    for word in text.split():
        if textstat.syllable_count(word) >= 3:
            complex_word_count += 1

    return complex_word_count
for i in text:
    complex_word_count = calculate_complex_word_count(i)
    print(complex_word_count)