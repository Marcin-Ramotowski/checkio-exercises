#!/usr/bin/env checkio --domain=py run count-divisibles-in-range

# Let us take a breather by tackling a problem simple enough that its solution needs only a couple of conditional statements and some arithmetic, but not even one loop or anything more fancy. The difficulty is coming up with the conditions that cover all possible cases of this problem just right, including all of the potentially tricksy edge and corner cases, without being off-by-one anywhere.
# 
# Given three integersstart, end, n, so thatstart <= end, count how many integers betweenstartandend, inclusive, are evenly divisible byn. Note that eitherstartorendcan well be negative or zero, butnis guaranteed to be greater than zero. Here is the scheme for1, 9, 3input.
# 
# 
# 
# Sure, this problem could be solved as a one-liner with the lazy comprehension.Try to have code with no loops at all, but use only integer arithmetic and conditional statements to root out the truth.
# 
# Input:Three integers(int).
# 
# Output:Integer(int).
# 
# Examples:
# 
# assert count_divisibles(7, 28, 4) == 6
# assert count_divisibles(-77, 19, 10) == 9
# assert count_divisibles(1, 999999999999, 5) == 199999999999
# Preconditions:start <= end;n > 0.
# 
# The mission was taken fromPython CCPS 109. It is taught forRyerson Chang School of Continuing EducationbyIlkka Kokkarinen
# 
# 
# END_DESC

def count_divisibles(start: int, end: int, n: int) -> int:
    # your code here
    return 0


print("Example:")
print(count_divisibles(1, 9, 3))

# These "asserts" are used for self-checking
assert count_divisibles(7, 28, 4) == 6
assert count_divisibles(-77, 19, 10) == 9
assert count_divisibles(1, 999999999999, 5) == 199999999999

print("The mission is done! Click 'Check Solution' to earn rewards!")