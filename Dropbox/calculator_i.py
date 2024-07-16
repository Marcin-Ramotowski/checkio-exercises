#!/usr/bin/env checkio --domain=py run calculator-i

# 
# 
# The first solid-state electronic calculator was created in the early 1960s. Pocket-sized devices became available in the 1970s, especially after the Intel 4004, the first microprocessor, was developed by Intel for the Japanese calculator company Busicom. They later became used commonly within the petroleum industry (oil and gas).Find more on wikipedia page...
# 
# In this series of missions you are going to build an elementary calculator.
# 
# As an input, you get a sequence of keys pressed, and, as the result of that function, you should show what will be shown on the screen when the last key is pressed. Be attentive, it's not always the result of the expression. Actually, playing with the physical calculator or app will really help you to catch edge cases.
# 
# In the first mission only digits and single signs (only +, -, =) between them are used.
# 
# Expected behavior:beginning zeros should be removed, only-zeros number - converted to single zero.
# 
# Input:String.
# 
# Output:String.
# 
# Examples:
# 
# assert calculator("000000") == "0"
# assert calculator("0000123") == "123"
# assert calculator("12") == "12"
# assert calculator("+12") == "12"
# Precondition:Allowed characters: digits (0-9), single signs plus (+), minus (-) or equation (=) between digit blocks. NO combinations of signs (+=, +- etc.).
# 
# 
# END_DESC

def calculator(log: str) -> str:
    # your code here
    return ""


print("Example:")
print(calculator("1+2"))

# These "asserts" are used for self-checking
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