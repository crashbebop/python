"""
        myself:     Crash
        Date  :     July 3, 2022
        Topic :     Multiline Print Test
"""

#you can use single or double quotes to create a string literal
x = 'This is single quotes'
y = "Double the quotes, double the fun"

#you can also assign a multiline string, with line breaks at certain points
z = """MULTILINE TEST WITH OFFSETS
            Guy 1: "Hey Man, you stole my wristwatch"
            Guy 2: "You dumb,  I already had a wristwatch. You dumb"
            Announcer: "BUUUUUURNED!"
            Meatwad: "Yeeahah, burned"
            Guy 1: *points finger "I saw you lookin' at it!" 
            Guy 2: *Pfft "Yo momma, you did"
            Announcer: "CLASSIC COMEBACK!"
            Guy 2: "Yo momma. Yo momma. Yo momma."
            *Guy 1 catches on fire
            Announcer: "INCINERATION!"
            Meatwad: "All right!"
            Announcer: "YOU'RE THE INSULT MASTER!"
    """

print(x, "(length:", len(x),")")
print(y, "(length:", len(y),")")
print(z, "(length:", len(z),")")

#OUTPUT LOOKS LIKE THIS FOR "py multiPrint.py"
""" 
This is single quotes (length: 21 )
Double the quotes, double the fun (length: 33 )
MULTILINE TEST WITH OFFSETS
            Guy 1: "Hey Man, you stole my wristwatch"
            Guy 2: "You dumb,  I already had a wristwatch. You dumb"
            Announcer: "BUUUUUURNED!"
            Meatwad: "Yeeahah, burned"
            Guy 1: *points finger "I saw you lookin' at it!"
            Guy 2: *Pfft "Yo momma, you did"
            Announcer: "CLASSIC COMEBACK!"
            Guy 2: "Yo momma. Yo momma. Yo momma."
            *Guy 1 catches on fire
            Announcer: "INCINERATION!"
            Meatwad: "All right!"
            Announcer: "YOU'RE THE INSULT MASTER!"
     (length: 592 )
"""