#!/usr/bin/env checkio --domain=py run beat-the-previous

# Given a string of digits guaranteed to only contain ordinary integer digit characters 0 to 9, create and return the list of increasing integers acquired from reading these digits in order from left to right. The first integer in the result list is made up from the first digit of the string. After that, each element is an integer that consists of as many following consecutive digits as are needed to make that integerstrictly largerthan the previous integer. The leftover digits at the end of the digit string that do not form a sufficiently large integer are ignored.
# 
# This mission is quite easy, but we also have got a harder version -Staircase. Try it!
# 
# Input:String(str).
# 
# Output:Listof integers(int).
# 
# Examples:
# 
# assert beat_previous("600005") == [6]
# assert beat_previous("6000050") == [6, 50]
# assert beat_previous("045349") == [0, 4, 5, 34]
# assert beat_previous("77777777777777777777777") == [7, 77, 777, 7777, 77777, 777777]
# The mission was taken fromPython CCPS 109. It is taught forRyerson Chang School of Continuing EducationbyIlkka Kokkarinen
# 
# 
# END_DESC

def beat_previous(digits: str) -> list[int]:
    # your code here
    return []


print("Example:")
print(beat_previous("123"))

# These "asserts" are used for self-checking
assert beat_previous("600005") == [6]
assert beat_previous("6000050") == [6, 50]
assert beat_previous("045349") == [0, 4, 5, 34]
assert beat_previous("77777777777777777777777") == [7, 77, 777, 7777, 77777, 777777]

print("The mission is done! Click 'Check Solution' to earn rewards!")