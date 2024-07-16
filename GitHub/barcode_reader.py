#!/usr/bin/env checkio --domain=py run barcode-reader

# Learning barcode specifications and implementing a barcode reader with Python.
# 
# This time I will useEAN-13 (from Wikipedia).
# 
# The input is a String of length 95 representing the barcode. Each databit is displayed by an underscore or space. An underscore is the bar area. The input may be reversed. You should decode the barcode so that the output was a String of length 13.
# 
# In case a barcode does not conform to the specifications, return None.
# 
# The input final digit is the checksum. It is calculated from the other 12 digits, but in this mission it may be wrong. You must return None for this.
# 
# Input:The image of the barcode is a String of length 95. It consists only of underscores or spaces.
# 
# Output:The decoded barcode number is a String of length 13 or None.
# 
# How it is used:
# understand the mechanism of a barcode.
# 
# Precondition:
# len(barcode) == 95all(b in ('_', ' ') for b in barcode)
# 
# 
# END_DESC

def barcode_reader(kod,isReversed=False):
    binkod = ''
    for znak in kod:
        if znak == "_":
            binkod += '1'
        else:
            binkod += '0'
    if binkod[0:3] != '101': #START
        return None
    if binkod[45:50] !='01010': #MIDDLE
        return None
    if binkod[92:95] != '101': #END
        return None
    binkod = binkod[3:45] + binkod[50:92]
    modules = [binkod[i - 7:i] for i in range(7, len(binkod) + 1, 7)]
    lexicon = {
        '0001101': '0A', '0100111': '0B', '1110010': '0C',
        '0011001': '1A', '0110011': '1B', '1100110': '1C',
        '0010011': '2A', '0011011': '2B', '1101100': '2C',
        '0111101': '3A', '0100001': '3B', '1000010': '3C',
        '0100011': '4A', '0011101': '4B', '1011100': '4C',
        '0110001': '5A', '0111001': '5B', '1001110': '5C',
        '0101111': '6A', '0000101': '6B', '1010000': '6C',
        '0111011': '7A', '0010001': '7B', '1000100': '7C',
        '0110111': '8A', '0001001': '8B', '1001000': '8C',
        '0001011': '9A', '0010111': '9B', '1110100': '9C'}

    score = ''
    letters = ''
    check = [True if module in lexicon else False for module in modules]
    if all(check):
        for i, module in enumerate(modules):
            value = lexicon[module]
            score += value[0]
            if i < 6:
                if value[1] == 'C':
                    return barcode_reader(kod[::-1])
                letters += value[1]
    else:
        if isReversed:
            return None
        else:
            kod = kod[::-1]
            return barcode_reader(kod, True)

    lexicon2 = {
        'AAAAAA': '0',
        'AABABB': '1',
        'AABBAB': '2',
        'AABBBA': '3',
        'ABAABB': '4',
        'ABBAAB': '5',
        'ABBBAA': '6',
        'ABABAB': '7',
        'ABABBA': '8',
        'ABBABA': '9'}
    if letters not in lexicon2:
        if not(isReversed):
            kod = kod[::-1]
            return barcode_reader(kod,True)
        else:
            return None
    score = lexicon2[letters] + score
    numbers = list(map(int, score))
    lastdigit = numbers[-1]
    numbers2 = numbers[:-1]
    sumNumbers = sum([n*3 if i % 2 == 1 else n for i, n in enumerate(numbers2)])
    rest = sumNumbers % 10
    controlDigit = 10 - rest
    if controlDigit == 10:
        controlDigit = 0
    if lastdigit == controlDigit:
        return score
    return None


if __name__ == '__main__':
    assert barcode_reader(
        '_ _   _ __ _  ___ __  __  _  __ ____ _  ___ _ _ _ __  __ __ __  _    _ _ ___  _  ___ _   _  _ _'
    ) == '5901234123457', '5901234123457'

    assert barcode_reader(
        '_ _  _  __  _ ___   _ __ _ ____   _  _  _   _ _ _ _ _    __  __ _    _ _ _    _ _    _  ___ _ _'
    ) == '4299687613665', '4299687613665'

    assert barcode_reader(
        '_ _ ___ __  __  _  _  __ ____ _ _   __ __   _ _ _ _ _    _   _  _  _   ___ _  __  __ __ __  _ _'
    ) is None, '0712345678912 : wrong check digit (right: 1)'

    assert barcode_reader(
        '___  _  __  _ ___   _ __ _ ____   _  _  _   _ _ _ _ _    __  __ _    _ _ _    _ _    _  ___ _ _'
    ) is None, 'wrong left guard bar'
    
    assert barcode_reader(
        '_ _  _  __  _ ___   _ __ _ ____   _  _  _   _ _ ___ _    __  __ _    _ _ _    _ _    _  ___ _ _'
    ) is None, 'wrong center bar'

    assert barcode_reader(
        '_ _  _  __  _ ___   _ __ _ ____   _  _  _   _ _ _ _ _    __  __ _    _ _ _    _ _    _  ___ ___'
    ) == None, 'wrong right guard bar'

    print("Check done.")
    print(barcode_reader("_ _ ___  _  _ ___  _   _  _ ___  ___ _   _  _ _ _ __ ___ __ __  __  _  _ ___  ___  _ _ __   _ _"))