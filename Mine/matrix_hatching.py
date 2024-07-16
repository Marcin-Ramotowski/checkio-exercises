#!/usr/bin/env checkio --domain=py run matrix-hatching

# You are given a 2-dimensional matrix: a list of lists of integers. Your function should return another Iterable of lists, where each inner list is a sequence of matrix elements on the same diagonal "stroke". The order of elements in the "stroke" is SW -> NE. So, building these sequences is like "hatching" the matrix!
# 
# Let's look at the example. The matrix may NOT be square!
# 
# 
# 
# Input:List of lists of integers.
# 
# Output:List or another Iterable (generator, iterator) of lists of integers.
# 
# Examples:
# 
# assert list(hatching([[0]])) == [[0]]
# assert list(hatching([[1, 2], [3, 4]])) == [[1], [3, 2], [4]]
# assert list(hatching([[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]])) == [
#     [1],
#     [6, 2],
#     [7, 3],
#     [8, 4],
#     [9, 5],
#     [0],
# ]
# assert list(hatching([[1, 2], [3, 4], [5, 6], [7, 8], [9, 0]])) == [
#     [1],
#     [3, 2],
#     [5, 4],
#     [7, 6],
#     [9, 8],
#     [0],
# ]
# 
# END_DESC

from typing import Iterable


def hatching(matrix: list[list[int]]) -> Iterable[list[int]]:
    # your code here
    return [[]]


print("Example:")
print(list(hatching([[1, 2], [3, 4]])))

# These "asserts" are used for self-checking
assert list(hatching([[0]])) == [[0]]
assert list(hatching([[1, 2], [3, 4]])) == [[1], [3, 2], [4]]
assert list(hatching([[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]])) == [
    [1],
    [6, 2],
    [7, 3],
    [8, 4],
    [9, 5],
    [0],
]
assert list(hatching([[1, 2], [3, 4], [5, 6], [7, 8], [9, 0]])) == [
    [1],
    [3, 2],
    [5, 4],
    [7, 6],
    [9, 8],
    [0],
]

print("The mission is done! Click 'Check Solution' to earn rewards!")