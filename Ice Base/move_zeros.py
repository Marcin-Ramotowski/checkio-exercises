#!/usr/bin/env checkio --domain=py run move-zeros

# You are given a list of integers.    Move all zeros in the list to the end of it.    The order of non-zero elements should not change.
# 
# Input:A list of integers.
# 
# Output:A list or another Iterable (tuple, genenator, iterator) of integers.
# 
# Examples:
# 
# assert list(move_zeros([0, 1, 0, 3, 12])) == [1, 3, 12, 0, 0]
# assert list(move_zeros([0])) == [0]
# 
# END_DESC

def move_zeros(items: list[int]) -> list[int]:
    return list(filter(bool, items)) + [0] * items.count(0)


print("Example:")
print(move_zeros([0, 1, 0, 3, 12]))

assert move_zeros([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
assert move_zeros([0]) == [0]

print("The mission is done! Click 'Check Solution' to earn rewards!")