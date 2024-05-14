from collections import Counter
word_counts = Counter(words)
top_four = word_counts.most_common(4)
print(top_four)