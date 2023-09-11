
from textblob import TextBlob

def calculate_subjectivity_score(text):
    # create TextBlob object
    text_blob = TextBlob(text)
    
    # calculate subjectivity score
    subjectivity_score = text_blob.sentiment.subjectivity
    
    return subjectivity_score
for i in text:
    subjectivity_score = calculate_subjectivity_score(i)
    print(subjectivity_score)