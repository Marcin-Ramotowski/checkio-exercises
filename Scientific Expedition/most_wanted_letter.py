#!/usr/bin/env checkio --domain=py run most-wanted-letter

# You are given a text, which contains different English letters and punctuation symbols.    You should find the most frequent letter in the text. The letter returned must be in lower case.
# While checking for the most wanted letter, casing does not matter, so for the purpose of your search,    "A" == "a".    Make sure you do not count punctuation symbols, digits and whitespaces, only letters.
# 
# If you havetwo or more letters with the same frequency,    then return the letter which comes first in the Latin alphabet.    For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".
# 
# Input:A text for analysis as a string.
# 
# Output:The most frequent letter in lower case as a string.
# 
# Precondition:
# A text contains only ASCII symbols.
# 0 < len(text) ≤ 105
# 
# 
# END_DESC

def checkio(text: str) -> str:
    tekst = text.lower()
    checked = []
    dictionary = {}
    for letter in tekst:
        if letter.isalpha() is True:
            if letter not in checked:
                dictionary[letter] = tekst.count(letter)
                checked.append(letter)
    ranking = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    thebest = ranking[0][1]
    top = []
    for x in ranking:
        if x[1] == thebest:
            top.append(x[0])
    top = sorted(top)
    return top[0]

if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")