def calculate_percentage_complex_words(text):
    # define a set of common words that are not considered complex
    common_words = {'the', 'and', 'a', 'an', 'in', 'on', 'at', 'to', 'is', 'was', 'were', 'it', 'that', 'this', 'of', 'for'}
    # split the text into words
    words = text.split()
    # remove any punctuation from the words
    words = [word.translate(str.maketrans('', '', string.punctuation)) for word in words]
    # calculate the number of words and complex words
    num_words = len(words)
    num_complex_words = sum([1 for word in words if word not in common_words and len(word) > 2])
    # calculate the percentage of complex words
    if num_words > 0:
        pct_complex_words = (num_complex_words / num_words) * 100
    else:
        pct_complex_words = 0
    return pct_complex_words

for i in text:
    pct_complex_words = calculate_percentage_complex_words(i)
    print(pct_complex_words)