print("===== STUDENT MARKS ANALYZER =====")

# Name
name = input("\nEnter your name: ")

# Marks
english = int(input("Enter your English marks: "))
computer = int(input("Enter your Computer Science marks: "))
maths = int(input("Enter your Maths marks: "))
physics = int(input("Enter your Physics marks: "))
chemistry = int(input("Enter your Chemistry marks: "))

# Store subjects and marks
subjects = {
    "English": english,
    "Computer Science": computer,
    "Maths": maths,
    "Physics": physics,
    "Chemistry": chemistry
}

# Total marks
total = sum(subjects.values())

# Percentage
percentage = total / 500 * 100

# Grade
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

# Pass / Fail
if percentage >= 33:
    result = "PASS"
else:
    result = "FAIL"

# Highest marks
highest_subject = max(subjects, key=subjects.get)
highest_marks = subjects[highest_subject]

# Result
print("\n===== RESULT =====")
print("Name:", name)
print("Total Marks:", total, "/ 500")
print("Percentage:", percentage, "%")
print("Grade:", grade)
print("Result:", result)
print("Highest Marks:", highest_subject, "-", highest_marks)