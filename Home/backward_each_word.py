#!/usr/bin/env checkio --domain=py run backward-each-word

# In a given string you should reverse every word, but the words should stay in their places.
# 
# Input:A string.
# 
# Output:A string.
# 
# Precondition:The line consists only from alphabetical symbols and spaces.
# 
# 
# END_DESC

def backward_string_by_word(text: str) -> str:
    l = len(text)
    if l < 2:
        return text
    split = []
    string = ''
    i = 0
    j = 0
    spacesDetected = False
    for char in text:
        if char.isalpha() is True:
            if spacesDetected is True:
                i = 0
                spacesDetected = not(spacesDetected)
                split.append(string)
                string = ''
                string += char
            else:
                string += char
        else:
            i += 1
            spacesDetected = True
            if i > 1:
                string += char
            else:
                split.append(string)
                string =''
                string += char
        j += 1
        if j == l:
            split.append(string)
    lista = []
    for word in split:
        x = word[::-1]
        lista.append(x)
    words = "".join(lista)
    return words

if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word(''))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")