from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text = "This is a simple example of Natural Language Processing."

words = word_tokenize(text)

stop_words = set(stopwords.words('english'))

filtered = [word for word in words if word.lower() not in stop_words]

print("Words after removing stop words:")
print(filtered)
