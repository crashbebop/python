"""
        myself:     Crash
        Date  :     July 3, 2022
        Topic :     Global Variables, Function test
"""

# create a global variable, then call it inside a function
global x 
x = "awansome"

#creating a function called thisIsMyFunctionIllNameItAsLongAsIWantFoo where we'll print out x
def thisIsMyFunctionIllNameItAsLongAsIWantFoo():
    x = "poopsmcgee"
    print("This is another print test inside a function, but look at my cool local variable x: ", x)

#calling our super cool function
thisIsMyFunctionIllNameItAsLongAsIWantFoo()

#testing global vs local operations, why does python allow you to do this?
print("The Final Printout; this x should be global again: ", x)

#OUTPUT LOOKS LIKE THIS FOR "py globalFunTest.py"
""" 
This is another print test inside a function, but look at my cool local variable x:  poopsmcgee
The Final Printout; this x should be global again:  awansome
"""