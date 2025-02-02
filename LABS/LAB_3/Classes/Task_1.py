#Define a class which has at least two methods: getString: 
#to get a string from console input printString: to print the string in upper case.

class twoMethods:
    def __init__(self):
        self.string=""
    def getString(self):
        self.string=input()
    def printString(self):
        print(self.string.upper())

x = twoMethods()
x.getString()
x.printString()