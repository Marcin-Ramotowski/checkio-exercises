#!/usr/bin/env checkio --domain=py run grid-painting

# This mission paints designated cells in a 5x5 grid with a brush.    And return its minimum number of steps.
# 
# Each cell is assigned a letter of the alphabet from A to Y (Row-major order). Use this as input value.You can paint vertically (or horizontally) consecutive cells  with any width brush at a time.NOTE:Don't paint undesignated cells.The cell may be painted multiple times.
# 
# 
# 
# Input:Designated cells (str).
# 
# Output:Minimum number of steps (int).
# 
# Examples:
# 
# assert grid_painting("ABCFGHMRX") == 3
# assert grid_painting("GHLMNRS") == 2
# assert grid_painting("GHILNQRS") == 4
# 
# END_DESC

def grid_painting(cells: str) -> int:
    # your code here
    return 0


print("Example:")
print(grid_painting("ABCFGHMRX"))

# These "asserts" are used for self-checking
assert grid_painting("ABCFGHMRX") == 3
assert grid_painting("GHLMNRS") == 2
assert grid_painting("GHILNQRS") == 4

print("The mission is done! Click 'Check Solution' to earn rewards!")