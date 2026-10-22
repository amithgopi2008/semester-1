"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }



# Simulate the traffic light system up to time=maxtime in 1-second steps

# At the end of each step you should output the time and state using the statement on line 14

finished = False
time = -1

while time < 40:
    for state, timefor in states.items():
        for x in range(timefor):
            if time < 40:
                time = time + 1
                print(("Time ") + f"{time:03d}"+ (" State " + state))
            else:
                break




