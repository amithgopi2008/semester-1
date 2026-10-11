"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Amith Gopi
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.

monthlyspend = input("Enter your monthlhly saving amount, it should be an integer: ")

while not monthlyspend.isdigit():

    print("Invalid amount")
    monthlyspend = input("Enter your monthlhly saving amount, it should be an integer: ")

    
monthlyspend = int(monthlyspend)
yearlysavings = monthlyspend * 12
print("Total saved money for the year will be £" + str(yearlysavings) + ".")

totalsavings = yearlysavings + (yearlysavings * 0.008)
roundedsavings = round(totalsavings, 2)

print("£"+"{:.2f}".format(roundedsavings))




# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).


# print this out for the user with a suitable message.



# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.

# print this out in the format £X.XX (to two decimal places).

