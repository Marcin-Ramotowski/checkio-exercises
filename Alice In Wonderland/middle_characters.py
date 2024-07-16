#!/usr/bin/env checkio --domain=py run middle-characters

# You are given some string where you need to find its middle characters. The string may contain one word, a few symbols or a whole sentence. If the length of the string is even, then you should return two middle characters, but if the length is odd, return just one. For more details look at the Example.
# 
# 
# 
# Input:A string.
# 
# Output:The middle characters.
# 
# Precondition:
# 1 <= the length of the text <= 100
# 
# 
# END_DESC

def middle(text):
    i = len(text) // 2
    return text[i] if len(text) % 2 == 1 else text[i-1:i+1]