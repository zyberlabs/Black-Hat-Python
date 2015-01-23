#!/usr/bin/python

def anti_vowel(text):
    x = len(text)
    print x
    y = 0
    anti = ""
    while y < x:
        z = text[y]
        print y, z 
        if z == "a" or \
           z == "e" or \
           z == "i" or \
           z == "o" or \
           z == "u" or \
           z == "A" or \
           z == "E" or \
           z == "I" or \
           z == "O" or \
           z == "U":
            y = y + 1 
        else:
            anti = anti + text[y]
            y = y + 1
    return anti

print anti_vowel("I rock this!")

