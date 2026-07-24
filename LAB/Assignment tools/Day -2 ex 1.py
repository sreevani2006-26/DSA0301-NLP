import re

text = "My DOB is 15/08/2004 and exam is on 20/07/2026."

dates = re.findall(r'\b\d{2}/\d{2}/\d{4}\b', text)

print("Dates:")
print(dates)
