#!/usr/bin/env checkio --domain=py run stepping-stones-puzzle

# This task is adapted from following video with Neil Sloane (founder of theOn-Line Encyclopedia of Integer Sequences), that you should watch first to learn, how this excellent puzzle works.
# 
# 
# 
# You have got a certain number of 🟤 stones (1 point each) anywhere on the board. Now you add ⚪ stones with increasing points value (2, 3, 4 ...) on the board. The rule of placement is: you can only put down a ⚪ stone with valuekif sum of values of its eight neighbors (🟤 and/or ⚪) isk.
# 
# To keep this problem manageable, the placement of stones is restricted into a finiten * nchessboard, whose edges the stones cannot cross into the void. As usual, rows and columns are numbered starting from zero.
# 
# Starting the placement from stone number2, consecutively (no value skipping allowed) numbered stones are placed on board in ascending order so that the moment that the stone numberkis placed somewhere, the stones previously placed into its up to eight neighboring locations add up to exactlyk.
# 
# Given the board sizenand the initial coordinates of the 🟤ones, your function should return the highest numbered stone in the longest sequence of stones that can be placed consecutively on the board within the rules of the puzzle.
# 
# Input:Two arguments: integer, list of tuples of 2 integers.
# 
# Output:Integer.
# 
# Examples:
# 
# assert stepping_stones(4, [(0, 0), (3, 3)]) == 1
# assert stepping_stones(5, [(0, 1), (1, 1), (2, 2)]) == 10
# assert stepping_stones(6, [(2, 0), (5, 3), (1, 3), (0, 0)]) == 19
# This task is taken from the course CCPS 109 Computer Science I, Version of December 21, 2022, as taught byIlkka Kokkarinen.
# 
# 
# END_DESC

def stepping_stones(n: int, ones: list[tuple[int, int]]) -> int:
    # your code here
    return 0


print("Example:")
print(stepping_stones(4, [(0, 0), (3, 3)]))

# These "asserts" are used for self-checking
assert stepping_stones(4, [(0, 0), (3, 3)]) == 1
assert stepping_stones(5, [(0, 1), (1, 1), (2, 2)]) == 10
assert stepping_stones(6, [(2, 0), (5, 3), (1, 3), (0, 0)]) == 19

print("The mission is done! Click 'Check Solution' to earn rewards!")