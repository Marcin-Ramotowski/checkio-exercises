#!/usr/bin/env checkio --domain=py run epi

# In this challenge, you will be given a result, and your task is to find an arithmetic expression that uses only the numbers pi and e to yield that result.    You can use addition, subtraction, multiplication, division, and exponentiation operations, and each number (pi and e) can appear at most two times.    Parentheses are not allowed. If there are multiple solutions, return the one that requires fewer operations. If there are still multiple solutions,    return the one that comes first alphabetically (without spaces). The calculated result must be equal with an error smaller than 1 x 10-10.     If there is no solution for the input, return None. Non negative/positive symbol at the beginning is allowed.
# 
# Input:Floating point number(float).
# 
# Output:String(str).
# 
# Examples:
# 
# assert checkio(5.85987448205) == "e+pi"
# assert checkio(18.2958548951) == "e**e+pi"
# assert checkio(47.6085189284) == "e**e*pi"
# assert checkio(-0.42331082513) == "e-pi"
# 
# END_DESC

from math import e, pi


def checkio(n: float) -> str:
    # your code here
    return ""


print("Example:")
print(checkio(5.85987448205))

# These "asserts" are used for self-checking
assert checkio(5.85987448205) == "e+pi"
assert checkio(18.2958548951) == "e**e+pi"
assert checkio(47.6085189284) == "e**e*pi"
assert checkio(-0.42331082513) == "e-pi"
assert checkio(7.38905609893) == "e*e"

print("The mission is done! Click 'Check Solution' to earn rewards!")