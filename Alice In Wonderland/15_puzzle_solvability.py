#!/usr/bin/env checkio --domain=py run 15-puzzle-solvability

# 15-puzzleis a quite old and famous puzzle, which had its own peak of interest!
# 
# In this mission you are given apositionof tiles - a list of 4 lists of equal length with all integers from 1 to 16 incl. in arbitrary order (but number 16 always stands for empty place!). Your function should return a boolean value, if this combination of tiles is solvable (may be transformed by valid moves to "normal" order) or not, asTrueorFalserespectively.
# 
# Here is an interesting video about the puzzle itself and its solvability problem with the algorithm of checking explained. So if you don't like spoilers, you may try to solve the mission first without watching the video.
# 
# 
# 
# Input:A position of tiles as a list of 4 lists of integers from 1 to 16 incl.
# 
# Output:Solvability of puzzle as boolean value.
# 
# Examples:
# 
# assert (
#     fifteen_puzzle([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
#     == True
# )
# assert (
#     fifteen_puzzle([[15, 14, 13, 12], [11, 10, 9, 8], [7, 6, 5, 4], [3, 2, 1, 16]])
#     == False
# )
# assert (
#     fifteen_puzzle([[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]])
#     == True
# )
# assert (
#     fifteen_puzzle([[1, 3, 2, 4], [5, 7, 6, 8], [9, 11, 10, 12], [13, 15, 14, 16]])
#     == True
# )
# Preconditions:len(position) == len(position[i]) == 4;set(sum(position, [])) == {1, 2, ... 16}.
# 
# 
# END_DESC

def fifteen_puzzle(position: list[list[int]]) -> bool:
    # your code here
    return False


print("Example:")
print(fifteen_puzzle([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))

# These "asserts" are used for self-checking
assert (
    fifteen_puzzle([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
    == True
)
assert (
    fifteen_puzzle([[15, 14, 13, 12], [11, 10, 9, 8], [7, 6, 5, 4], [3, 2, 1, 16]])
    == False
)
assert (
    fifteen_puzzle([[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]])
    == True
)
assert (
    fifteen_puzzle([[1, 3, 2, 4], [5, 7, 6, 8], [9, 11, 10, 12], [13, 15, 14, 16]])
    == True
)
assert (
    fifteen_puzzle([[1, 9, 2, 10], [3, 11, 4, 12], [5, 13, 6, 14], [7, 15, 8, 16]])
    == True
)
assert (
    fifteen_puzzle([[1, 4, 5, 8], [2, 3, 6, 7], [9, 10, 13, 14], [16, 11, 12, 15]])
    == True
)
assert (
    fifteen_puzzle([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 15, 14, 16]])
    == False
)

print("The mission is done! Click 'Check Solution' to earn rewards!")