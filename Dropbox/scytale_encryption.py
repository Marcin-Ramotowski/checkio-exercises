#!/usr/bin/env checkio --domain=py run scytale-encryption

# This is the second in a series of missions dedicated to classical cryptography. In this mission we will try to break the Scytale encryption.
# 
# Scytale is one of the first known cryptographic devices, used by ancient Greeks, namely Spartans, during their military campaigns.It consisted of a cylindrical rod or staff with a long strip of parchment wrapped around it. The sender would simply write the message along the length of the rod and across the winds of a strip until the end of the parchment was reached, then turn the cylinder and continue writing the next line. After unwinding the parchment, the text became unintelligible. To decrypt the message, it would be wrapped around another scytale of the same diameter, after which the plaintext could be read along it.Scytale is atranspositioncipher. Unlike substitution ciphers, like Atbash or Caesar's cipher, here the letters of the plaintext remain unchanged, but their order is altered.
# 
# For example, suppose the message is"let's meet at eleven in the evening"and diameter of the rod allows to write 4 letters in a circle. The scytale with a message written on it would look like this:
# 
# After unwinding the strip the message becomeslteeeanvttaesetnmltieehneveg.
# 
# If an adversary intercepted a message, they wouldn't be able to read it unless they knew thekeyto encryption - in this case, the diameter of the cylinder (or, more specifically, number of letters that could be written in a circle around it). However, it could easily be found by trying several rods of different size. Another method (attributed to Aristotle) includes wrapping the parchment with encrypted message around a cone-shaped rod with varying diameter until a fragment of text becomes readable.
# 
# In this mission we'll try to break a scytale encryption. You have a cryptogram and acrib- a word that is expected to be in the decrypted message. You need to try all the possible keys until you get a plaintext that contains the crib. If after trying every key you either found no such plaintext, or found more than one possible keys - returnNone.
# 
# There is also one last piece of informaion: you know that the sender encrypts the messages using the shortest possible strip of parchment, so that there are no empty spaces on it. for example, the message"let's meet at eleven in the evening", encrypted with key5, will look like this:
# 
# Note that the lines have different lengths. The cryptogram will be"leeteetvhntaeeistnenmeivgeln".
# 
# Input:ciphertext: str, crib: str
# 
# Output:plaintext: str orNone
# 
# 
# END_DESC

from typing import Optional


def scytale_decipher(ciphertext: str, crib: str) -> Optional[str]:
    a = len(ciphertext)
    b = a//2
    score = ""
    scores = []
    for r in range(2,b+1): # wybiera klucze
        for i in range(0,r): # ustala początki
            for j in range(i,a,r): # przesuwa się co r
                score += ciphertext[j]
        if crib in score:
            if scores: return None
            scores.append(score)
        score = ""
    return scores[0] if scores else None


if __name__ == "__main__":
    print("Example:")
    print(scytale_decipher("aaaatctwtkdn", "dawn"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert scytale_decipher("aaaatctwtkdn", "dawn") == "attackatdawn"
    assert scytale_decipher("hdoeerlallrdow", "world") == "hellodearworld"
    assert (
        scytale_decipher("totetshpmeecisendysescwticsriasraytlaegphet", "sicret")
        == None
    ), "Crib is not in plaintext"
    assert (
        scytale_decipher("aaaatctwtkdn", "at") == None
    ), "More than one possible decryptions"

    print("Coding complete? Click 'Check' to earn cool rewards!")