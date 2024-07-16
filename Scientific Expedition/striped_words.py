#!/usr/bin/env checkio --domain=py run striped-words

# Our robots are always working to improve their linguistic skills.    For this mission, they research the Latin alphabet and its applications.
# 
# The alphabet contains both vowel and consonant letters (yes, we divide the letters).
# Vowels --A E I O U Y
# Consonants --B C D F G H J K L M N P Q R S T V W X Z
# 
# You are given a block of text with different words.     These words are separated by whitespaces and punctuation marks.    Numbers are not considered as words in this mission (a mix of letters and digits is not a word either).    You should count the number of words (striped words) where the vowels with consonants are alternating;     words that you count cannot have two consecutive vowels or consonants.    The words consisting of a single letter are not striped -- don't count those. Casing is not significant for this mission.
# 
# Input:A text as a string (unicode)
# 
# Output:A quantity of striped words as an integer.
# 
# Precondition:The text contains only ASCII symbols.
# 0 < len(text) < 105
# 
# 
# END_DESC

def checkio(line: str) -> int:
    line = line.lower()
    line += " "
    x = 0
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    word = ''
    words = []
    for char in line:
        if char.isalpha() is True or char.isdigit() is True:
            word += char
        else:
            words.append(word)
            word = ''
    words = [word for word in words if len(word) > 1 and word.isalpha() is True]
    for word in words:
        l = len(word)
        lista = []
        for letter in word:
            if letter in vowels:
                lista.append(True)
            else:
                lista.append(False)
        lista2 = []
        lista3 = []
        if l % 2 == 0:
            for i in range(1, l, 2):
                lista2.append(lista[i])
                lista3.append(lista[i - 1])
        else:
            for i in range(0, l, 2):
                lista2.append(lista[i])
                if i != l - 1:
                    lista3.append(lista[i + 1])
        set2 = set(lista2)
        set3 = set(lista3)
        l2 = len(set2)
        l3 = len(set3)
        if l2 == l3 and l2 == 1:
            check2 = list(set2)
            check3 = list(set3)
            if check2[0] != check3[0]:
                x += 1
    return x


if __name__ == '__main__':
    print("Example:")
    print(checkio('My name is ...'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert checkio('My name is ...') == 3
    assert checkio('Hello world') == 0
    assert checkio('A quantity of striped words.') == 1
    assert checkio('Dog,cat,mouse,bird.Human.') == 3
    print("Coding complete? Click 'Check' to earn cool rewards!")