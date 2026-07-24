import nltk
from nltk.tokenize import sent_tokenize

text = "Hello everyone. Welcome to NLP. This is sentence tokenization."

sentences = sent_tokenize(text)

print("Sentences:")
for sentence in sentences:
    print(sentence)
