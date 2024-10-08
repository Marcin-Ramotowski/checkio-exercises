#!/usr/bin/env checkio --domain=py run goes-after

# In a given word you need to check if one symbol goes only right after another.
# 
# Cases you should expect while solving this challenge:
# 
# If more than one symbol is in the list you should always count the first oneOne of the symbols are not in the given word - your function should return False;Any symbol appears in a word more than once - use only the first one;Two symbols are the same - your function should return False;The condition is case sensitive, which means 'a' and 'A' are two different symbols.Input:Three arguments. The first one is a given string, second is a symbol that should go first, and the third is a symbol that should go after the first one.
# 
# Output:A bool.
# 
# 
# END_DESC

def goes_after(word: str, first: str, second: str) -> bool:
    a = word.find(first)
    b = word.find(second)
    if a == -1 or b == -1:
        return False
    x = True if b-a == 1 else False
    return x


if __name__ == '__main__':
    print("Example:")
    print(goes_after('world', 'w', 'o'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert goes_after('world', 'w', 'o') == True
    assert goes_after('world', 'w', 'r') == False
    assert goes_after('world', 'l', 'o') == False
    assert goes_after('panorama', 'a', 'n') == True
    assert goes_after('list', 'l', 'o') == False
    assert goes_after('', 'l', 'o') == False
    assert goes_after('list', 'l', 'l') == False
    assert goes_after('world', 'd', 'w') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")