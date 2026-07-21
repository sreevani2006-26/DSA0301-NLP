from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import SnowballStemmer

porter = PorterStemmer()
lancaster = LancasterStemmer()
snowball = SnowballStemmer("english")

words = ["playing","running","studies","connection","relational"]

print("Word\tPorter\tLancaster\tSnowball")

for word in words:
    print(word,"\t",
          porter.stem(word),"\t",
          lancaster.stem(word),"\t\t",
          snowball.stem(word))
