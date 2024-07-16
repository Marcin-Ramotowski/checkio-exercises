#!/usr/bin/env checkio --domain=py run atbash-cipher

# This is the first in a series of missions inspired by classical cryptography. In this mission we will take a look at the Atbash cipher.
# 
# Atbash is one of the oldest known ciphers, created in Middle East around 600 B.C.; the first known examples of it can be found in the Dead Sea Scrolls     (ancient religious Hebrew manuscripts), where it was used to encrypt certain important names and words.
# 
# Atbash is an example of asimple substitutioncipher. In this type of ciphers each letter of the message (orplaintext) is mapped to     a single correspinding letter of the ciphertext. in case of Atbash the plaintext alphabet is simply mapped to it's reverse, so that the first letter     is replaced with the last, the second letter - with the second to last and so on. For example, the message "Hello, world!" is enciphered to "Swool, dliow!".     The substitution table (for Latin alphabet) looks like this:
#     Plaintext alphabet:  abcdefghijklmnopqrstuvwxyz
#     Ciphertext alphabet: zyxwvutsrqponmlkjihgfedcba
# To decrypt a message, the same algorithm is applied to the ciphertext.
# 
# It's easy to see that Atbash provides virtually no information security. Anyone who intercepts the message encrypted with the Atbash cipher can easily     decipher it by applying the same substitution table.
# 
# For this mission you need to write a function that encrypts given text with Atbash. Punctuation, whitespaces and other characters should remain unchanged.
# 
# Input:plaintext: str
# 
# Output:ciphertext: str
# 
# Example:
# 
# 
# atbash('testing') == 'gvhgrmt'
# atbash('Hello, world!') == 'Svool, dliow!'
# 
# 
# 
# END_DESC

def atbash(plaintext: str) -> str:
    alphabet1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet2 = "zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA"
    score = ""
    for char in plaintext:
        n = alphabet1.find(char)
        if n != -1:
            score += alphabet2[n]
        else:
            score += char
    return score


if __name__ == "__main__":
    print("Example:\nplaintext: testing")
    print(atbash("testing"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert atbash("testing") == "gvhgrmt"
    assert atbash("attack at dawn") == "zggzxp zg wzdm"
    assert atbash("Hello, world!") == "Svool, dliow!"

    print("Coding complete? Click 'Check' to earn cool rewards!")