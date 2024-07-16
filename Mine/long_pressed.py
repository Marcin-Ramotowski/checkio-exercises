#!/usr/bin/env checkio --domain=py run long-pressed

# "I Love you soooooo much! You are the best!!"
# 
# Sometimes your friends want to express their feelings in a message, and sometimes a key with a letter gets stuck on the keyboard. In both cases we will get a "long-pressed letter" and the letter will then be printed more than once.    You are given two strings. The first string is the original text message. The second string is a printed message, which may contain several (or possibly none) long-pressed letters. It may happen that the message was written in a hurry, so do not forget to check that all the letters match those in the original. ReturnTrueif the printed message matches the original one, taking into account possible long keystrokes. OrFalseif there are errors or no long-pressed letters.
# 
# Input:String(str).
# 
# Output:Logic value(bool).
# 
# Preconditions:"text" and "typed" consist of only lowercase English letters and symbols "'/?!.,;1 <= len(text), len(typed) <= 1000.
# 
# 
# END_DESC

import re


def long_pressed(text: str, typed: str) -> bool:
    if text == typed:
        return False
    pattern = '+'.join(list(text)) + '+'
    return bool(re.fullmatch(pattern, typed))


print("Example:")
print(long_pressed("alex", "aaleex"))

assert long_pressed("alex", "aaleex") == True
assert long_pressed("welcome to checkio", "weeeelcome to cccheckio") == True
assert long_pressed("there is an error here", "there is an errorrr hereaa") == False
assert long_pressed("hi, my name is...", "hi, my name is...") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")