#!/usr/bin/env checkio --domain=py run reverse-roman-numerals

# .numeral-table {    margin: auto;    border-collapse: collapse;    text-align: center;  }  .numeral-table * {    border: 1px solid black;    padding: 8px;    width: 50%;  }In this CheckiO missionRoman Numeralsyou have to convert a decimal    number into its representation as a Roman number.
# Here you have to do the same but the other way around.
# 
# You are given a Roman number as a string and your job is to convert this number into  its decimal representation.
# 
# A valid Roman number, in the context of this mission, will only  contain Roman numerals as per the below tableandfollow the rules of  the subtractive notation.
# Check out thisWikipedia articlefor more details on how to form Roman numerals.NumeralValueI1 (unus)V5 (quinque)X10 (decem)L50 (quinquaginta)C100 (centum)D500 (quingenti)M1,000 (mille)
# 
# Input:A Roman number as a string.
# 
# Output:The decimal representation of the Roman number as an int.
# 
# Precondition:
# len(roman_string) > 0
# all(char in "MDCLXVI" for char in roman_string) == True
# 0 < reverse_roman(roman_string) < 4000
# 
# 
# 
# END_DESC

def reverse_roman(data):
    translator = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    translator2 = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
    code = 0
    for char in translator2:
        x = data.count(char)
        if x != -1:
            number = translator2[char]
            code += number * x
            data = data.replace(char, "")
    for char in data:
        number = translator[char]
        code += number
    return code

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert reverse_roman('VI') == 6, '6'
    assert reverse_roman('LXXVI') == 76, '76'
    assert reverse_roman('CDXCIX') == 499, '499'
    assert reverse_roman('MMMDCCCLXXXVIII') == 3888, '3888'
    print('Great! It is time to Check your code!');