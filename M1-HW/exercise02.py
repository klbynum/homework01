# Author: Kemon Bynum
# Date: 01/30/25
# Class: CSC-488-01
# Create a list of ~ 10 different integers. Write a function (using modulus and
# conditionals) to determine if each integer is even or odd. Print to screen each digit
# followed by the word ‘even’ or ‘odd’ as appropriate

def my_list(myList):
    for x in myList:
        if x % 2 == 0: 
            print(x, " is an even number")
        else:
            print(x, " is an odd number")


myList = (20, 45, 10, 76, 55, 34, 88, 97, 1, 31)

my_list(myList)