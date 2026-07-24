import re
resume = """
Name: Teja Varma
Email: teja123@gmail.com
Mobile: +91 9876543210

Skills:
Python, Java, SQL, Machine Learning, NLP

Experience: 3 years
"""
name = re.search(r"Name\s*:\s*(.*)", resume)
name = name.group(1) if name else "Not Found"
email = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", resume)
mobile = re.findall(r"(?:\+91[-\s]?)?[6-9]\d{9}", resume)
skills_list = ["Python", "Java", "SQL", "Machine Learning", "NLP"]
skills = []
for skill in skills_list:
    if re.search(skill, resume, re.IGNORECASE):
        skills.append(skill)
exp = re.search(r"(\d+)\s+years?", resume, re.IGNORECASE)
experience = int(exp.group(1)) if exp else 0
print("----- Candidate Profile -----")
print("Name:", name)
print("Email:", email)
print("Mobile:", mobile)
print("Skills:", skills)
print("Experience:", experience, "years")
if experience >= 2 and "Python" in skills:
    print("\nStatus: Eligible for Shortlisting")
else:
    print("\nStatus: Not Eligible")
