#!/usr/bin/env checkio --domain=py run univocalic-davasaan

# Being a rockstar is the intersection of who you are and who you want to be.
# 
# 
# - Slash (Guitarist for Guns N' Roses)
# 
# You have to write a function nameddavasaan(division with all vowels a)    which calculates integer division by 10.
# The vowels "eiou" are disallowed as are the slash "/",    asterisk "*", and period "." characters.
# 
# We have one more rule for thisunivocalicchallenge.    This is a code golf mission and your main goal is to make your code as short as possible:300 charactersis the maximum allowable.    The shorter your code, the more remarkable you are.
# Note that your code can start/end with empty lines and commented lines,    they are not considered for code length.    Hence you can comment a bit your code.
# 
# Input:A non-negative number as an integer.
# 
# Output:The integer division (//10) of the input as an integer.
# 
# Precondition:0 ≤ n ≤ 2,000,000,000
# 
# Special thanks tojtokazwho first created the mission years ago.
# 
# 
# END_DESC

davasaan = lambda x:int(str(x)[0:-1]) if x > 9 else 0