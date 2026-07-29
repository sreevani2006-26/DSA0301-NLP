# Initial tagged sentence (Word, Tag)
sentence = [
    ("I", "PRON"),
    ("can", "NOUN"),      # Initially tagged incorrectly
    ("swim", "VERB")
]

print("Initial Tags:")
for word, tag in sentence:
    print(word, "->", tag)

# -------------------------------
# Transformation Rule
# Rule:
# If the word is "can" and the next word is a VERB,
# change its tag from NOUN to AUX.
# -------------------------------

for i in range(len(sentence) - 1):
    word, tag = sentence[i]
    next_word, next_tag = sentence[i + 1]

    if word == "can" and tag == "NOUN" and next_tag == "VERB":
        sentence[i] = (word, "AUX")

print("\nAfter Applying Transformation Rule:")
for word, tag in sentence:
    print(word, "->", tag)
