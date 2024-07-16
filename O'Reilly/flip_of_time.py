#!/usr/bin/env checkio --domain=py run flip-of-time

# An hourglass is given as a tuple(upper, lower)for the number of minutes of sand that are currently stored in its upper and lower chambers, both chambers large enough to hold all of the sand in that hourglass. So aftermminutes of time has elapsed, the state of that particular hourglass will beupper - min(upper, m), lower + min(upper, m). The total amount of sand inside the hourglass never changes, nor will either chamber ever contain negative anti-sand.
# 
# Given a list ofglasses, your task is to find an optimal sequence of moves to measure exactlytminutes, scored as the number of individual hourglass flips performed along the way. Each move consists of two stages:
# 
# you must first wait for the hourglass that currently holds the lowest non zero amountmof sand in its upper chamber to run out.when that happens, chooseany subsetofglassesand instantaneously flip this chosen subset.Look at the example for[(7, 0), (11, 0)], 15case. You can find an explanation for slightly changed case in aPopular Mechanics article.
# 
# 
# 
# You don’t have any choice in waiting in the first stage, but in the second stage you enjoy an embarrassment of riches of 2n– 1 possible moves fornglasses!
# 
# This function should returnthe smallest possible number of individual hourglass flipsneeded to measure exactlytminutes, or None if this exact measurement is impossible.
# 
# Input:Two arguments:listoftuplesof two integers(int), integer.
# 
# Output:Integer orNone.
# 
# Examples:
# 
# assert hourglass_flips([(1, 0), (2, 0)], 2) == 0
# assert hourglass_flips([(7, 0), (11, 0)], 15) == 2
# assert hourglass_flips([(4, 0), (6, 0)], 11) == None
# assert hourglass_flips([(7, 1), (10, 4), (13, 1), (18, 4)], 28) == 3
# Pss..if you feel yourself in need of a hint, click this line.The base cases of recursion are whentequals 0 or when exactlytminutes remain in some upper chamber (no flips are needed), or whentis smaller than the smallest time remaining in the upper chamber of any hourglass (no solution is possible). Otherwise, update all hourglasses to their new states aftermminutes, and loop through all possible subsets ofglassesto flip. For each such subset, recursively construct the optimal sequence of moves to measure the remainingt - mminutes, and combine these moves to the best solution.
# 
# The mission was taken fromPython CCPS 109. It is taught forRyerson Chang School of Continuing EducationbyIlkka Kokkarinen
# 
# 
# END_DESC

def hourglass_flips(glasses: list[tuple[int, int]], t: int) -> int | None:
    # your code here
    return 0


print("Example:")
print(hourglass_flips([(1, 0), (2, 0)], 2))

# These "asserts" are used for self-checking
assert hourglass_flips([(1, 0), (2, 0)], 2) == 0
assert hourglass_flips([(7, 0), (11, 0)], 15) == 2
assert hourglass_flips([(4, 0), (6, 0)], 11) == None
assert hourglass_flips([(7, 1), (10, 4), (13, 1), (18, 4)], 28) == 3

print("The mission is done! Click 'Check Solution' to earn rewards!")