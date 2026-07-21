

from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

text = input("Enter a paragraph: ")

words = word_tokenize(text)

print("Original Words:")
print(words)

print("\nStemmed Words:")
for word in words:
    print(stemmer.stem(word), end=" ")
