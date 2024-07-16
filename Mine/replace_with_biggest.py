#!/usr/bin/env checkio --domain=py run replace-with-biggest

# You are given a list of integersdata. Replace every element in it with the biggest element among the elements to its strict right (not including current element). The last element should be replaced with-1. Return modified sequence as any Iterable.
# 
# Take a look at the following example:
# [17, 18, 5, 4, 6, 1] -> [18, 6, 6, 6, 1, -1]
# 
# 
# Explanation:data1[0]--> the greatest element to the right ofdata[0]is element at index1-18;data1[1]--> -//- at index4-6;data1[2]--> -//- at index4-6;data1[3]--> -//- at index4-6;data1[4]--> -//- at index5-1;data1[5]--> there are no elements to the right of element with index5, so we put-1.
# 
# Input:A list of integers.
# 
# Output:A list  or another Iterable (tuple, iterator, generator) of integers.
# 
# Examples:
# 
# assert list(replace_biggest([17, 18, 5, 4, 6, 1])) == [18, 6, 6, 6, 1, -1]
# assert list(replace_biggest([1, 2, 3, 4, 5, 6])) == [6, 6, 6, 6, 6, -1]
# assert list(replace_biggest([1, 1, 1])) == [1, 1, -1]
# 
# END_DESC

from typing import Iterable


def replace_biggest(data: list[int]) -> Iterable[int]:
    # your code here
    return []


print("Example:")
print(list(replace_biggest([17, 18, 5, 4, 6, 1])))

# These "asserts" are used for self-checking
assert list(replace_biggest([17, 18, 5, 4, 6, 1])) == [18, 6, 6, 6, 1, -1]
assert list(replace_biggest([1, 2, 3, 4, 5, 6])) == [6, 6, 6, 6, 6, -1]
assert list(replace_biggest([1, 1, 1])) == [1, 1, -1]

print("The mission is done! Click 'Check Solution' to earn rewards!")