#!/usr/bin/env checkio --domain=py run conversion-into-camelcase

# Your mission is to convert the name of a function (a string) from the Python format (for example "my_function_name") into CamelCase ("MyFunctionName"), where the first char of every word is in uppercase and all words are concatenated without any intervening characters.
# 
# Input:A function name as a string.
# 
# Output:The same string, but in CamelCase.
# 
# Precondition:
# 0 < len(string) <= 100
# Input data won't contain any numbers.
# 
# 
# 
# END_DESC

def to_camel_case(name):
    string = name[0].upper()
    i = 1
    while i < len(name):
        if name[i] == '_':
            i += 1
            string += name[i].upper()
        else:
            string += name[i]
        i += 1
    return string

if __name__ == '__main__':
    print("Example:")
    print(to_camel_case('name'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_camel_case("my_function_name") == "MyFunctionName"
    assert to_camel_case("i_phone") == "IPhone"
    assert to_camel_case("this_function_is_empty") == "ThisFunctionIsEmpty"
    assert to_camel_case("name") == "Name"
    print("Coding complete? Click 'Check' to earn cool rewards!")