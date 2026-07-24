import re

text = "Running and playing are enjoyable."

words = re.findall(r"\b\w+ing\b", text)

print(words)
