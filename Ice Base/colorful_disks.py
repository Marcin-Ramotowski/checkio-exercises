#!/usr/bin/env checkio --domain=py run colorful-disks

# Colorful Disks is a game played on a base with vertical stick and some paper disks with a hole in the center. The disks all have different radiuses and colors. When all the disks are stacked on top of each other, the number of colors that can be seen from above is the score in this game. So, disks that cannot be seen from above are not scored.
# 
# 
# 
# Given the radiuses of the disks in order of placing on the stick (from the bottom one to the top one), calculate the score when all the disks are stacked.
# 
# Input:Tuple of integers(int).
# 
# Output:Integer(int).
# 
# Examples:
# 
# assert count_discs((3, 6, 7, 4, 5, 1, 2)) == 3
# assert count_discs((6, 5, 4, 3, 2, 1)) == 6
# assert count_discs((5,)) == 1
# This mission was taken fromAIZU ONLINE JUDGE
# 
# 
# END_DESC

def count_discs(discs: tuple[int, ...]) -> int:
    # your code here
    return 0


print("Example:")
print(count_discs((3, 2)))

# These "asserts" are used for self-checking
assert count_discs((3, 6, 7, 4, 5, 1, 2)) == 3
assert count_discs((6, 5, 4, 3, 2, 1)) == 6
assert count_discs((5,)) == 1

print("The mission is done! Click 'Check Solution' to earn rewards!")