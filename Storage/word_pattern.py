#!/usr/bin/env checkio --domain=py run word-pattern

# pre.example {        background-color: #EBEDED;        margin: 5px;        padding: 3px;        border: solid 1px #737370;        border-radius: 3px;        --webkit-border-radius: 3px;    }Sophia's drones are too simple and can recognize symbols in only single words, digits or letters.    She wants to teach the drones to understand basic commands which are represented as "words" consisted by letters and digits.    For that, Sophia has uploaded "patterns," which describe the sequence of digits and letters in the command.    Unfortunately, the drones memory can only store integers and convert them into binary format for comparison.    We should help Sophia to write a module for the comparison of patterns and commands.
# 
# You are given a pattern as a positive integer and a command as a word.    For the comparison, the drone should convert the integer pattern into binary form,    append zeros to left for the command length and compare this combination with the command.
# 1 is a letter. 0 is a digit.
# If the pattern and the command are coincided, then return True, else -- False.    If pattern is longer than a command, then they are not coincided (For example - 8 = 1000 and "a").
# 
# For example. The pattern is 42 and the command is "12a0b3e4".
# 42 == 101010 in binary form, but this is not enough of length. Let's append zeroes -- "00101010".    Then compare:
#       42 == 00101010
# 12a0b3e4 == DDLDLDLD
# --------------------
#     True    VVVVVVVVOne more example -- 101 and "ab23b4zz":
#      101 == 01100101
# ab23b4zz == LLDDLDLL
# --------------------
#    False    XVXVXXXVInput:Two arguments. A pattern as a positive integer and a command as a string.
# 
# Output:Is the pattern coincide with the command or not as a boolean.
# 
# Precondition:0 ≤ pattern < 231
# 0 < len(command) < 32
# "command" contains only ASCII letters or digits.
# 
# 
# END_DESC

def check_command(pattern:int, command:str) -> bool:
    binary = bin(pattern)[2:]
    if len(binary) < len(command):
        amount = len(command) - len(binary)
        addition = '0' * amount
        binary = addition + binary
    string = ''
    for char in command:
        string += '1' if char.isalpha() else '0'
    return binary == string