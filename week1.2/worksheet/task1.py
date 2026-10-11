# Worksheet 1.2: Task 1 Solution
import sys


score = int(input("Enter an integer between 0 and 100: "))

if score.isdigit() == False or score < 0 or score > 100:
    sys.exit("Error: Grade must be an integer between 0 and 100")

grade = ""
if score <= 39 and score >= 0:
    grade = "Fail"
elif score >= 40 and score <= 69:
    grade = "Pass"
else:
    grade = "Distinction"

print(str(score) + "is a " + grade + "")