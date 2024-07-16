#!/usr/bin/env checkio --domain=py run not-in-order

# You are given a list of integers. Your function should return the number of elements, which are not at their places as if the list would be sorted ascending. For example, for the sequence[1, 1, 4, 2, 1, 3]the result is3, since elements at indexes 2, 4, 5 (remember about 0-based indexing in Python) are not at their places as in the same sequence sorted ascending -[1, 1, 1, 2, 3, 4].
# 
# Input:Listof integers (int).
# 
# Output:Integer (int).
# 
# Examples:
# 
# assert not_order([1, 1, 4, 2, 1, 3]) == 3
# assert not_order([]) == 0
# assert not_order([1, 1, 1, 1, 1]) == 0
# assert not_order([1, 2, 3, 4, 5]) == 0
# 
# END_DESC

def not_order(data: list[int]) -> int:
    # your code here
    return 0


print("Example:")
print(not_order([1, 1, 4, 2, 1, 3]))

# These "asserts" are used for self-checking
assert not_order([1, 1, 4, 2, 1, 3]) == 3
assert not_order([]) == 0
assert not_order([1, 1, 1, 1, 1]) == 0
assert not_order([1, 2, 3, 4, 5]) == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")