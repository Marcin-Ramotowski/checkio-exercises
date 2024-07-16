#!/usr/bin/env checkio --domain=py run rolling

# There is a standard 6-sided 🎲, which looks and placed as shown below. It may be rolled in four cardinal directions:North,South,West,East.
# 
# 
# 
# For the mission you are given a stringmoveswith directions. You need to find out, what side of 🎲 is on top after rolling.
# 
# Input:String with directions of rolling.
# 
# Output:Number of side, which is on top.
# 
# Examples:
# 
# assert rolling_dice("SN") == 1
# assert rolling_dice("") == 1
# assert rolling_dice("EESWN") == 6
# assert rolling_dice("NWSNWEESNW") == 3
# The mission was taken fromAIZU ONLINE JUDGE (ITP1_11_A: Dice I).
# 
# 
# END_DESC

def rolling_dice(moves: str) -> int:
    # your code here
    return 0


print("Example:")
print(rolling_dice("SE"))

# These "asserts" are used for self-checking
assert rolling_dice("SN") == 1
assert rolling_dice("") == 1
assert rolling_dice("EESWN") == 6
assert rolling_dice("NWSNWEESNW") == 3
assert rolling_dice("NNNSESNESWNENSWNNWSWNSSNWWSWNW") == 5

print("The mission is done! Click 'Check Solution' to earn rewards!")