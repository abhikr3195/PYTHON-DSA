"""
Create a function named printPattern that takes one integer (num) as
an argument. Print from -num to num. Also keep in mind number passed as
an argument can be negative or positive.
"""
def printPattern(num):
    if num>0:
        start = -num
        end=num
    else:
        start = num
        end = -num
    while start<=end:
        print(start,end="")
        start += 1
printPattern(-9)        