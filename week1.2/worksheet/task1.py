# Worksheet 1.2: Task 1 Solution
import sys


score = input("Enter an integer between 0 and 100: ")

if score.isdigit() == False or int(score) < 0 or int(score) > 100:
    sys.exit("Error: Grade must be an integer between 0 and 100")

grade = ""
if int(score) <= 39 and int(score) >= 0:
    grade = "Fail"
elif int(score) >= 40 and int(score) <= 69:
    grade = "Pass"
else:
    grade = "Distinction"

print(str(score) + " is a " + grade + "")