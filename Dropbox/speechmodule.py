#!/usr/bin/env checkio --domain=py run speechmodule

# Stephen's speech module is broken.    This module is responsible for his number pronunciation.    He has to click to input all of the numerical digits in a figure,    so when there are big numbers it can take him a long time.    Help the robot to speak properly and increase his number processing speed by writing a new speech module for him.    All the words in the string must be separated by exactly one space character.    Be careful with spaces -- it's hard to see if you place two spaces instead one.
# 
# Input:A number as an integer.
# 
# Output:The string representation of the number as a string.
# 
# How it is used:This concept may be useful for the speech synthesis software or automatic reports systems.    This system can also be used when writing a chatbot by assigning words or phrases numerical    values and having a system retrieve responses based on those values.
# 
# Precondition:0 < number < 1000
# 
# 
# END_DESC

FIRST_TEN = ["", "one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
NUMBERS = FIRST_TEN + SECOND_TEN # numbers from 1 to 20


def checkio(n: int):
    text = f"{n:03}"
    divs = list(map(int, text))
    parts = []
    if divs[0] > 0:
        parts.append(f"{FIRST_TEN[divs[0]]} hundred")
        n -= 100 * divs[0]
    if n >= 20:
        parts.append(f"{OTHER_TENS[divs[1]-2]} {NUMBERS[divs[2]]}")
    else:
        parts.append(NUMBERS[n])
    return ' '.join(parts).rstrip()