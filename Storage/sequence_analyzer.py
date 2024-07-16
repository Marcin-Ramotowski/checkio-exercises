#!/usr/bin/env checkio --domain=py run sequence-analyzer

# Consider a sequence of uppercase alphabetic characters (A-Z). The sequence is said to have a "constant step" if the distance between adjacent characters in the sequence is the same. For example, the distance between A and B is 1, D and F is 2, P and V is 6, Z and C is 3 etc. Note that "wraparound" from Z to C is defined. The following sequences have a "constant step":
# 
# 
#     ACEG... step = 2
#     AZYX... step = 25
# Two or mor sequences are said to be "intertwined" if their adjacent elements are separated by exactly one element of each of the other sequences. For example, the following sequences are intertwined:
# 
# 
#     AQBRCSDT... sequences: ABCD... step = 1
#                            QRST... step = 1
#     AZTAYRAXP...sequences:  AAA... step = 0
#                             ZYX... step = 25
#                             TRP... step = 24
# For the given string of 12 characters of 1, 2 or 3 (find out it by yourself) intertwined sequences, return the next 12 character of the sequence.
# 
# 
# 
# Input:String(str).
# 
# Output:String(str).
# 
# Examples:
# 
# assert analyzer("ACEGIKMOQSUW") == "YACEGIKMOQSU"
# assert analyzer("AQBRCSDTEUFV") == "GWHXIYJZKALB"
# assert analyzer("AZTAYRAXPAWN") == "AVLAUJATHASF"
# The mission was taken fromThe International Collegiate Programming Contest - 1980.
# 
# 
# END_DESC

def analyzer(seq: str) -> str:
    # your code here
    return ""


print("Example:")
print(analyzer("ACEGIKMOQSUW"))

# These "asserts" are used for self-checking
assert analyzer("ACEGIKMOQSUW") == "YACEGIKMOQSU"
assert analyzer("AQBRCSDTEUFV") == "GWHXIYJZKALB"
assert analyzer("AZTAYRAXPAWN") == "AVLAUJATHASF"

print("The mission is done! Click 'Check Solution' to earn rewards!")