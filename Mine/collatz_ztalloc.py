#!/usr/bin/env checkio --domain=py run collatz-ztalloc

# TheCollatz conjectureis one of the most famous unsolved problems in mathematics. However, the Collatz sequence can also be viewed in a binary fashion depending on whether each value stepsup(3x+1) ordown(x/2)  from the previous value, denoting these steps with"u", "d", respectively. For example, starting from n=12 here is the sequence and step shape:
# 
# 
# 
# Depending of thedatatype, you function must return the starting value (if string shape of letters"u", "d"is given) or shape of steps (if value is given).
# 
# This function must also recognize that some shape strings are impossible as entailed by the Collatz transition rules, and correctly returnNonefor all such shapes. You should start from the goal state 1, and perform  the given  transitions in reverse. Along  the way, you have  to ensure that your function does not accept moves that would be illegal in the original forward-going Collatz sequence.
# 
# Input:String(str)or integer(int).
# 
# Output:String(str), integer(int)or None.
# 
# Examples:
# 
# assert collatz_convert("ududududddddudddd") == 15
# assert collatz_convert(135) == "udududduddddududdudduddddudududdudddudddd"
# assert collatz_convert("dudududdudddudddd") == 14
# assert collatz_convert(10) == "dudddd"
# The mission was taken from Python CCPS 109. It is taught for Ryerson Chang School of Continuing Education byIlkka Kokkarinen
# 
# 
# END_DESC

def collatz_convert(data: int | str) -> int | str | None:
    # your code here
    return 0


print("Example:")
print(collatz_convert(10))

# These "asserts" are used for self-checking
assert collatz_convert("ududududddddudddd") == 15
assert collatz_convert(135) == "udududduddddududdudduddddudududdudddudddd"
assert collatz_convert("dudududdudddudddd") == 14
assert collatz_convert(10) == "dudddd"
assert collatz_convert("uduuudddd") == None

print("The mission is done! Click 'Check Solution' to earn rewards!")