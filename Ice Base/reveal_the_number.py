#!/usr/bin/env checkio --domain=py run reveal-the-number

# https://youtu.be/hSlffi7fMO8You are given a string of different characters (letters, digits and other symbols). The goal is to "extract" the number from the string: concatenate only digits, number sign and "." (if present) and return the result in number format. If no number can be extracted (no digits in the given string) - returnNone.
# 
# Expected behavior:take into consideration the LAST number sign before the FIRST digit;take into consideration the FIRST dot in the string (It's guaranteed, that it goes after at least one digit or has at least one digit after). If there is a dot, return as float, otherwise - integer.
# 
# Input:String(str).
# 
# Output:Integer(int), float(float)orNone.
# 
# Examples:
# 
# assert reveal_num("F0(t}") == 0
# assert reveal_num("Utc&g") == None
# assert reveal_num("-aB%|_-+2ADS.12+3.ADS1.2") == 2.12312
# assert reveal_num("-aB%|_+-2ADS.12+3.ADS1.2") == -2.12312
# 
# END_DESC

def reveal_num(line: str) -> int | float | None:
    # your code here
    return 0


print("Example:")
print(reveal_num("+A%+-1-0..."))

# These "asserts" are used for self-checking
assert reveal_num("F0(t}") == 0
assert reveal_num("Utc&g") == None
assert reveal_num("-aB%|_-+2ADS.12+3.ADS1.2") == 2.12312
assert reveal_num("-aB%|_+-2ADS.12+3.ADS1.2") == -2.12312
assert reveal_num("zV№1}3;o.vEf``C.WqTY0") == 13.0
assert reveal_num("!3B'j=(}89JQ6aWvN*%5@uy.r)B<?pZ.!545ZD^KF9Sx@gqfa*") == 38965.5459

print("The mission is done! Click 'Check Solution' to earn rewards!")