#!/usr/bin/env checkio --domain=py run toothpicks

# This task is adapted from following video with Neil Sloane (founder of theOn-Line Encyclopedia of Integer Sequences). There are a few interesting sequences are shown in the video (so I recommend you to watch it all), but this particular mission is dedicated to the very first one -toothpicks sequence.
# 
# 
# 
# So, you have an infinite number of toothpicks of equal length and put them down on the table according to the rule. On the first step you just put one toothpick. It has two free ends, on which on the second step you respectively put two toothpicks perpendicularly. Now you have four free ends and put the next four toothpicks on the step three. If two toothpicks ends touch each other, the are not free, so after step three you again have four free end and so on.
# 
# Theplaygroundof this and other patterns may be seen on thepage. It will be easier to solve the task and it's just a beautiful hypnotic view!)
# 
# So, your function must return the number of toothpicks, placed on the table, afterstepsteps.
# 
# Input:Number of steps as integer.
# 
# Output:Number of toothpicks as integer.
# 
# Examples:
# 
# assert toothpicks(1) == 1
# assert toothpicks(2) == 3
# assert toothpicks(3) == 7
# assert toothpicks(4) == 11
# 
# END_DESC

def toothpicks(step: int) -> int:
    # your code here
    return 0


print("Example:")
print(toothpicks(2))

# These "asserts" are used for self-checking
assert toothpicks(1) == 1
assert toothpicks(2) == 3
assert toothpicks(3) == 7
assert toothpicks(4) == 11
assert toothpicks(5) == 15

print("The mission is done! Click 'Check Solution' to earn rewards!")