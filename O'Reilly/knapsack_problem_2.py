#!/usr/bin/env checkio --domain=py run knapsack-problem-2

# 
# 
# This mission is dedicated to a famous and classicalKnapsack Problem.
# 
# You are given a list of kinds of itemsitems, that you want to put into knapsack. Item of each kind is a tuple of its value, weight and maximum amount (optional). You need to find a subset of items, such that:the total value of the items in subset is as large as possible;the total weight of items in subset is at mostweight, that is capacity of the knapsack;for each kind of items you can select at most given amount items. If its not given - there is no restriction for amount.
# 
# Input:Two arguments. Maximum weight as integer, items as list of tuples of two or three integers.
# 
# Output:Maximum value as integer.
# 
# Examples:
# 
# assert knapsack(5, [(4, 2, 1), (5, 2, 1), (2, 1, 1), (8, 3, 1)]) == 13
# assert knapsack(8, [(4, 2), (5, 2), (2, 1), (8, 3)]) == 21
# assert knapsack(8, [(10, 10, 3)]) == 0
# assert knapsack(8, [(4, 3, 2), (2, 1, 1), (1, 2, 4), (3, 2, 2)]) == 12
# 
# END_DESC

def knapsack(weight: int, items: list[tuple[int, int] | tuple[int, int, int]]) -> int:
    # your code here
    return 0


print("Example:")
print(knapsack(8, [(4, 3, 2), (2, 1, 1), (1, 2, 4), (3, 2, 2)]))

# These "asserts" are used for self-checking
assert knapsack(5, [(4, 2, 1), (5, 2, 1), (2, 1, 1), (8, 3, 1)]) == 13
assert knapsack(8, [(4, 2), (5, 2), (2, 1), (8, 3)]) == 21
assert knapsack(8, [(10, 10, 3)]) == 0
assert knapsack(8, [(4, 3, 2), (2, 1, 1), (1, 2, 4), (3, 2, 2)]) == 12

print("The mission is done! Click 'Check Solution' to earn rewards!")