#!/usr/bin/env checkio --domain=py run verify-anagrams

# An anagram is a type of word play,    the result of rearranging the letters of a word or phrase to produce a new word or phrase,    using all the original letters exactly once.    Two words are anagrams to each other if we can get one from another by rearranging the letters.    Anagrams are case-insensitive and don't take account whitespaces.    For example: "Gram Ring Mop" and "Programming" are anagrams. But "Hello" and "Ole Oh" are not.
# 
# You are given two words or phrase. Try to verify are they anagrams or not.
# 
# Input:Two arguments as strings.
# 
# Output:Are they anagrams or not as boolean (True or False)
# 
# Precondition:0 < |first_word| < 100;
# 0 < |second_word| < 100;
# Words contain only ASCII latin letters and whitespaces.
# 
# 
# END_DESC

def verify_anagrams(a, b):
    set1 = [letter.lower() for letter in a if letter.isalpha() is True]
    set2 = [letter.lower() for letter in b if letter.isalpha() is True]
    if len(set1) != len(set2):
        return False
    x = False
    y = True
    for letter in set1:
        if letter in set2:
            x = True
        else:
            x = False
            break
    if x is False:
        return False
    else:
        for letter in set1:
            count = set1.count(letter)
            if count > 1:
                check = set2.count(letter)
                if count != check:
                    y = False
    if x is True and y is True:
        return True
    else:
        return False


if __name__ == '__main__':
    print("Example:")
    print(verify_anagrams('Programming', 'Gram Ring Mop'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert verify_anagrams('Programming', 'Gram Ring Mop') == True
    assert verify_anagrams('Hello', 'Ole Oh') == False
    assert verify_anagrams('Kyoto', 'Tokyo') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")