#!/usr/bin/env checkio --domain=py run ordinary-cardinals

# Sorting can be performed meaningfully according to arbitrary comparison criteria, as long as those criteria satisfy the mathematical requirements of atotal orderingrelation. To play around with this concept to grok it, let us define a wacky ordering relation of positive integers so that for any two integers, the one that contains the digit 9 more times is considered to be larger, regardless of the magnitude and other digits of these numbers.
# 
# For example,99 > 123456789 > 1010in this ordering. If both integers contain the digit 9 the same number of times, the comparison proceeds to the next lower digit 8, and so on down there until the first distinguishing digit has been discovered. If both integers contain every digit from 9 to 0 pairwise the same number of times, theordinary integer ordercomparison determines their mutual ordering.
# 
# Your goal is to sort given sequence of integers according to this rule in ascending order. Let's see an additional example for[111, 19, 919, 1199, 911, 999]input.
# 
# 
# 
# Input:Listof integers(int).
# 
# Output:Listof integers(int).
# 
# Examples:
# 
# assert sort_digit_count([99, 123456789, 10000000000]) == [10000000000, 123456789, 99]
# assert sort_digit_count([9876, 19, 4321, 99, 73, 241, 111111, 563, 33]) == [
#     111111,
#     33,
#     241,
#     4321,
#     563,
#     73,
#     19,
#     9876,
#     99,
# ]
# assert sort_digit_count([111, 19, 919, 1199, 911, 999]) == [
#     111,
#     19,
#     911,
#     919,
#     1199,
#     999,
# ]
# assert sort_digit_count([1234, 4321, 3214, 2413]) == [1234, 2413, 3214, 4321]
# The mission was taken fromPython CCPS 109. It is taught forRyerson Chang School of Continuing EducationbyIlkka Kokkarinen
# 
# 
# END_DESC

def sort_digit_count(items: list[int]) -> list[int]:
    # your code here
    return []


print("Example:")
print(sort_digit_count([99, 123456789, 10**10]))

# These "asserts" are used for self-checking
assert sort_digit_count([99, 123456789, 10000000000]) == [10000000000, 123456789, 99]
assert sort_digit_count([9876, 19, 4321, 99, 73, 241, 111111, 563, 33]) == [
    111111,
    33,
    241,
    4321,
    563,
    73,
    19,
    9876,
    99,
]
assert sort_digit_count([111, 19, 919, 1199, 911, 999]) == [
    111,
    19,
    911,
    919,
    1199,
    999,
]
assert sort_digit_count([1234, 4321, 3214, 2413]) == [1234, 2413, 3214, 4321]

print("The mission is done! Click 'Check Solution' to earn rewards!")