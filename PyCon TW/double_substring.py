#!/usr/bin/env checkio --domain=py run double-substring

# There are four substring missionsthat were born all in one day and you shouldn’t be needed more than one day to solve them. All of those mission can be simply solved by brute force, but is it always the best way to go? (you might not have access to all of those missions yet, but they are going to be available with more opened islands on the map).
# 
# This is the third mission of the series, and it’s the only one where you have to return not a substring but a substring length. You need to find a substring that repeats more than once in a given string. This reiteration shouldn't have overlaps. For example, in a string "abcab" the longest substring that repeats more than once is "ab", so the answer should be 2 (length of "ab")
# 
# Input:String.Output:Int.
# 
# 
# 
# 
# 
# 
# END_DESC

def double_substring(text:str) -> int:
    n = len(text)
    l = n//2
    for x in range(l,0,-1):
        for i in range(0,n-n%x,x):
            substring = text[i:i+x]
            c = text.count(substring)
            if c > 1:
                return len(substring)
    return 0