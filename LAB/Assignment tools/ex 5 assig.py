import string

text = "Hello! Welcome to NLP, Python."

result = ""

for ch in text:
    if ch not in string.punctuation:
        result += ch

print("Text without punctuation:")
print(result)
