import re

text = "Hello! How are you? I'm fine."

result = re.sub(r'[^\w\s]', '', text)

print("Original:", text)
print("Without Punctuation:", result)
