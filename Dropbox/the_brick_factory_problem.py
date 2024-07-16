#!/usr/bin/env checkio --domain=py run the-brick-factory-problem

# .video-container {    position: relative;    max-width: 560px; /* Maximum width in pixels */    margin: 0 auto; /* Center the container horizontally */    padding-bottom: 56.25%; /* 16:9 aspect ratio */}.video-container iframe {    position: absolute;    top: 0;    left: 0;    width: 100%;    height: 100%;}Imagine you are at the brick factory making bricks. You have a number of kilnskand a number of storagess. And you want to connect every kiln with every storage with the minimum possible number of tracks intersections. Notice, that it's not necessary for tracks to be straight (scheme 1).
# 
# Another variant of this problem is to find the minimum number of intersections while connecting every element with all others inksequence (scheme 2).
# 
# 
# 
# Your function must return the minimum number of intersections in the variant 1 (two arguments) or variant 2 (one argument), depending of the number of given arguments.
# 
# Here is a video with wider explanation of the problems, examples, schemes and formulas 😉. Notice, that the formulas are not fully proven yet and it may be your next own study!
# 
# 
# 
# Input:Two or one integer(int)
# 
# Output:Integer.
# 
# Examples:
# 
# assert crosses(1, 1) == 0
# assert crosses(5) == 1
# assert crosses(5, 5) == 16
# assert crosses(7) == 9
# 
# END_DESC

def crosses(k: int, s: int = None) -> int:
    # your code here
    return 0


print("Example:")
print(crosses(6, 5))

# These "asserts" are used for self-checking
assert crosses(1, 1) == 0
assert crosses(5) == 1
assert crosses(5, 5) == 16
assert crosses(7) == 9
assert crosses(9, 0) == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")