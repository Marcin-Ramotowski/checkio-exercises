#!/usr/bin/env checkio --domain=py run excel-column-number

# Given a string that represents the column title as appears in an Excel sheet, return its corresponding column number.
# 
# Input:String.
# 
# Output:Int.
# 
# 
# END_DESC

column_number = lambda name: sum((ord(letter)-64) * 26 ** i for i, letter in enumerate(name[::-1]))


print("Example:")
print(column_number("AA"))

assert column_number("A") == 1
assert column_number("Z") == 26
assert column_number("AB") == 28
assert column_number("ZY") == 701

print("The first mission is done! Click 'Check' to earn cool rewards!")