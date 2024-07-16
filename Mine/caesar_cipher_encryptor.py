#!/usr/bin/env checkio --domain=py run caesar-cipher-encryptor

# This mission is the part of the set. Another one -Caesar cipher decriptor.
# 
# Your mission is to encrypt a secret message (text only, without special chars like "!", "&", "?" etc.) using Caesar cipher where each letter of input text is replaced by another that stands at a fixed distance. For example ("a b c", 3) == "d e f"
# 
# 
# 
# Input:A secret message as a string (lowercase letters only and white spaces)
# 
# Output:The same string, but encrypted
# 
# Precondition:
# 0 < len(text) < 50
# -26 < delta < 26
# 
# 
# END_DESC

def to_encrypt(message,n):
    score = ''
    for char in message:
        if char.isalpha():
            num = ord(char) + n
            if num < 97:
                num += 26
            elif num > 122:
                num -= 26
            score += chr(num)
        elif len(score) > 0 and score[-1] != ' ':
            score += ' '
    return score