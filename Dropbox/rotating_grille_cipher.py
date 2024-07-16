#!/usr/bin/env checkio --domain=py run rotating-grille-cipher

# This is the third mission on classical cryptography. In this mission we will encrypt a message using a rotating grille.
# 
# Rotating grille cipher is a transposition cipher that uses a special square sheet of cardboard (thegrille) with holes cut in it.     To encrypt a message, sender must place the grille on an empty sheet of paper and write letters of the plaintext into the holes left to right, top to bottom.     After filling all the holes, the grille is rotated 90 degrees clockwise (the holes move to empty spaces) and the process continues.     After the grille was rotated 2 more times, there should be no empty spaces on the paper; if the message is not finished, the algorithm is repeated on the next sheet.
# 
# For example, here's what encrypting the lineMeet me at twelve PMwould look like (we'll use a grille of size 4x4):
# 
# After the encryption, the ciphertext reads astmmveeewepeatlmt.
# 
# In this task you are given a message and a key (4x4 square grille); length of the message is divisible by 16. You need to encrypt a message with the rotating grille cipher.     There is a problem, though: some of the keys are defective.     A "correct" key is made in such a way that, when laid over a grid and rotated around, every cell is shown exactly once.     So with defective keys, either some cells are shown more than once, or after applying the key in all four directions there are still unfilled spaces on the sheet.     See examples of bad keys below:
# 
# If the key is correct, return encrypted message; if the key is defective - returnNone.
# 
# Input:plaintext: str, grille: list of str (positions of holes are marked by"Х")
# 
# Output:ciphertext: str orNone
# 
# Preconditions:len(key) == 4
# all(len(l) == 4 for l in key)
# len(plaintext) % 16 == 0
# all(all(cell == "X" or cell == "." for cell in line) for line in key)
# 
# 
# PS:If you are interested in decryption of a Rotating Grille Cipher, check out missionCipher Map.
# 
# 
# END_DESC

from typing import List, Optional
import numpy as np


def grille_encrypt(plaintext: str, grille: List[str]) -> Optional[str]:
    key = np.array([list(row) for row in grille])
    matrix = [['', '', '', ''] for i in range(0, 4)]
    plaintext = list(plaintext)
    ciphertext = ""
    nums = []
    while plaintext:
        for a in range(0, 4):
            for i, row in enumerate(key):
                for j, char in enumerate(row):
                    if char == 'X':
                        point = [i, j]
                        if point in nums:
                            return None
                        matrix[i][j] = plaintext.pop(0)
                        nums.append([i, j])
            key = np.rot90(key, axes=(1,0))
        nums = []
        text = ''.join(''.join(row) for row in matrix)
        if len(text) < 16: return None
        ciphertext += text
    return ciphertext


if __name__ == "__main__":
    print("Example:")
    print(grille_encrypt("cardangrilletest", [".X..", ".X..", "...X", "X..."]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert (
        grille_encrypt("cardangrilletest", [".X..", ".X..", "...X", "X..."])
        == "actilangeslrdret"
    )
    assert (
        grille_encrypt(
            "quickbrownfoxjumpsoverthelazydog", ["X...", "...X", "..X.", ".X.."]
        )
        == "qxwkbnjufriumcoopyeerldsatoogvhz"
    )
    assert (
        grille_encrypt(
            "quickbrownfoxjumpsoverthelazydog", [".XX.", ".XX.", "..X.", "X..."]
        )
        == None
    )
    assert grille_encrypt("cardangrilletest", ["...X", "....", "....", "...."]) == None

    print("Coding complete? Click 'Check' to earn cool rewards!")