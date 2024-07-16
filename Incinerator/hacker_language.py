#!/usr/bin/env checkio --domain=py run hacker-language

# Your friends and you have decided to feel like the true hackers and create a special "hacker language" for correspondence in the net. The original messages will be written in English and then encrypted according to these rules:
# - all letters and whitespaces will be converted into theirASCIIcodes and than into the binary numbers. Except the whitespaces - their binary form should be '1000000' not '100000'.
# - numbers, dates (in the 'dd.mm.yyyy' format), time (in the 'hh:mm' format) and special signs ('.', ':', '!', '?', '@', '$', '%') won't be converted.
# For the realisation of this system you should create the HackerLanguage class with the following methods:
# 
# write(text) - adds new (text) to the current text message.
# delete(N) - deletes from the current text message the last N symbols.
# send()- returns the encrypted message which will be send.
# read(text) - gets the encrypted (text) as the argument and returns the normal readable English text.
# 
# In this mission you could use theInterpreterdesign pattern.
# 
# Examples:
# message_1 = HackerLanguage()
# message_1.write('Remember: 21.07.2018 at 11:11AM')
# message_1.delete(2)
# message_1.write('PM')
# message_1.send() == '10100101100101110110111001011101101110001011001011110010:100000021.07.2018100000011000011110100100000011:1110100001001101'
# 
# message_2 = HackerLanguage()
# message_2.read('10011011111001100000011001011101101110000111010011101100100000011010011110011100000011011011110010.11100101101111110001011011111110100@11001111101101110000111010011101100.110001111011111101101') ==
# 'My email is mr.robot@gmail.com'
# 
# 
# 
# Input:Plain or encrypted text.
# 
# Output:Encrypted or decrypted text of the message.
# 
# Precondition:Only [a-z], [A-Z], [0-9], ".", ":", "!", "?", "$", "%", "@" in the text.
# 
# 
# END_DESC

import re

signs = ('.', ':', '!', '?', '@', '$', '%')


class HackerLanguage:
    def __init__(self) -> None:
        self.message = ''

    def write(self, text):
        self.message += text
    
    def delete(self, N):
        self.message = self.message[:-N]
    
    def send(self):
        return encrypt(self.message)
    
    def read(self, text):
        return decrypt(text)


def searcher(data): # searching and removing dates and times
    temps = []
    infos =[]

    # searching dates
    found = re.search('\d\d\.\d\d\.\d\d\d\d', data) # date in format dd.mm.yyyy
    while found != None:
        indexes = found.span()
        temps.append(data[indexes[0]:indexes[1]])
        infos.append(indexes[0])
        data = data[:indexes[0]] + data[indexes[1]:]
        found = re.search('\d\d\.\d\d\.\d\d\d\d', data)
    
    #searching time
    found = re.search('1000000\d\d:\d\d', data)
    while found != None:
        indexes = found.span()
        temps.append(data[indexes[0]+7:indexes[1]])
        infos.append(indexes[0]+ 7)
        data = data[:indexes[0]+ 7] + data[indexes[1]:]
        found = re.search('1000000\d\d:\d\d', data) #  before time must be space (binary: '1000000')
    return data, temps, infos


def decrypt(data):
    informations = searcher(data)
    data, temps, indexes = informations
    i, j = 0, 0
    string = ''
    part = ''
    temp = temps[0] if len(temps) > 0 else None
    index = indexes[0] if len(indexes) > 0 else None

    for char in data:
        if i == index:
            string += temp
            j += 1
            temp = temps[j] if len(temps) > j else None
            index = indexes[j] if len(indexes) > j else None
        if char not in signs:
            part += char
        else:
            string += char
        if len(part) == 7 or i == len(data) - 1:
            if part == '1000000':
                string += ' '
            elif part:
                string += chr(int(part,2))
            part = ''
        i += 1
    return string


def encrypt(data):
    score = ''
    for char in data:
        if not(char.isdigit()) and char not in signs:
            if char == ' ':
                score += '1000000'
            else:
                score += bin(ord(char))[2:]
        else:
            score += char
    return score