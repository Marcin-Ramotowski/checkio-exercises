#!/usr/bin/env checkio --domain=py run fibonacci-poem

# This mission is inspired by the following Brian Bilston's facebookpost:
# 
# 
# 
# Split a given text  into multiline one with "\n", where each line includes number of words equal to the currentFibonacci number.
# 
# Here are some clarifications:Fibonacci sequence starts from 0, 1, but the result string should include only non-empty lines;in case, there are not enough words for current line - complement to proper length with "_";punctuation marks are considered as a part of a previous or next word.
# 
# Let's look at the schematic example ("w" for a word):
# 
# 
# "w w w w w w w w" -> '''w
#                         w
#                         w w
#                         w w w
#                         w _ _ _ _'''
# Input:A string(str).
# 
# Output:A string(str).
# 
# Examples:
# 
# assert fibo_poem("") == ""
# assert fibo_poem("Django framework") == "Django\nframework"
# assert fibo_poem("Zen of Python") == "Zen\nof\nPython _"
# assert (
#     fibo_poem("There are three kinds of lies: Lies, damned lies, and the benchmarks.")
#     == "There\nare\nthree kinds\nof lies: Lies,\ndamned lies, and the benchmarks."
# )
# 
# END_DESC

def fibo_poem(text: str) -> str:
    # your code here
    return ""


print("Example:")
print(fibo_poem("Zen of Python"))

# These "asserts" are used for self-checking
assert fibo_poem("") == ""
assert fibo_poem("Django framework") == "Django\nframework"
assert fibo_poem("Zen of Python") == "Zen\nof\nPython _"
assert (
    fibo_poem("There are three kinds of lies: Lies, damned lies, and the benchmarks.")
    == "There\nare\nthree kinds\nof lies: Lies,\ndamned lies, and the benchmarks."
)

print("The mission is done! Click 'Check Solution' to earn rewards!")