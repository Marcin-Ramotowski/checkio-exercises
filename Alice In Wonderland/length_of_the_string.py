#!/usr/bin/env checkio --domain=py run length-of-the-string

# Your function should return the length of the given string
# 
# Input:String.
# 
# Output:Int.
# 
# Example:
# 
# assert string_length('hi') == 2
# assert string_length('CheckiO') == 7
# assert string_length('') == 0
# END_DESC

string_length = lambda text: len(text)