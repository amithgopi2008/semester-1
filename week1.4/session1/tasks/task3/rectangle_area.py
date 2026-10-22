
# function implementation

def rectangle_area(length, width):  # define suitable input data
    # ...               # implement the function
    return length * width  # return an appropriate value

# testing the function

print(f"Area is {rectangle_area(3,4)}")   # provide suitable data matching your inputs


def evenums(num):
    even = []
    start = 1
    for x in range(num):
        if start % 2 == 0:
            even.append(start)
        start = start + 1
    
    return even

print(evenums(16))

def mean(numlist):
    total = 0
    for x in range(len(numlist)):
        total = total + numlist[x]
    
    return (total / len(numlist))

numlist = [4,54,2,3,46,78]
print(mean(numlist))
