#!/usr/bin/env checkio --domain=py run isometric-strings

# Maybe it's a cipher? Maybe, but we don’t know for sure.
# 
# Maybe you can call it"homomorphism"? I wish I knew this word before.
# 
# You need to check that the String A is isometric to the String B. There exists a function that turns characters from String A into characters in the same spot in String B.
# 
# Characters in String A correspond to a unique character value in String B. Characters in String B are allowed to correspond to multiple character values in String A.
# 
# Input:Two arguments. String A and String B.
# 
# Output:Boolean.
# 
# Precondition:
# both strings are the same length
# 
# 
# END_DESC

def isometric_strings(str1: str, str2: str) -> bool:
    dictionary = {}
    i = 0
    while i < len(str1):
        if str1[i] in dictionary:
            if dictionary[str1[i]] == str2[i]:
                return True
            else:
                return False
        dictionary[str1[i]] = str2[i]
        i += 1
    return True


if __name__ == '__main__':
    print("Example:")
    print(isometric_strings('add', 'egg'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert isometric_strings('add', 'egg') == True
    assert isometric_strings('foo', 'bar') == False
    assert isometric_strings('', '') == True
    assert isometric_strings('all', 'all') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")