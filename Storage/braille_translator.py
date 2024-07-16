#!/usr/bin/env checkio --domain=py run braille-translator

# Brailleis a tactile writing system used by the blind and the visually impaired. It is    traditionally written with embossed paper. Braille characters are small rectangular blocks,    called cells, which contain tiny palpable bumps called raised dots. The number and arrangement    of these dots distinguish one character from another.
# 
# We will use a 6-dots Braille alphabet. Each letter can be represented as a 3x2 matrix where 1 is    a raised dot and 0 is an empty space.
# 
# 
# 
# (Letter W is not original)
# 
# Letters should be separated by an empty column. Whitespaces are two empty columns (plus a    separator empty column if it is between letters). Various formatting marks indicate the values    of the letters that follow them. They have no direct equivalent in print. The most important    indicators in English Braille are: "capital" and "number".    These marks work as "shift" - only for a follow letter.
# 
# 
# 
# We will use several basic punctuation symbols:
# 
# 
# 
# You are given a page of text and you should convert it into Braille. The page contains one or    several lines represented as a matrix. Each line contains no more than 10 symbols (including    non-printed). Lines are separated by one empty row. Symbols are separated by empty columns but    there are no separators in beginnings and ends of lines. If text can be placed in one line, then    the page width is proportional to the length of the text. If the page has more than one line,    then the width is equal to the longer line and the final line is appended by whitespaces.
# 
# For example, this is the text "hello 1st World!".
# 
# 
# 
# Input:A text as a string.
# 
# Output:The page as a list of lists or tuple of tuples with integers (1/0).
# 
# Precondition:
# 0 < len(text)
# all(ch in string.ascii_letters + " .,!?-_0123456789" for ch in text)
# 
# 
# END_DESC

from numpy import zeros

def convert(code):
    bin_code = bin(code)[2:].zfill(6)[::-1]
    return [[int(bin_code[j + i * 3]) for i in range(2)] for j in range(3)]


LETTERS_NUMBERS = list(map(convert,
                           [1, 3, 9, 25, 17, 11, 27, 19, 10, 26,
                            5, 7, 13, 29, 21, 15, 31, 23, 14, 30,
                            37, 39, 62, 45, 61, 53, 47, 63, 55, 46, 26]))
CAPITAL_FORMAT = convert(32)
NUMBER_FORMAT = convert(60)
PUNCTUATION = {",": convert(2), "-": convert(18), "?": convert(38),
               "!": convert(22), ".": convert(50), "_": convert(36), ' ':convert(0)}
WHITESPACE = convert(0)


def generate_matrix(n):
    r = (n // 10 + 1) *3 if n % 10 != 0 else n//10*3
    sepr = n//10 -0 if n % 10 != 0 else n//10 -1
    r += sepr
    if n <= 9:
        sepc = n-1
        c = n*2 + sepc
    else:
        c = 29
    return zeros((r,c), int)


def braille_page(text: str):
    n = 0
    commands = []
    for char in text:
        if char.isdigit():
            n += 2
            commands.append(NUMBER_FORMAT)
            commands.append(LETTERS_NUMBERS[int(char)-1])
        elif char.isupper():
            n += 2
            char = char.lower()
            commands.append(CAPITAL_FORMAT)
            commands.append(LETTERS_NUMBERS[ord(char)-97])
        elif char in PUNCTUATION:
            n += 1
            commands.append(PUNCTUATION[char])
        else:
            n += 1
            commands.append(LETTERS_NUMBERS[ord(char)-97])

    M = generate_matrix(n)
    x, y, z = 0,0,0
    for block in commands:
        for command in block:
            if y > 29:
                z += 1
                x = z * 4
                y = 0
            r ,c = command
            if r:
                M[x,y] = 1
            if c:
                M[x,y+1] = 1
            x += 1
        x = z * 4
        y += 3
    score = [list(line) for line in M]
    return score