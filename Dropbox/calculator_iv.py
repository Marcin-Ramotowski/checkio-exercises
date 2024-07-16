#!/usr/bin/env checkio --domain=py run calculator-iv

# 
# 
# The first known tools used to aid arithmetic calculations were: bones (used to tally items), pebbles, and counting boards, and the abacus, known to have been used by Sumerians and Egyptians before 2000 BC. Except for the Antikythera mechanism (an "out of the time" astronomical device), development of computing tools arrived near the start of the 17th century: the geometric-military compass (by Galileo), logarithms and Napier bones (by Napier), and the slide rule (by Edmund Gunter).Find more on wikipedia page...
# 
# In this series of missions you are going to build an elementary calculator.
# 
# As an input, you get a sequence of keys pressed, and, as the result of that function, you should show what will be shown on the screen when the last key is pressed. Be attentive, it's not always the result of the expression. Actually, playing with the physical calculator or app will really helps you to catch edge cases.
# 
# In the forth mission float numbers are allowed. The "." takes space as one digit, so max digit space is 4 for float number results. It means that the maximum float number you can enter is "9999.".
# 
# Expected behavior:beginning zeros should be removed, only-zeros number - converted to single zero;among +- signs between numbers, the last one should be taken;"==" means repeating the last operation;"+=" or "-=" - adding/subtracting the number (or operations result) before the combination (doubling the number/subtracting itself);the calculator ignores digit you enter after 5th;"-" for numbers < 0 is NOT taking digit place;if the abs(result) is more than 99999 - "error" is shown as a result;for float, if the integer part of abs(result) is more then 9999 - "error" is shown as a result;for float, in case the total length of number is more than 5 digits, it should be rounded to 5 digits (1.23456 -> 1.235);for float, beginning and trailing zeros should be removed (until the "." if possible): 0.1200 -> .12 ,  123.00 -> 123. . It should be done after the rounding: 1.000123 -> 1. . Stripping of trailing zeros should only be done after entering a number has concluded (non-digit character pressed).
# 
# Input:String.
# 
# Output:String.
# 
# Examples:
# 
# assert calculator("0001.1000") == "1.100"
# assert calculator("0001.1000-") == "1.1"
# assert calculator("999.9999999+=") == "2000."
# assert calculator("1.000123") == "1.000"
# Precondition:Allowed characters: digits (0-9), dot (.), signs plus (+), minus (-) or equation (=) and their combinations (+=, +-, == etc.). The integer number may contain no more than 5 digits, float - 4.
# 
# 
# END_DESC

def calculator(log: str) -> str:
    # your code here
    return ""


print("Example:")
print(calculator("0001.1000"))

# These "asserts" are used for self-checking
assert calculator("0001.1000") == "1.100"
assert calculator("0001.1000-") == "1.1"
assert calculator("999.9999999+=") == "2000."
assert calculator("1.000123") == "1.000"
assert calculator("9999.9999999+=") == "error"
assert calculator("90000+10000=") == "error"
assert calculator("90000+10000-10000=") == "error"
assert calculator("90000+10000-10000") == "10000"
assert calculator("123456789") == "12345"
assert calculator("123456789+5=") == "12350"
assert calculator("5+123456789") == "12345"
assert calculator("50000+=") == "error"
assert calculator("3+=") == "6"
assert calculator("3+2==") == "7"
assert calculator("4-1==") == "2"
assert calculator("3+-2=") == "1"
assert calculator("-=-+3-++--+-2=-") == "1"
assert calculator("000000") == "0"
assert calculator("0000123") == "123"
assert calculator("12") == "12"
assert calculator("+12") == "12"
assert calculator("") == "0"
assert calculator("1+2") == "2"
assert calculator("2+") == "2"
assert calculator("1+2=") == "3"
assert calculator("1+2-") == "3"
assert calculator("1+2=2") == "2"
assert calculator("=5=10=15") == "15"

print("The mission is done! Click 'Check Solution' to earn rewards!")