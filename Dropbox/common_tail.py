#!/usr/bin/env checkio --domain=py run common-tail

# You are given two lists of integers.    Elements are unique inside each list.    These lists may have common element(s).    But we are interested in the common element(s) at the end of the lists.    Your function should return an element, from what a common part starts and there are no    different element(s) after this part - the first element of the last common part (common tail).    If there is no such element (lists    don't end with common element) your function should return None. Good luck!
# 
# Input:Two lists of integers.
# 
# Output:Integer or None.
# 
# Examples:
# 
# assert common_tail([], [1, 2, 3]) == None
# assert common_tail([1], [1]) == 1
# assert common_tail([3], [1, 2, 3]) == 3
# assert common_tail([1, 3, 4, 6], [2, 9, 4, 6]) == 4
# 
# END_DESC

def common_tail(a: list[int], b: list[int]) -> int | None:
    for i, el in enumerate(b):
        if el in a:
            slice1 = a[a.index(el):]
            slice2 = b[i:]
            if slice1 == slice2:
                return slice1[0]


print("Example:")
print(common_tail([1, 2, 3, 4], [5, 6, 3, 4]))

assert common_tail([], [1, 2, 3]) == None
assert common_tail([1], [1]) == 1
assert common_tail([3], [1, 2, 3]) == 3

print("The mission is done! Click 'Check Solution' to earn rewards!")