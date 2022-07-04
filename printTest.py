"""
        myself:     Crash
        Date  :     July 3, 2022
        Topic :     Variables Output
"""

# test printing/concatenating multiple variables to output
x = "twinkle my star"
y = "okay you win"
z = 'i like air'

# print the output, double spaced after comma? any differences?
print("Print test #1: double space after commas")
print(x,  y,  z)
#print empty newline
print("") 

# print the output, no space after comma
print("Print test #2: no space after commas")
print(x,y,z)
#print empty newline
print("") 

# print the output, using +
print("Print test #3: use +")
print(x + y + z)
#print empty newline
print("") 

print("*****************************") 
print("done, you rock.")
print("*****************************") 


#OUTPUT LOOKS LIKE THIS FOR "py printTest.py"
""" 
Print test #1: double space after commas
twinkle my star okay you win i like air

Print test #2: no space after commas
twinkle my star okay you win i like air

Print test #3: use +
twinkle my starokay you wini like air

*****************************
done, you rock.
*****************************
"""