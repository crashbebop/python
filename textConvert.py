"""
        myself:     Crash
        Date  :     July 4, 2022
        Topic :     Function-TextConvert Test
"""

def makeMeScream(arg):
    
    #for debugging, show what the user gave us:
    #print("")
    #print("Entering makeMeScream: User argument is:", arg)
    
    #confirm that the user gave us a string
    if type(arg) is str:
        #they did the thing, convert everything to upper-case
        result = arg.upper()
    else:
        #the hell are they doing, remind them to fix things
        result = "You did not give me a string; prepare to die"    
    return result

def makeMeWhisper(arg):
    #for debugging, show what the user gave us:
    #print("")
    #print("Entering makeMeWhisper: User argument is:", arg)
    
    #confirm that the user gave us a string; doing inverse for fun...If user did not give us a string
    if type(arg) is not str:
        #this again...
        result = "i will lose my mind" 
    else:
        #they did the thing, convert everything to lower-case
        result = arg.lower()
    return result

def makeMeChangeMyMind(arg):
    #for debugging, show what the user gave us:
    #print("")
    #print("Entering makeMeChangeMyMind: User argument is:", arg)
    
    #confirm that the user gave us a string
    if type(arg) is str:
        #they did the thing, now allow them to change my mind if they chose an acceptable replacement
        acceptableAnswers    = ["Toad the Wet Sprocket", "Yo Momma", "Weezer"]
        rejectSpecialAnswers = ["Jay-Z", "Bright Eyes"]
        
        #ignore Case differences by converting user input and list of acceptable answers into lowercase
        checker = any(ele in str.lower(arg) for ele in map(lambda x: x.lower(), acceptableAnswers))
    else:
        #this again...
        checker = "GIB ME THAT string please"
    
    if checker:
        #true, we found something from the acceptableAnswers list
        result = "All right, all right. You win. You changed my mind.", arg, "is a decent band too."
    else:
        #failed
        result = "Blegh.", arg, "sucks."
        
    return result


#this is the test string we'll use. it's appropriate
myString = "CREEDeNCE CLEARWATER REVIVAL isn't that bad, fight me bruh"

#METHOD 1 = Assign the return values to variables; then print the variables
res1 = makeMeScream(myString)
res2 = makeMeWhisper(myString)
res3 = makeMeChangeMyMind("WeezER")

#print the return values
print("Print Test #1, Assignment Method:")
print("Test string    =", myString)
print("Scream result  =", res1)
print("Whisper result =", res2)
print("Change result  =", res3)
print("")

#METHOD 2 = Print inline without assigning to a separate variable
print("Print Test #2, Call Method:")
print("Test string    =", myString)
print("Scream result  =", makeMeScream(myString))
print("Whisper result =", makeMeWhisper(myString))
print("")

#METHOD 3 = Break it
print("Print Test #3, Break it by sending an integer:")
x = int(4)
print("Test           =", x)
print("Scream result  =", makeMeScream(x))
print("Whisper result =", makeMeWhisper(x))
print("")

#METHOD 4 = Replace it
print("Print Test #4, Maybe you can change my mind")
x = "WeezeR"
print("Test string    =", x)
print("Scream result  =", makeMeScream(x))
print("Whisper result =", makeMeWhisper(x))
print("Change result  =", makeMeChangeMyMind(x))
print("")

#OUTPUT LOOKS LIKE THIS FOR "py textConvert.py"
"""
Print Test #1, Assignment Method:
Test string    = CREEDeNCE CLEARWATER REVIVAL isn't that bad, fight me bruh
Scream result  = CREEDENCE CLEARWATER REVIVAL ISN'T THAT BAD, FIGHT ME BRUH
Whisper result = creedence clearwater revival isn't that bad, fight me bruh
Change result  =('All right, all right. You win. You changed my mind.', 'WeezER', 'is a decent band too.')

Print Test #2, Call Method:
Test string    = CREEDeNCE CLEARWATER REVIVAL isn't that bad, fight me bruh
Scream result  = CREEDENCE CLEARWATER REVIVAL ISN'T THAT BAD, FIGHT ME BRUH
Whisper result = creedence clearwater revival isn't that bad, fight me bruh

Print Test #3, Break it by sending an integer:
Test           = 4
Scream result  = You did not give me a string; prepare to die
Whisper result = i will lose my mind

Print Test #4, Maybe you can change my mind
Test string    = WeezeR
Scream result  = WEEZER
Whisper result = weezer
Change result  = ('All right, all right. You win. You changed my mind.', 'WeezeR', 'is a decent band too.')
"""