from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = [
    "connect","connected","connection","connections","connective",
    "relate","related","relation","relative","relativity"
]

print("Original Word\tStemmed Word")

for word in words:
    print(word,"\t",stemmer.stem(word))
