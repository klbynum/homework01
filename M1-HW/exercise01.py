# Author: Kemon Bynum
# Date: 01/30/25
# Class: CSC-488-01
# Create three lists containing 10 integers each. The first list should contain all the
# integers sequentially from 1 to 10 (inclusive). The second list should contain the
# squares of each element in the first list. The third list should contain the cubes of
# each element in the first list. Print all three lists side-by-side in three columns. E.g.
# the first row should contain 1, 1, 1 and the second row should contain 2, 4, 8.
def my_list(myList):
    myList = (20, 45, 10, 76, 55, 34, 88, 97, 1, 31)
    return myList

def print_list(myList):
    for x in myList:
        if x % 1 == 0: 
            print("The following numbers are even numbers: ", myList)
        else: 
            print("The following numbers are odd numbers: ", myList)
