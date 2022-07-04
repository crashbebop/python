"""
        myself:     Crash
        Date  :     July 3, 2022
        Topic :     Function-Argument Test
"""

#creating a function here; going to add sanity checking
def poopingIsAJoyEveryoneShouldExperienceOnce(arg1):
    
    #for debugging, show what the user gave us:
    print("")
    print("Entering poopingIsAJoyEveryoneShouldExperienceOnce.py: User argument is:", arg1)
    
    #confirm that the user gave us a number
    if type(arg1) is int:
        if arg1 == 1:
             #if the user gave us "1" then we choose this option
            print("You have chosen wisely, 1 will not be the lonliest number anymore")
        else:
            #otherwise, the user did not give a "1", use this text
            print("You have chosen more wisely than your predecessor. You can have a cookie")
    else:
        #if we ended up here, the user did not give us an int
        print("You done broke it")

poopingIsAJoyEveryoneShouldExperienceOnce(1)
poopingIsAJoyEveryoneShouldExperienceOnce(5)
poopingIsAJoyEveryoneShouldExperienceOnce("I won't do what you tell me!")

#OUTPUT LOOKS LIKE THIS FOR "py fxTest.py"
"""
Entering poopingIsAJoyEveryoneShouldExperienceOnce.py: User argument is: 1
You have chosen wisely, 1 will not be the lonliest number anymore

Entering poopingIsAJoyEveryoneShouldExperienceOnce.py: User argument is: 5
You have chosen more wisely than your predecessor. You can have a cookie

Entering poopingIsAJoyEveryoneShouldExperienceOnce.py: User argument is: I won't do what you tell me!
You done broke it
"""