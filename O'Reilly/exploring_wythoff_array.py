#!/usr/bin/env checkio --domain=py run exploring-wythoff-array

# Wythoff array(see also theWikipedia articlefor illustration) is an infinite two-dimensional grid of integers that is seeded with1and2to start off the first row. In each row, each element equals the sum of the previous two elements, so the first row contains precisely theFibonacci numbers.
# 
# The first element of each row after the first isthe smallest integer c that does not appear anywhere in the previous rows. Since every row is strictly ascending and grows exponentially fast, you can find this out by looking at relatively short finite prefixes of these rows. To determine the second element of that row, letaandbbe the first two elements of the previous row. If the differencec-aequals2, the second element of that row equalsb+3, and otherwise that element equalsb+5.
# 
# This construction guarantees the Wythoff array to be aninterspersionof positive integers; every positive integer will appearexactly oncein the entire infinite grid, with no gaps or duplicates anywhere! (This result also nicely highlights the deeper combinatorial importance of the deceptively simple Fibonacci numbers as potential building blocks of integers and their sequences.)
# 
# This function should return the position ofnin the Wythoff array as tuple(row, col), rows and columns both starting from zero.
# 
# Input:Integer(int).
# 
# Output:Position astupleof two integers.
# 
# Examples:
# 
# assert wythoff_array(21) == (0, 6)
# assert wythoff_array(47) == (1, 5)
# assert wythoff_array(1042) == (8, 8)
# The mission was taken fromPython CCPS 109. It is taught forRyerson Chang School of Continuing EducationbyIlkka Kokkarinen
# 
# 
# END_DESC

def wythoff_array(n: int) -> tuple[int, int]:
    # your code here
    return (0, 0)


print("Example:")
print(wythoff_array(3))

# These "asserts" are used for self-checking
assert wythoff_array(21) == (0, 6)
assert wythoff_array(47) == (1, 5)
assert wythoff_array(1042) == (8, 8)

print("The mission is done! Click 'Check Solution' to earn rewards!")