#!/usr/bin/env checkio --domain=py run champernowne-word

# TheChampernowne word1234567891011121314151617181920212223…, also known as the counting series, is an infinitely long string of digits made up of all positive integers written out in ascending order without any separators. This function should return the digit at positionnof the Champernowne word. Position counting again starts from zero.
# 
# 
# 
# Click this line if you need a hint.This infinite sequence starts with nine single-digit numbers, followed by ninety two-digit numbers, followed by nine hundred three-digit numbers, and so on. Once you reach the block of k-digit numbers that contains the position n, the digit in that position is best determined with integer arithmetic, perhaps aided by anstrconversion for access to digit positions.
# 
# Input:Integer(int).
# 
# Output:Integer(int).
# 
# Examples:
# 
# assert counting_series(0) == 1
# assert counting_series(10) == 0
# assert counting_series(100) == 5
# The mission was taken from Python CCPS 109. It is taught for Ryerson Chang School of Continuing Education byIlkka Kokkarinen
# 
# 
# END_DESC

def counting_series(n: int) -> int:
    # your code here
    return 0


print("Example:")
print(counting_series(1))

# These "asserts" are used for self-checking
assert counting_series(0) == 1
assert counting_series(10) == 0
assert counting_series(100) == 5

print("The mission is done! Click 'Check Solution' to earn rewards!")