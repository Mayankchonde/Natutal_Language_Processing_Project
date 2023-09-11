
import nltk

nltk.download("punkt")

personal_pronouns = ["I", "me", "my", "mine", "myself", "you", "your", "yours", "yourself", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "we", "us", "our", "ours", "ourselves", "they", "them", "their", "theirs", "themselves"]

personal_pronoun_counts = []
for i in text:
    words = nltk.word_tokenize(i)
    personal_pronoun_count = sum([1 for word in words if word in personal_pronouns])
    personal_pronoun_counts.append(personal_pronoun_count)
    

for j in personal_pronoun_counts:
    print(j)