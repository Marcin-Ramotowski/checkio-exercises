#!/usr/bin/env checkio --domain=py run amsco-cipher

# Let's look at the AMSCO cipher. This is a positional cipher with exchanges. You can easily encode or decode a    message with a pen and paper, that is of course, if you know the key.
# 
# The key is represented as a number that consist of unique digits from 1 to N. N is a length of the key. To encode    message we should write a message in a matrix with N columns. The matrix is written row by row. In this process, one    or two characters are alternately recorded in a field. One or two characters alternate in rows and in columns too    (like a chessboard). The first element is single letter field (this is the arrangement for this mission). The last    field can have single characters if there are not enough. Columns are then numbered with digits from the key in    order. For example: using the key 312, the first column will be 3, the second is 1 and the third is 2. Lastly, you    will write all characters in the columns as they were numbered in the most recent step. All white spaces and    punctuation symbols are excluded while letters are in lowercase.
# 
# Let's look at this with an example. The message "Lorem ipsum dolor sit amet". And the key is 4123. The cut message    is "loremipsumdolorsitamet". In matrix form it will be:
# 
# 
#    4   1   2   3
#    l  or   e  mi
#   ps   u  md   o
#    l  or   s  it
#   am   e   t
# 
# Now write the columns as they are numbered in the ascending order - "oruore", "emdst", "mioit", "lpslam". The    encoded message is "oruoreemdstmioitlpslam".
# 
# You are given an encoded message and the key. Your mission is to decode the message.    Of course in the cut version.
# 
# Input:Two arguments. A message as a string (unicode) and a key as an integer.
# 
# Output:The decoded message as a string.
# 
# Precondition:4 ≤ len(str(key))
# int(len(str(key)) * 1.5) ≤ len(message)
# re.match("\w+$", message)
# 
# 
# END_DESC

from itertools import cycle

def decode_amsco(message, key):
    key = str(key)
    l1 = len(message)
    l2 = len(key)
    matrix = []
    one_two = cycle([1, 2])

    while l1 > 0:
        row = []
        num = next(one_two)
        for i in range(l2):
            if num > l1:
                num = 1
            row.append(num)
            l1 -= num
            if l1 == 0:
                while len(row) < l2:
                    row.append(0)
                break
            num = 2 if num == 1 else 1
        matrix.append(row)

    l = len(matrix)
    for i in range(1, l2 + 1):
        pos = key.find(str(i))
        column = [matrix[j][pos] for j in range(l)]
        s = sum(column)
        chars = message[0:s]
        message = message[s:]
        for j in range(l):
            num = matrix[j][pos]
            znaki = chars[0:num]
            chars = chars[num:]
            matrix[j][pos] = znaki
    scores = [''.join(row) for row in matrix]
    score = ''.join(scores)
    return score

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert decode_amsco("oruoreemdstmioitlpslam", 4123) == "loremipsumdolorsitamet", "Lorem Ipsum"
    assert decode_amsco('kicheco', 23415) == "checkio", "Checkio"
    assert decode_amsco('hrewhoorrowyilmmmoaouletow', 123) == "howareyouwillhometommorrow", "How are you"