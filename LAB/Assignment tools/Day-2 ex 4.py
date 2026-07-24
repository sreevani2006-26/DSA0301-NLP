import re

text = "Ram scored 95 marks and paid 2500 rupees."

numbers = re.findall(r'\d+', text)

print("Numbers:")
print(numbers)
