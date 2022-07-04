"""
        myself:     Crash
        Date  :     July 3, 2022
        Topic :     Index Slicing Test
"""

#interested to see how negative indexing works

#show what we're working with
print("Beginning sliceTest.py")
x = "123456789abcdef"
print("x =", x)
print("*****************************")

#note: range(9) is actually 0 to 8
print("Beginning positive index test")
print("x =", x)
#in this test, we'll start at index = 0 (implicit), step up +1 each iteration (implicit), until we reach index = 9...well, actually 8 because range takes off one.
for i in range(9):
    print("i =", i)
    print("x =", x[i])
    print("")
print("*****************************")

print("Beginning negative index test") 
print("x =", x)   
#in this test, we'll start at index = -4, step up +1 each iteration, until we reach index = 0...well, actually -1 because range takes off one.
for i in range(-4, 0, 1):
    print("i =", i)
    print("x =", x[i])
    print("")
print("*****************************")
    
print("Beginning negative index test2") 
print("x =", x)   
#in this test, we'll start at index = -4, step down -1 each iteration, until we reach index = -16...well actually -15 because range takes off one.
#note: you can't set this to "-17" because the string isn't that long; causes out-of-bounds index reference and will fail compilation.
for i in range(-4, -16, -1):
    print("i =", i)
    print("x =", x[i])
    print("")
print("*****************************")


#OUTPUT LOOKS LIKE THIS FOR "py sliceTest.py"
""" 
Beginning sliceTest.py
x = 123456789abcdef
*****************************
Beginning positive index test
x = 123456789abcdef
i = 0
x = 1

i = 1
x = 2

i = 2
x = 3

i = 3
x = 4

i = 4
x = 5

i = 5
x = 6

i = 6
x = 7

i = 7
x = 8

i = 8
x = 9

*****************************
Beginning negative index test
x = 123456789abcdef
i = -4
x = c

i = -3
x = d

i = -2
x = e

i = -1
x = f

*****************************
Beginning negative index test2
x = 123456789abcdef
i = -4
x = c

i = -5
x = b

i = -6
x = a

i = -7
x = 9

i = -8
x = 8

i = -9
x = 7

i = -10
x = 6

i = -11
x = 5

i = -12
x = 4

i = -13
x = 3

i = -14
x = 2

i = -15
x = 1

*****************************
"""