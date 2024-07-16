#!/usr/bin/env checkio --domain=py run playfair-cipher

# ThePlayfair cipheror Playfair square, is a manual symmetric encryption technique and was the first literal digraph substitution    cipher. The scheme was invented in 1854 by Charles Wheatstone, but bears the name of Lord Playfair who promoted the    use of the cipher. The Playfair cipher uses a 5 by 5 table containing a keyword or phrase. Memorization of the    keyword and 4 simple rules are all that’s required to create the 5 by 5 table and use the cipher. For this mission,    we will do one better and use a 6 by 6 table.
# 
# For the key table, we should use ASCII letters in lowercase ("abcdefghijklmnopqrstuvwxyz") and digits    ("0123456789"). They are have the following order:
# 
# 
# "abcdefghijklmnopqrstuvwxyz0123456789"
# 
# To generate the key table, the spaces in the table must be filled with the letters contained in the keyword    (dropping any duplicate letters and digits), then the remaining spaces are filled with the rest of the letters and    digits of the alphabet in order. The key is written in the top rows of the table, from left to right. The keyword    together with the conventions for filling in the 6 by 6 table constitute the cipher key.
# 
# To encrypt a message, we will need to prepare a block of text. Upper case letters get transposed into lower case of    letters, we’d break the message into digraphs (groups of 2 letters) and skip white spaces and punctuation symbols.    The result would turn a message like "Hello World!" into "he ll ow or ld", and would get mapped out in the key    table. The two letters of the digraph are considered to be the opposite corners of a rectangle in the key table.    Note the relative position of the corners of this rectangle. Then apply the following 4 rules, in order, to each    pair of letters in the plaintext:
# 
# Prepare text: convert to lowercase, remove all non-useable symbols (white spaces, punctuation etc) and break the        message into digraphs. If both letters are the same, add an "x" after the first letter (for double "x" use "z"        as completion character) and shift following digraphs. If needed, append a "z" to complete the final digraph (or        "x" if the last letter is "z"). For example "pp dr ..." will become "px pd r..." before encoding and "xx zz ..."        will became "xz xz z...".If the letters appear on the same row of your table, replace them with the letters to their immediate right        respectively (wrapping around to the left side of the row if a letter in the original pair was on the right side        of the row).If the letters appear on the same column of your table, replace them with the letters immediately below        respectively (wrapping around to the top side of the column        if a letter in the original pair was on the bottom side of the column).If the letters are not on the same row or column, replace them with the letters on the same row respectively but        at the other pair of corners of the rectangle defined by the original pair. The order is important – the first        letter of the encrypted pair is the one that lies on the same row as the first letter of the plaintext pair.To decrypt, use the inverse (opposite) of the last 3 rules and you will get the processed (cut version).
# 
# For example, the keyword is "checkio101". Then the key table will be looked as
# 
# 
# c h e k i o
# 1 0 a b d f
# g j l m n p
# q r s t u v
# w x y z 2 3
# 4 5 6 7 8 9
# 
# Let's the message is "Fizz Buzz is x89 XX." After using rule 1 (text preparation) we will get -    "fi zx zb uz zi sx 89 xz xz".
# - "fi" => "do";
# - "zx" => "2y";
# - "zb" => "7m";
# - "uz" => "t2";
# - "zi" => "2k";
# - "sx" => "ry";
# - "89" => "94";
# - "xz" => "y2";
# - "xz" => "y2".
# And the encoded message is "do2y7mt22kry94y2y2".
# 
# You should write two functions - "encode" and "decode". Each function receives a message (ciphered or opened) and    keyword. The "encode" function processes and encrypts a message. The "decode" function decrypts the encoded message    (of course in the processed version).
# 
# Input:Two arguments. A message as a string (unicode) and a keyword as a string (unicode).
# 
# Output:The encoded or decoded message (related to function).
# 
# Precondition:0 < len(key) ≤ 36
# 
# 
# Sources:Wikipedia
# 
# 
# 
# END_DESC

from numpy import zeros, nonzero
from itertools import chain, zip_longest

def encode(message: str, keyword: str) -> str:
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
    message = message.lower()
    message = ''.join([char for char in message if char in alphabet])
    matrix = zeros((6, 6), str)
    x, y = 0, 0
    for char in chain(keyword, alphabet):
        if char in alphabet:
            matrix[x, y] = char
            if y < 5:
                y += 1
            else:
                y = 0
                x += 1
        alphabet = alphabet.replace(char, '')

    i = 1
    while i < len(message):
        pair = message[i-1:i+1]
        if pair[0] == pair[1]:
            bonus = 'x' if pair[0] != 'x' else 'z'
            message = message[:i] + bonus + message[i:]
        i += 2
    pairs = list(zip_longest(message[0::2],message[1::2],fillvalue= 'x' if message[-1] =='z' else 'z'))

    score = ''
    for pair in pairs:
        places = []
        for char in pair:
            place = nonzero(matrix == char)
            coords = list(zip(place[0], place[1]))[0]
            places.append(coords)
        rows = [places[0][0], places[1][0]]
        cols = [places[0][1], places[1][1]]
        if rows[0] == rows[1]:
            for place in places:
                x, y = place
                if y < 5:
                    y += 1
                else:
                    y = 0
                score += matrix[x, y]
        elif cols[0] == cols[1]:
            for place in places:
                x, y = place
                if x < 5:
                    x += 1
                else:
                    x = 0
                score += matrix[x, y]
        else:
            x, y = places[0]
            x2, y2 = places[1]
            score += matrix[x, y2]
            score += matrix[x2, y]
    return score


def decode(message:str, keyword:str) -> str:
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
    matrix = zeros((6,6),str)
    x,y = 0,0
    for char in chain(keyword, alphabet):
        if char in alphabet:
            matrix[x,y] = char
            if y < 5: 
                y += 1
            else: 
                y = 0
                x += 1
        alphabet = alphabet.replace(char,'')
    pairs = list(zip(message[0::2],message[1::2]))

    score = ''
    for pair in pairs:
        places = []
        for char in pair:
            place = nonzero(matrix==char)
            coords = list(zip(place[0], place[1]))[0]
            places.append(coords)
        rows = [places[0][0], places[1][0]]
        cols = [places[0][1], places[1][1]]
        if rows[0] == rows[1]:
            for place in places:
                x, y = place
                if y > 0:
                    y -= 1
                else:
                    y = 5
                score += matrix[x,y]
        elif cols[0] == cols[1]:
            for place in places:
                x , y = place
                if x > 0:
                    x -= 1
                else:
                    x = 5
                score += matrix[x,y]
        else:
            x, y = places[0]
            x2, y2 = places[1]
            score += matrix[x,y2]
            score += matrix[x2,y]
    return score