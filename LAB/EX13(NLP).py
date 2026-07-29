import nltk
from nltk import CFG
from nltk.parse import ChartParser

# Define the Context-Free Grammar
grammar = CFG.fromstring("""
S -> NP VP
NP -> 'I' | 'You'
VP -> V N
V -> 'like' | 'love'
N -> 'Python' | 'NLP'
""")

# Create the parser
parser = ChartParser(grammar)

# Input sentence
sentence = "I like Python".split()

# Generate and display parse tree
print("Parse Tree:\n")

for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()
