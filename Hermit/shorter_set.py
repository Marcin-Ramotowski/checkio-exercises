#!/usr/bin/env checkio --domain=py run shorter-set

# In a given set of integers, you need to remove minimum and maximum elements.
# 
# The second argument tells how many min and max elements should be removed.
# 
# Input:Two arguments. Set of ints and int.
# 
# Output:Set of ints
# 
# 
# END_DESC

def remove_min_max(data: set, total:int) -> set:
    while data and total > 0:
        data.remove(min(data))
        if data:
            data.remove(max(data))
        total -= 1
    return data

print('Example:')
print(remove_min_max({4,5,6,7}, 1))

assert remove_min_max({8, 9, 18, 7}, 1) == {8, 9}
assert remove_min_max({8, 9, 7}, 0) == {8, 9, 7}
assert remove_min_max({8, 9, 7}, 2) == set()
assert remove_min_max({1, 2, 7, 8, 9}, 2) == {7}
assert remove_min_max(set(), 1) == set()

print("The first mission is done! Click 'Check' to earn cool rewards!")