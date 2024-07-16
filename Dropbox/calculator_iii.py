#!/usr/bin/env checkio --domain=py run calculator-iii

# 
# 
# The fundamental difference between a calculator and computer is that a computer can be programmed in a way that allows the program to take different branches according to intermediate results, while calculators are pre-designed with specific functions built in. The distinction is not clear-cut: some devices classed as programmable calculators have programming functions, sometimes with support for programming languagesFind more on wikipedia page...
# 
# In this series of missions you are going to build an elementary calculator.
# 
# As an input, you get a sequence of keys pressed, and, as the result of that function, you should show what will be shown on the screen when the last key is pressed. Be attentive, it's not always the result of the expression. Actually, playing with the physical calculator or app will really helps you to catch edge cases.
# 
# Max digit space of 5 is added. It means that the maximum number you can enter is "99999".
# 
# Expected behavior:beginning zeros should be removed, only-zeros number - converted to single zero;among +- signs between numbers, the last one should be taken;"==" means repeating the last operation;"+=" or "-=" - adding/subtracting the number (or operations result) before the combination (doubling the number/subtracting itself);the calculator ignores digit you enter after 5th;"-" for numbers < 0 is NOT taking digit place;if the abs(result) is more than 99999 - "error" is shown as a result.
# 
# Input:String.
# 
# Output:String.
# 
# Examples:
# 
# assert calculator("90000+10000=") == "error"
# assert calculator("90000+10000-10000=") == "error"
# assert calculator("90000+10000-10000") == "10000"
# assert calculator("123456789") == "12345"
# Precondition:Allowed characters: digits (0-9), signs plus (+), minus (-) or equation (=) and their combinations (+=, +-, == etc.). The number may contain no more than 5 digits.
# 
# 
# END_DESC

def calculator(log: str) -> str:
    # your code here
    return ""


print("Example:")
print(calculator("100000"))

# These "asserts" are used for self-checking
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