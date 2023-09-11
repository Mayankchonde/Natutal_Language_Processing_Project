


word_counts = []
for i in text:
    words = i.split()
    word_count = 0
    for word in words:
        word_count += 1
    word_counts.append(word_count)
print(word_counts)


for j in word_counts:
    print(j)
