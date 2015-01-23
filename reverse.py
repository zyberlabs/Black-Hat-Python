#!/usr/bin/python

def reverse(text):
    x = (len(text) - 1)
    reversed = ""
    while x >= 0:
        reversed = reversed + text[x]
        x = x - 1
    return reversed

print reverse("Python!")

