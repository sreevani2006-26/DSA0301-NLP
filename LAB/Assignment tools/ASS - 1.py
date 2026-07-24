import re
reg_no = input("Enter Register Number: ")
email = input("Enter Institutional Email: ")
course_code = input("Enter Course Code: ")
semester = input("Enter Semester (1-8): ")
mobile = input("Enter Mobile Number: ")
reg_pattern = r"^[A-Z]{2}\d{6}$"
email_pattern = r"^[a-zA-Z0-9._%+-]+@saveetha\.com$"
course_pattern = r"^[A-Z]{2,4}\d{3}$"
semester_pattern = r"^[1-8]$"
mobile_pattern = r"^[6-9]\d{9}$"
status = True

if re.match(reg_pattern, reg_no):
    print("Register Number : Valid")
else:
    print("Register Number : Invalid")
    status = False
if re.match(email_pattern, email):
    print("Institutional Email : Valid")
else:
    print("Institutional Email : Invalid")
    status = False
if re.match(course_pattern, course_code):
    print("Course Code : Valid")
else:
    print("Course Code : Invalid")
    status = False
if re.match(semester_pattern, semester):
    print("Semester : Valid")
else:
    print("Semester : Invalid")
    status = False
if re.match(mobile_pattern, mobile):
    print("Mobile Number : Valid")
else:
    print("Mobile Number : Invalid")
    status = False
print("\n========== Registration Status ==========")

if status:
    print("Registration Successful")
else:
    print("Registration Failed")
