#!/usr/bin/env checkio --domain=py run staircase

# The easier problemBeat the previousasked you to greedily extract a strictly ascending sequence of integers from the given series ofdigits. For example, fordigitsequal to"31415926", thelistof integers returned should be[3, 14, 15, 92], with the last original digit left unused.
# 
# Going somewhat against intuition, the ability to tactically skip some of thedigitsat will may allow the resultinglistof integers to contain more elements than the list constructed in the previous greedy fashion. With this additional freedom, the example digit string"31415926"would allow the result[3, 4, 5, 9, 26]with one more element than the greedily constructed solution.
# 
# Your function should return the length of the longestlistof ascending integers that can be extracted fromdigits. Note that you are allowed to skip one or moredigitsnot just between two integers being extracted, but during the construction of each such integer.
# 
# Input:String(str).
# 
# Output:Integer(int).
# 
# Examples:
# 
# assert staircase("100123") == 4
# assert staircase("503715") == 4
# assert staircase("0425494220946") == 6
# assert staircase("04414952075836") == 7
# The mission was taken fromPython CCPS 109. It is taught forRyerson Chang School of Continuing EducationbyIlkka Kokkarinen
# 
# 
# END_DESC

def staircase(digits: str) -> int:
    # your code here
    return 0


print("Example:")
print(staircase("31415926"))

# These "asserts" are used for self-checking
assert staircase("100123") == 4
assert staircase("503715") == 4
assert staircase("0425494220946") == 6
assert staircase("04414952075836") == 7
assert staircase("1234567891011213") == 12

print("The mission is done! Click 'Check Solution' to earn rewards!")