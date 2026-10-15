# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers

is_num = False
float_values = read_numbers()
real_floatvalues = []


def is_float(value):
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False
for x in range(len(float_values)):
    if is_float(float_values[x]) == True:
        is_num = True
        real_floatvalues.append(float(float_values[x]))
if is_num == False:
    sys.exit("Error: no numbers provided")



total = 0
maximum = 0
minimum = real_floatvalues[0]
median = 0

def calculate_highest(float_list):
    sorted_list = sorted(float_list)
    return sorted_list[len(float_list)-1]


mean = sum(real_floatvalues) / len(real_floatvalues)

def calculate_lowest(float_list):
    sorted_list = sorted(float_list)
    return sorted_list[0]

def calculate_median(float_list):
    sorted_list = sorted(float_list)
    n = len(sorted_list)
    if n == 0:
        print("Error list is empty! ")
    
    mid = n // 2
    if n % 2 == 0:
        return (sorted_list[mid-1] + sorted_list[mid]) / 2
    else:
        return sorted_list[mid]

median = calculate_median(real_floatvalues)
minimum = calculate_lowest(real_floatvalues)
maximum = calculate_highest(real_floatvalues)
print("Minimum = " + str(minimum))
print("Maximum = " + str(maximum))
print("Mean = " + str(mean))
print("Median = " + str(median))
