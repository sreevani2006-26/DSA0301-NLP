from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = ["relational", "running", "studies", "connections", "happiness"]

print("Original Word\tStemmed Word")
print("-"*35)

for word in words:
    print(word, "\t", stemmer.stem(word))
