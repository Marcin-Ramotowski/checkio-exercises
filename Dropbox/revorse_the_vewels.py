#!/usr/bin/env checkio --domain=py run revorse-the-vewels

# Given atextstring, create and return a new string constructed by finding all its vowels and reversing their order, while keeping all other characters exactly as they were in their original positions. To make the result more presentable, the capitalization of each position must remain the same as it was in the original text.
# 
# For example, reversing the vowels of"Ilkka"should produce"Alkki"instead of"alkkI". For this problem, vowels are the usual"aeiouAEIOU". Let's look at another example.
# 
# 
# 
# Input:String(str).
# 
# Output:String(str).
# 
# Examples:
# 
# assert reverse_vowels("Bengt Hilgursson") == "Bongt Hulgirssen"
# assert (
#     reverse_vowels("Why do you laugh? I chose death.")
#     == "Why da yee loigh? U chasu dooth."
# )
# assert (
#     reverse_vowels("These are the people you protect with your pain!")
#     == "Thisa uro thi peoplu yoe protect weth year peen!"
# )
# The mission was taken from Python CCPS 109. It is taught for Ryerson Chang School of Continuing Education byIlkka Kokkarinen
# 
# 
# END_DESC

def reverse_vowels(text: str) -> str:
    # your code here
    return ""


print("Example:")
print(reverse_vowels("Hello, World"))

# These "asserts" are used for self-checking
assert reverse_vowels("Bengt Hilgursson") == "Bongt Hulgirssen"
assert (
    reverse_vowels("Why do you laugh? I chose death.")
    == "Why da yee loigh? U chasu dooth."
)
assert (
    reverse_vowels("These are the people you protect with your pain!")
    == "Thisa uro thi peoplu yoe protect weth year peen!"
)

print("The mission is done! Click 'Check Solution' to earn rewards!")