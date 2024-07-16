#!/usr/bin/env checkio --domain=py run restricted-prime

# ul.words li {        font-weight: bold;        font-style: italic;    }Next, we want to teach ourcensored calculatorto check if numbers are primes or not.    This crazy calculator has learned new some words (but forgotten some others) and does not accept new words, certain symbols and it hates digits!
# 
# The list of forbidden words and symbols:
# 
# importdivevalrangelen⁄ % −digits (0-9)Given a number (0 < n < 10000), you should check if it is a prime or not.    Your solution should not contain any of the forbidden words, symbols or digits (even as a part of another word).
# 
# Input:A number as an integer.
# 
# Output:Is it prime or not as a boolean.
# 
# Precondition:1 < number < 10000
# 
# 
# 
# END_DESC

ZERO = int(False)
ONE = int(True)
TWO = int(True) + int(True)

def odd_candidates(n):
    i = int(True)
    j = int(True) + int(True)
    while i < n:
        yield i
        i += j
        if i * TWO > n:
            break

def checkio(n):
    evens = list(map(str,[ZERO, TWO, TWO**TWO, TWO**TWO + TWO, TWO*TWO**TWO]))
    chars = list(str(n))
    chars.reverse()
    is_even = chars[ZERO] in evens
    if is_even:
        return n == TWO
    candidates = list(odd_candidates(n))
    i = ZERO
    for i in candidates[ONE:]:
        x = i
        while x < n:
            x += i
        if x == n:
            return False
    return True