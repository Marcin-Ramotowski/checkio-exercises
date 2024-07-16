#!/usr/bin/env checkio --domain=py run calculator-ii

# 
# 
# In addition to general purpose calculators, there are those designed for specific markets. For example, there are scientific calculators which include trigonometric and statistical calculations. Some calculators even have the ability to do computer algebra. Graphing calculators can be used to graph functions defined on the real line, or higher-dimensional Euclidean space.Find more on wikipedia page...
# 
# In this series of missions you are going to build an elementary calculator.
# 
# As an input, you get a sequence of keys pressed, and, as the result of that function, you should show what will be shown on the screen when the last key is pressed. Be attentive, it's not always the result of the expression. Actually, playing with the physical calculator or app will really help you to catch edge cases.
# 
# In this mission the combinations of signs are presented.
# 
# Expected behavior:beginning zeros should be removed, only-zeros number - converted to single zero;among +- signs between numbers, the last one should be taken;"==" means repeating the last operation;"+=" or "-=" - adding/subtracting the number (or operations result) before the combination (doubling the number/subtracting itself).
# 
# Input:String.
# 
# Output:String.
# 
# Examples:
# 
# assert calculator("3+=") == "6"
# assert calculator("3+2==") == "7"
# assert calculator("4-1==") == "2"
# assert calculator("3+-2=") == "1"
# Precondition:Allowed characters: digits (0-9), signs plus (+), minus (-) or equation (=) and their combinations (+=, +-, == etc.).
# 
# 
# END_DESC

def calculator(log: str) -> str:
    # your code here
    return ""


print("Example:")
print(calculator("3+="))

# These "asserts" are used for self-checking
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