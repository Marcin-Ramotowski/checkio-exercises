#!/usr/bin/env checkio --domain=py run playfair-cipher-attack

# This is the fifth and final (for now) mission inspired by classical cryptography. In this mission we'll try to break the Playfair cipher using known plaintext attack. To learn more about this cipher, check outPlayfair Ciphermission.
# 
# Playfair Cipheris a manual substitution cipher invented in 1854. Unlike other substitution ciphers that existed at the time, Playfair doesn't encrypt single letters - instead it works with pairs of letters, orbigrams. Let's remind ourselves of the encryption algorithm:
# 
# Playfair cipher used a 5x5 key table filled with 25 letters of English alphabet in random order (letterJis omitted). Message is broken up into pairs of letters (each pair must consist of two different letters, otherwise letterXis inserted between them). Then each bigram is encrypted according to following rules:
# 
# 1. If both letters are in the same row of key table, each is replaced by the letter to it's immediateright(the last column wraps around to the first);
# 
# 2. If the letters appear in the same column - each is replaced with the onebelowit (the bottom row wraps around to the top);
# 
# 3. If the letters are at diagonally opposite corners of a rectangle, they are replaced with letters at other two corners. The order is important - the first letter of the encrypted pair is the one that lies on the samerowas the first letter of the plaintext pair
# 
# For example, if the key table is
# 
# 
# d f o l s
# e a r m c
# b z h q p
# t g i n x
# k u v y w
# then the wordsecretwill be encrypted asdcembk.To decrypt the message, we use the same rules (except that if the letters of a bigram lies in the same row or column, we must use the letters to theirleftandaboverespectively).
# 
# In this mission you will try to break the Playfair Cipher using known plaintext attack. You are given a plaintext and a corresponding cryptogram. The plaintext is already prepared for encryption (J's replaced with I's and X's inserted between double letters), so don't worry about that. You need to find the key table used for encryption and return the codephrase "topsecretmessage" encrypted with the same key table.
# 
# Important note: each input is guaranteed to have a single solution.
# 
# Input:plaintext: str, cryptogram: str
# 
# Output:encrypted codephrase: str
# 
# Preconditions:
# len(plaintext) == len(cryptogram)
# len(plaintext) % 2 == 0
# all([l in 'abcdefghiklmnopqrstuvwxyz' for l in plaintext])
# all([l in 'abcdefghiklmnopqrstuvwxyz' for l in cryptogram])
# 
# 
# 
# 
# 
# END_DESC

def playfair_attack(plaintext: str, cryptogram: str) -> str:
    # your code here
    return ""


if __name__ == "__main__":
    print("Example:")
    print(
        playfair_attack(
            "sixcrazykingsvowedtoabolishmyquitepitifulioust",
            "zlgrcekqztvoolunhbvkemsvlzadnpzflrqlvlhwtluzkl",
        )
    )

    # These "asserts" are used for self-checking and not for an auto-testing
    assert (
        playfair_attack(
            "sixcrazykingsvowedtoabolishmyquitepitifulioust",
            "zlgrcekqztvoolunhbvkemsvlzadnpzflrqlvlhwtluzkl",
        )
        == "vklprhcrixbpzebc"
    )

    assert (
        playfair_attack(
            "pythonsxstandardlibraryisveryextensiveofferingawiderangeofstuffx",
            "aiwblarskwphydowzehmhoieksxlixgwvufxlvzqvizxbehdycxlphyxzqkwcvsi",
        )
        == "dmhfiulxgbxvqhyx"
    )

    assert (
        playfair_attack(
            "zombiesquicklyatetwelveofmyneighboursx",
            "uzuywyksmzdcvhfgtnftonbnkfevywlgxzmxzd",
        )
        == "xnzpchtyrfcwpkth"
    )

    print("Coding complete? Click 'Check' to earn cool rewards!")