#!/usr/bin/env checkio --domain=py run yaml-more-types

# This is the second task on parsing YAML. It represents the next step where parsing gets more complicated. The data types, such as null and bool, are being added, and besides that, you’re getting the ability to use quotes in strings.
# 
# Here are some of the examples:
# 
# 
# name: "Bob Dylan"
# children: 6
# 
# {
#   "name": "Bob Dylan", 
#   "children": 6
# }
# As you can see, the string can be put in quotes. It can be both double and single quotes.
# 
# 
# name: "Bob Dylan"
# children: 6
# alive: false
# 
# {
#   "name": "Bob Dylan", 
#   "alive": False, 
#   "children": 6
# }
# true and false are the keywords defining the boolean type.
# 
# 
# name: "Bob Dylan"
# children: 6
# coding:
# 
# {
#   "coding": None, 
#   "name": "Bob Dylan", 
#   "children": 6
# }
# If no value is specified, it becomes undefined. There also is a keyword for this - null.
# 
# Input:A format string.
# 
# Output:An object.
# 
# Precondition:YAML 1.2 is being used withJSON Schema.
# 
# 
# END_DESC

def converter(text):
    if text.isdigit():
        return int(text)
    elif 'true' in text:
        return bool(text)
    elif 'false' in text:
        return False
    elif text == 'null':
        return None
    elif 'null' in text:
        return 'null'
    else:
        return text

def preparing(text:str):
    if text.find("\\") != -1:
        text = text.replace("\\", '')
    l = len(text)
    if text.find('''"''') == 0 and text.rfind('''"''') == l-1:
        if text.count('''"''') > 2:
                text = list(text)
                text.pop(0)
                text.pop(-1)
                text = "".join(text)
                return text
        return text.strip('''"''')
    else:
        return text.strip().strip("'")

def yaml(text:str):
    l = len(text)
    if text.rfind(":") == l-1:
        text = text + ' null'
    if text.find(":\n") != -1:
        text = text.replace(":\n", ": null\n")
    items = text.split("\n")
    lexicon = [converter(preparing(string)) for item in items for string in item.split(": ") if '' not in [string, string.strip()]]
    return dict(sorted(zip(lexicon[0::2], lexicon[1::2])))