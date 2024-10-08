#!/usr/bin/env checkio --domain=py run morse-decoder

# Your task is to decrypt the secret message using theMorse code.
# The message will consist of words with 3 spaces between them and 1 space between each letter of each word.
# If the decrypted text starts with a letter then you'll have to print this letter in uppercase.
# 
# 
# 
# Input:The secret message (string).
# 
# Output:The decrypted text (string).
# 
# Precondition:
# 0 < len(message) < 100
# The message will consists of numbers and English letters only.
# 
# 
# END_DESC

def morse_decoder(code):
    morse = {'.-': 'a', '-...': 'b', '-.-.': 'c',
             '-..': 'd', '.': 'e', '..-.': 'f',
             '--.': 'g', '....': 'h', '..': 'i',
             '.---': 'j', '-.-': 'k', '.-..': 'l',
             '--': 'm', '-.': 'n', '---': 'o',
             '.--.': 'p', '--.-': 'q', '.-.': 'r',
             '...': 's', '-': 't', '..-': 'u',
             '...-': 'v', '.--': 'w', '-..-': 'x',
             '-.--': 'y', '--..': 'z', '-----': '0',
             '.----': '1', '..---': '2', '...--': '3',
             '....-': '4', '.....': '5', '-....': '6',
             '--...': '7', '---..': '8', '----.': '9'
             }
    words = code.split("   ")
    decrypt = ""
    for word in words:
        letters = word.split()
        for letter in letters:
            char = morse[letter]
            decrypt += char
        decrypt += " "
    decrypt = decrypt.rstrip()
    decrypt = decrypt.capitalize()
    return decrypt

if __name__ == '__main__':
    print("Example:")
    print(morse_decoder('... --- ...'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert morse_decoder("... --- -- .   - . -..- -") == "Some text"
    assert morse_decoder("..--- ----- .---- ---..") == "2018"
    assert morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--") == "It was a good day"
    print("Coding complete? Click 'Check' to earn cool rewards!")