import re

text = "Contact us at abc@gmail.com or support@yahoo.com"

emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)

print("Email Addresses:")
print(emails)
