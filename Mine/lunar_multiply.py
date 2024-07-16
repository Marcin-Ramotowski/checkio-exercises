#!/usr/bin/env checkio --domain=py run lunar-multiply

# This problem was inspired by another jovialNumberphilevideo“Primes on the Moon”byNeil Sloanethat you should watch first to get an idea of how this wacky “lunar arithmetic” works.
# 
# 
# 
# Formerly known as “dismal arithmetic”, addition and multiplication of natural numbers are redefined so thataddingtwo digits means taking theirmaximum, whereasmultiplyingtwo digits means taking theirminimum. For example,2 + 7 = 7 + 2 = 7and2 × 7 = 7 × 2 = 2. Unlike ordinary addition, there can never be a carry to the next column of digits, no matter how many individual digits are added together in that column. For numbers that consist of several digits, addition and multiplication work exactly as you learned back in grade school, except that the shifted digit columns from lunar multiplication of the individual digits are added in the same lunatic fashion. Let's look again at the example:
# 
# 
# 
# Input:Two integers(int).
# 
# Output:Integer(int).
# 
# Examples:
# 
# assert lunar_multiply(2, 3) == 2
# assert lunar_multiply(8, 9) == 8
# assert lunar_multiply(10, 10) == 100
# assert lunar_multiply(11, 11) == 111
# The mission was taken from Python CCPS 109. It is taught for Ryerson Chang School of Continuing Education byIlkka Kokkarinen
# 
# 
# END_DESC

def lunar_multiply(a: int, b: int) -> int:
    # your code here
    return 0


print("Example:")
print(lunar_multiply(2, 3))

# These "asserts" are used for self-checking
assert lunar_multiply(2, 3) == 2
assert lunar_multiply(8, 9) == 8
assert lunar_multiply(10, 10) == 100
assert lunar_multiply(11, 11) == 111
assert lunar_multiply(17, 24) == 124
assert lunar_multiply(357, 64) == 3564

print("The mission is done! Click 'Check Solution' to earn rewards!")