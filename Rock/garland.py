#!/usr/bin/env checkio --domain=py run garland

# 
# 
# You are given a sequencelights, where each integer is a distinct light with itsbrightness. This value determines how many adjacent positions to both left and right the illumination from that light reaches, in addition to illuminating the position of that light itself. (A light whose brightness is zero will therefore illuminate only itself, but doesn’t have anything to shine on its neighbors).
# 
# Your task is to turn on as few individual lights as possible so that every position of the entire row is illuminated by at least one light. Since the smallest working subset of lights is not necessarily unique, your function should only return the number of lights needed to illuminate the entire row.
# 
# Input:Listof integers(int).
# 
# Output:Integer(int).
# 
# Examples:
# 
# assert illuminate_all([0, 0]) == 2
# assert illuminate_all([2, 3, 3, 2]) == 1
# assert illuminate_all([1, 0, 1, 0]) == 2
# The mission was taken fromPython CCPS 109. It is taught forRyerson Chang School of Continuing EducationbyIlkka Kokkarinen
# 
# 
# END_DESC

def illuminate_all(lights: list[int]) -> int:
    # your code here
    return 0


print("Example:")
print(illuminate_all([0, 0]))

# These "asserts" are used for self-checking
assert illuminate_all([0, 0]) == 2
assert illuminate_all([2, 3, 3, 2]) == 1
assert illuminate_all([1, 0, 1, 0]) == 2

print("The mission is done! Click 'Check Solution' to earn rewards!")