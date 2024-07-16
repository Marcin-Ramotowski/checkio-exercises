#!/usr/bin/env checkio --domain=py run gator-and-ducks

# Suppose there areducksfloating on the pond in a circle. The pond is also home for alligator with a fondness for ducks. Beginning at a particular position (duck number 1) the alligator counts clockwise around the circle and eats everystep-th duck (the circle closing as ducks are eaten).
# 
# For example, whenducks = 8andstep = 4, the following diagram shows duck number outside and consumption order inside:
# 
# 
# 
# The first duck is fifth on the menu, the second is forth, etc. The sequence5, 4, 6, 1, 3, 8, 7, 2of orders of consumption completely describes alligator's menu.
# 
# Write a script which returns the orders of consumption of the ducks givenducks, step.
# 
# Input:Two integers(int).
# 
# Output:Listof integers.
# 
# Examples:
# 
# assert gator(8, 4) == [5, 4, 6, 1, 3, 8, 7, 2]
# assert gator(7, 11) == [7, 2, 3, 1, 5, 6, 4]
# assert gator(3, 1) == [1, 2, 3]
# Precondition:ducks, step > 0
# 
# The mission was taken fromThe International Collegiate Programming Contest - 1974.
# 
# 
# END_DESC

def gator(ducks: int, step: int) -> list[int]:
    # your code here
    return []


print("Example:")
print(gator(3, 2))

# These "asserts" are used for self-checking
assert gator(8, 4) == [5, 4, 6, 1, 3, 8, 7, 2]
assert gator(7, 11) == [7, 2, 3, 1, 5, 6, 4]
assert gator(3, 1) == [1, 2, 3]

print("The mission is done! Click 'Check Solution' to earn rewards!")