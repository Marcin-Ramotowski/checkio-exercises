#!/usr/bin/env checkio --domain=py run text-formatting

# You are given a long line (a monospace font), and you have to break the line in order to respect a given width.	Then you have to format the text according to the given style: 'l' means you have to align the text to theleft, 'c' forcenter, 'r' forright, and 'j' means you have tojustify the text.	Finally, the lines of the output shouldn’t end with a whitespace.
# 
# If you have to put 2 * n + 1 spaces around a line in order to center it, then put n spaces before, not n + 1.
# 
# The justification rules:Since we can't always put the same number of spaces between words in a line, put big blocks of spaces first. For example: X---X---X--X--X--X when you have to put 12 spaces in 5 gaps: 3-3-2-2-2.Don't justify the last line of a text.
# 
# You won't have to consider splitting a word into two parts because the given widths are big enough.
# 
# Input:A text (string), width (integer) and style (string).
# 
# Output:The formatted text (string).
# 
# Preconditions:all(len(word) <= width for word in text.split())'\n' not in textstyle in ('l', 'c', 'r', 'j')0 < len(text) <= 1000
# 
# 
# END_DESC

def text_formatting(text: str, width: int, style: str) -> str:
    n = width
    while n < len(text):
        while text[n] != ' ':
            n -= 1
        text = text[:n] + '\n' + text[n+1:]
        n += width+1

    if style == 'l':
        return text

    elif style == 'c':
        lines = text.split('\n')
        for i, line in enumerate(lines):
            spaces = (width - len(line))//2  # spaces to add
            lines[i] = ' ' * spaces + line
        return '\n'.join(lines)

    elif style == 'r':
        lines = [(width - len(line)) * ' ' + line for line in text.split('\n')]
        return '\n'.join(lines)

    elif style == 'j':
        lines = text.split('\n')
        for i, line in enumerate(lines[0:-1]):
            spaces = width - len(line)  # spaces to add
            words = [word + ' ' for word in line.split()]
            words[-1] = words[-1][0:-1]
            j = 0
            while spaces > 0:
                if j == len(words)-1:
                    j = 0
                words[j] += ' '
                spaces -= 1
                j += 1
            lines[i] = ''.join(words)
        return '\n'.join(lines)