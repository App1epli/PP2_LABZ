#Define a functino histogram() that takes a list of integers and prints a histogram to the screen. 
#For example, histogram([4, 9, 7]) should print the following:
"""
****
*********
*******
"""
def histogram(l):
    for i in l:
        print("*"*i)
    
l=[4, 9, 7]
histogram(l)