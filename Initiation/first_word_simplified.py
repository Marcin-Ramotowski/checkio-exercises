#!/usr/bin/env checkio --domain=py run first-word-simplified

# You are given a string and you have to find its first word.
# 
# This is a simplified version of theFirst Wordmission, which can be solved later.
# 
# The input string consists of only English letters and spaces.There aren’t any spaces at the beginning and the end of the string.Input:A string.
# 
# Output:A string.
# 
# Precondition:The text can contain a-z, A-Z and spaces.
# 
# 
# END_DESC

def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    words=text.split()
    return words[0]


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word("a word") == "a"
    assert first_word("hi") == "hi"
    print("Coding complete? Click 'Check' to earn cool rewards!")