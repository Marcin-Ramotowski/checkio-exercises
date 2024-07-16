#!/usr/bin/env checkio --domain=py run count-and-say

# Given a string of digits that is guaranteed to contain only digit characters from0123456789, read that string “out loud” by saying how many times each digit occurs consecutively in the current bunch of digits, and then return the string of digits that you just said out loud.
# 
# 
# 
# As silly and straightforward as thiscount-and-say sequenceproblem might initially seem, it required the genius of a mathematician of no lesser caliber than the late greatJohn Conwayhimself not only to notice the tremendous complexity ready to burst out from just below the surface when this operation is repeatedly iterated to produce an infinite sequence of such digit strings, but also capture that whole mess into a symbolic polynomial equation, as the man himself explains in this video.
# 
# 
# 
# You can also check out the related construct of the infinitely long and yet perfectly self-describingKolakoski sequencewhere only the lengths of each consecutive block of digits is written into the result string, not the actual digits.
# 
# 
# 
# Input:String(str).
# 
# Output:String(str).
# 
# Examples:
# 
# assert count_and_say("333388822211177") == "4338323127"
# assert count_and_say("1") == "11"
# assert count_and_say("") == ""
# The mission was taken from Python CCPS 109. It is taught for Ryerson Chang School of Continuing Education byIlkka Kokkarinen
# 
# 
# END_DESC

def count_and_say(digits: str) -> str:
    # your code here
    return ""


print("Example:")
print(count_and_say("123"))

# These "asserts" are used for self-checking
assert count_and_say("333388822211177") == "4338323127"
assert count_and_say("1") == "11"
assert count_and_say("") == ""

print("The mission is done! Click 'Check Solution' to earn rewards!")