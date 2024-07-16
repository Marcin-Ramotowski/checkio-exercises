#!/usr/bin/env checkio --domain=py run exploring-calkin-wilf-tree

# The nodes of theCalkin–Wilf tree, when read in level order so that the elements in each level are read from left to right, produce the linear sequence of all possible positive rational numbers. Almost as if by magic, this construction guarantees every positive integer fraction to appear exactly once in this sequence. Even more delightfully, this construction makes every rational number to make its appearance in its lowest reduced form!
# 
# The tree is rooted at the number 1 (1/1), and any rational number expressed in simplest terms as the fraction a/b has as its two children the numbers a/(a + b) and (a + b)/b.
# 
# 
# 
# Your function should return then:th element of this sequence. Notice, that once you reach the positionn//2 + 1, the queue already contains the result you need, so you can save a hefty chunk of time and space by not finding any new values. Besides, the linked Wikipedia page and other sources provide additional shortcuts to jump into the given position faster than sloughing your way the hard way there one element at a time.
# 
# Input:Integer(int).
# 
# Output:Two integers.
# 
# Examples:
# 
# assert calkin_wilf(1) == (1, 1)
# assert calkin_wilf(2) == (1, 2)
# assert calkin_wilf(3) == (2, 1)
# assert calkin_wilf(10) == (3, 5)
# The mission was taken fromPython CCPS 109. It is taught forRyerson Chang School of Continuing EducationbyIlkka Kokkarinen
# 
# 
# END_DESC

def calkin_wilf(n: int) -> tuple[int, int]:
    # your code here
    return 1, 1


print("Example:")
print(calkin_wilf(2))

# These "asserts" are used for self-checking
assert calkin_wilf(1) == (1, 1)
assert calkin_wilf(2) == (1, 2)
assert calkin_wilf(3) == (2, 1)
assert calkin_wilf(10) == (3, 5)
assert calkin_wilf(100) == (7, 19)

print("The mission is done! Click 'Check Solution' to earn rewards!")