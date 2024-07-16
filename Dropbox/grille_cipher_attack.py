#!/usr/bin/env checkio --domain=py run grille-cipher-attack

# This is the fourth mission inspired by classical cryptography. In this mission we will attempt to break the Rotating Grille cipher. For more info on grille cipher check out missionsCipher MapandRotating Grille Cipher- it's highly recommended that you've solved them before trying this one.
# 
# In cryptanalysis,Known Plaintext Attack, orKPA, is a mode of attack on a cipher where the analyst has access to both the ciphertext and to the corresponding plaintext; those can be used to derive the secret key and decipher all further messages encrypted with it. Some types of ciphers are very vulnerable to KPA: for instance, Caesar's cipher can be broken knowing just one pair of corresponding plaintext and ciphertext symbols; in other cases, finding the key requires a bit more work.
# 
# In this task we'll try to perform known plaintext attack on the rotating grille cipher. First, let's quickly go over the algorithm: the key to encryption is a square stencil with holes cut in it (in this mission we will use grille of size 8x8);  the sender places the grille on a sheet and writes the first 16 letters of the message; then, turning the grille 90 degrees clockwise, the second 16 are written, and so on until the grid is filled. To decrypt a message, receiver arranges the cryptogram in an 8x8 square, places the grille on top of it and reads the letters in the holes, rotating the grille when necessary.
# 
# You are given two strings of text: a message and a corresponding cryptogram; both strings are 64 characters long. You need to find and return the grille used to encrypt the message. Like previous missions, the grille is a list of strings where "X" means hole, "." means no hole.
# 
# Important note: each input in this task is guaranteed to have a single solution.
# 
# Input:plaintext: string, cryptogram: string
# 
# Output:key: list of str size 8x8
# 
# Preconditions:
# len(plaintext) == 64
# len(cryptogram) == 64
# len(key) == 8
# all(len(line) == 8 for line in key)
# all(all(cell == "X" or cell == "." for cell in line) for line in key)
# 
# 
# 
# END_DESC

from typing import List


def find_grille(plaintext: str, cryptogram: str) -> List[str]:
    # your code here
    return []


if __name__ == "__main__":
    print("Example:")
    print(
        find_grille(
            "quickbrownfoxjumpsoverthelazydogandjackdawslovesmysphinxofquartz",
            "quicpsovkbroerthwnfoelazxjumydogmyspandjhinxackdofquawslartzoves",
        )
    )

    # These "asserts" are used for self-checking and not for an auto-testing
    assert find_grille(
        "quickbrownfoxjumpsoverthelazydogandjackdawslovesmysphinxofquartz",
        "quicpsovkbroerthwnfoelazxjumydogmyspandjhinxackdofquawslartzoves",
    ) == [
        "XXXX....",
        "XXXX....",
        "XXXX....",
        "XXXX....",
        "........",
        "........",
        "........",
        "........",
    ]

    assert find_grille(
        "weareallfromxanthcubesaidquicklyjustvisitingphazewewontbeforlong",
        "wejhewucuaeswtbrveeoisantsalilbifdteifrqunooigrmplxcakhonnlagtyz",
    ) == [
        "X...X...",
        ".X.....X",
        "..X...X.",
        "...X.X..",
        "X.....X.",
        "...X...X",
        "..X.X...",
        ".X...X..",
    ]

    assert find_grille(
        "theideaofcognitivebiasinpsychologyworksinananalogouswayacognitiv",
        "tgovgeubyhsiawseiinorkdepaswoasifcyncyaanaognconaginihlttoiivloo",
    ) == [
        "X.......",
        ".X.....X",
        "X.....XX",
        ".X..X...",
        "XX......",
        "..XXX...",
        "..X....X",
        "...X....",
    ]

    print("Coding complete? Click 'Check' to earn cool rewards!")