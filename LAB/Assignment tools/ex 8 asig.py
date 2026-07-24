from nltk.tokenize import word_tokenize
from collections import Counter

text = "NLP is easy. NLP is useful. NLP is powerful."

words = word_tokenize(text.lower())

frequency = Counter(words)

print("Word Frequency:")
for word, count in frequency.items():
    print(word, ":", count)
