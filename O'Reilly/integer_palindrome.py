#!/usr/bin/env checkio --domain=py run integer-palindrome

# You need to determine whether the given integer (in base10) is a palindrome or not in baseB. Base (or radix) is written as subscript text.    A number is a palindrome if it reads the same in both directions, for example12110is a palindrome, and12210is not.    If the integerBis a palindrome, returnTrue, if not, returnFalse.Read more about number bases.
# 
# The most common base is decimal. To convert an integer10to another base you need to divide it by base and take reminders until the number becomes equal zero. Let's look at the following example - convert integer610into the binary form62.
# 
# IntegerQuotientReminderNormalReversed6300031110011011100110Since reversed011is not equal normal110-62is not a palindrome.
# 
# To return back to the decimal form, start from zero, multiply by base and add reminders. For62== 110it's(((0*2) + 1)*2 + 1)*2 + 0 = 6.
# 
# Input:Given integer and base B (integer).
# 
# Output:Bool.
# 
# Preconditions:number >= 0;number is integer;B >= 2;B is integer.
# 
# 
# END_DESC

import string

def int_palindrome(number: int, B: int) -> bool:
    CHARS = string.printable
    if B != 10:
        str_number = ''
        while number:
            number, rest = divmod(number, B)
            str_number = CHARS[rest] + str_number
    else:
        str_number = str(number)
    return str_number == str_number[::-1]


print("Example:")
print(int_palindrome(455, 2))

assert int_palindrome(6, 2) == False
assert int_palindrome(34, 2) == False
assert int_palindrome(455, 2) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")