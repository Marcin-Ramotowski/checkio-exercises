#!/usr/bin/env checkio --domain=py run water-sort-game

# InWater Sort gameyou are given a sequence of flasks. Most of them are filled with mixed liquids of different colors, and some are empty. Your task is to collect liquids of the same color in one flask using empty flasks by pouring a single color portion(s) from one flask to another with this color on top or to empty one.
# 
# 
# 
# The sequence of flasks is represented as list of strings. All non-empty flasks in a sequence have the same capacity (which may vary from test to test). Colors of liquids are encoded by latin letters from top to bottom (in flasks) and from leftest to rightest flask in order of first appearance (the first color is encoded as"a", the next distinct color -"b"etc).  Adjacent portions of the same color encoded with repeating letter ("aa", "ccc"etc.).
# 
# Your mission is to calculate the minimum number of pourings needed to collect every distinct color in one flask.
# 
# 
# 
# Input:Listof strings(str).
# 
# Output:Integer(int).
# 
# Examples:
# 
# assert water_sort(["abab", "baba", ""]) == 7
# assert water_sort(["abcc", "abca", "bcab", "", ""]) == 10
# assert water_sort(["abca", "bcbc", "aabc", "", ""]) == 10
# Precondition:total_number_tubes >= number_colors + 1
# 
# This mission is an implementation of the followingWater Sort Google Play app. All tests were taken from the beginning of the app. You may use the app to understand the mission better and solve it easier as I did while creating it.
# 
# 
# END_DESC

def water_sort(flasks: list[str]) -> int:
    # your code here
    return 0


print("Example:")
print(water_sort(["abab", "baba", ""]))

# These "asserts" are used for self-checking
assert water_sort(["abab", "baba", ""]) == 7
assert water_sort(["abcc", "abca", "bcab", "", ""]) == 10
assert water_sort(["abca", "bcbc", "aabc", "", ""]) == 10

print("The mission is done! Click 'Check Solution' to earn rewards!")