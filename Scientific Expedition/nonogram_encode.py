#!/usr/bin/env checkio --domain=py run nonogram-encode

# I believe you love the picture logic puzzles callednonogramsand have solved many of them. This mission is the opposite: you already have a binary image, formed by strings of equal length,     where a background empty cell contains whitespace and a picture cell contains 'X'.
# 
# Your goal is to create a nonogram based upon the image: write number clues for solving the image like it was hidden. Your function     should return a list of two lists. The first one consists of     lists with numbers for the columns' clues and the second one     contains the same for the rows' clues. All lists of the columns' clues, as well as of     the rows' clues, should be of the same 'depth' (complemented with 0). Let's see an example:
# 
# 
# example = [' X X ',
#            'X X X', 
#            ' X X ']
#     Example with solution to see the whole idea:
# 
# 
#     columns clue 01010
#                  11111
# rows clue 0 1 1 ' X X '
#           1 1 1 'X X X'
#           0 1 1 ' X X '
#     So, for this example your function should return the following:
# 
# 
# result = [[[0, 1, 0, 1, 0],
#            [1, 1, 1, 1, 1]],
#           [[0, 1, 1],
#            [1, 1, 1],
#            [0, 1, 1]]]
# # the same, non formatted view
# [[[0, 1, 0, 1, 0], [1, 1, 1, 1, 1]], [[0, 1, 1], [1, 1, 1], [0, 1, 1]]]
#     
# 
# Input:List of strings.
# 
# Output:List of 2 lists.
# 
# Examples:
# 
# assert nonogram_encode([" X X ", "X X X", " X X "]) == [
#     [[0, 1, 0, 1, 0], [1, 1, 1, 1, 1]],
#     [[0, 1, 1], [1, 1, 1], [0, 1, 1]],
# ]
# assert nonogram_encode(["X"]) == [[[1]], [[1]]]
# Preconditions:len(data[i]) == len(data[0]);set(data[i]) == set([' ', 'X']);for lists in output: len(list[i]) == len(list[0]).
# 
# 
# END_DESC

def nonogram_encode(data: list[str]) -> list[list[list[int]]]:
    # your code here
    return []


print("Example:")
print(nonogram_encode([" X X ", "X X X", " X X "]))

# These "asserts" are used for self-checking
assert nonogram_encode([" X X ", "X X X", " X X "]) == [
    [[0, 1, 0, 1, 0], [1, 1, 1, 1, 1]],
    [[0, 1, 1], [1, 1, 1], [0, 1, 1]],
]
assert nonogram_encode(["X"]) == [[[1]], [[1]]]

print("The mission is done! Click 'Check Solution' to earn rewards!")