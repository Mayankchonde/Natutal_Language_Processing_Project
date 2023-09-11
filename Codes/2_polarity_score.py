
from textblob import TextBlob

def calculate_polarity_score(text):
  # creating TextBlob object
  text_blob = TextBlob(text)
  
  # calculating polarity score
  polarity_score = text_blob.sentiment.polarity
  
  return polarity_score
for i in text:
    polarity_score = calculate_polarity_score(i)
    print(polarity_score)