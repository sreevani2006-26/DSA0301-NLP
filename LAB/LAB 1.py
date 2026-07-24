1.
import re
text = input("Enter a sentence: ")
pattern = input("Enter the word to search: ")
match = re.match(pattern, text)
search = re.search(pattern, text)
if match:
    print("Match found at the beginning of the text.")
else:
    print("No match at the beginning.")
if search:
    print("Pattern found in the text.")
    print("Position:", search.start())
else:
    print("Pattern not found.")
