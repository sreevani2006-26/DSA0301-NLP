import nltk
from nltk import PCFG
from nltk.parse import ViterbiParser

# Define the Probabilistic Context-Free Grammar (PCFG)
grammar = PCFG.fromstring("""
S  -> NP VP [1.0]
NP -> 'I' [0.5] | 'You' [0.5]
VP -> V N [1.0]
V  -> 'like' [0.6] | 'love' [0.4]
N  -> 'Python' [0.7] | 'NLP' [0.3]
""")

# Create the parser
parser = ViterbiParser(grammar)

# Input sentence
sentence = "I like Python".split()

# Parse the sentence
print("Most Probable Parse Tree:\n")

for tree in parser.parse(sentence):
    print(tree)
    print("\nProbability =", tree.prob())
