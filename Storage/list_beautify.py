#!/usr/bin/env checkio --domain=py run list-beautify

# Let's assume, you are given a list of lists of positive/negative integer/float numbers, for example -[[1, 2, 10, 150], [10, 2, 1000, 2], [1, 120, 1, 1000]]. It's always correctly filled: has at least one non-empty inner list.
# 
# When you print it as a single object, you receive
# [[1, 2, 10, 150], [10, 2, 1000, 2], [1, 120, 1, 1000]]
#                 or row by row:
# [1, 2, 10, 150]
# [10, 2, 1000, 2]
# [1, 120, 1, 1000]
#                 
# 
# Your function should return something from both views and improved: asingle string(multiline if more than one inner list), where numbers in columns should be right-aligned. There must be exactly one whitespace between the longest number in a column incl. minus (if present) and the previous comma in a row. All rows of the same length, wrapped together in the list brackets.
# [[ 1,   2,   10,  150],
#  [10,   2, 1000,    2],
#  [ 1, 120,    1, 1000]]
#                 
# 
# Isn't it beautiful now 😍?
# 
# Input:List of lists of numbers.
# 
# Output:String.
# 
# Examples:
# 
# assert (
#     list_beautify([[1, 2, 10, 150], [10, 2, 1000, 2], [1, 120, 1, 1000]])
#     == "[[ 1,   2,   10,  150],\n [10,   2, 1000,    2],\n [ 1, 120,    1, 1000]]"
# )
# assert list_beautify([[1, 10, 100, -1000]]) == "[[1, 10, 100, -1000]]"
# assert (
#     list_beautify([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
#     == "[[1, 1, 1, 1, 1],\n [1, 1, 1, 1, 1],\n [1, 1, 1, 1, 1]]"
# )
# assert (
#     list_beautify([[1, 1, -1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
#     == "[[1, 1, -1, 1, 1],\n [1, 1,  1, 1, 1],\n [1, 1,  1, 1, 1]]"
# )
# 
# END_DESC

def list_beautify(data: list[list[int]]) -> str:
    # your code here
    return ""


print("Example:")
print(list_beautify([[1, 2, 10, 150], [10, 2, 1000, 2], [1, 120, 1, 1000]]))

# These "asserts" are used for self-checking
assert (
    list_beautify([[1, 2, 10, 150], [10, 2, 1000, 2], [1, 120, 1, 1000]])
    == "[[ 1,   2,   10,  150],\n [10,   2, 1000,    2],\n [ 1, 120,    1, 1000]]"
)
assert list_beautify([[1, 10, 100, -1000]]) == "[[1, 10, 100, -1000]]"
assert (
    list_beautify([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
    == "[[1, 1, 1, 1, 1],\n [1, 1, 1, 1, 1],\n [1, 1, 1, 1, 1]]"
)
assert (
    list_beautify([[1, 1, -1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
    == "[[1, 1, -1, 1, 1],\n [1, 1,  1, 1, 1],\n [1, 1,  1, 1, 1]]"
)

print("The mission is done! Click 'Check Solution' to earn rewards!")