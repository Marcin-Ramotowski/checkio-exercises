#!/usr/bin/env checkio --domain=py run yaml-list-and-comments

# In the 3rd YAML parsing task, we’re going to look into arrays.
# 
# (Remember that in this mission you must take into account the conditions of previous missions. It means that your solution should work with dictionaries from a previous mission and with arrays from this one.)
# 
# A simple example:
# 
# 
# - write some
# - "Alex Chii"
# - 89
# 
# [
#   "write some", 
#   "Alex Chii", 
#   89
# ]
# As you can see in the above example, the format for values is the same as we’ve used in the previous task for the format of values in the dictionary.
# 
# It's time to add comments to the format.
# 
# Everything indicated after the # sign should be ignored by the parser.
# 
# 
# # comment
# - write some # after
# # one mor
# - "Alex Chii #sir "
# - 89 #bl
# 
# [
#   "write some", 
#   "Alex Chii #sir ", 
#   89
# ]
# As you may have noticed, the comments inside the string aren’t considered as comments, they are treated as part of the string, which makes sense.
# 
# Input:Format string.
# 
# Output:An object.
# 
# Precondition:The YAML 1.2 standard is being used.
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
    elif text in ['null','-']:
        return None
    elif 'null' in text:
        return 'null'
    else:
        return text

def preparing(text:str):
    if text.find('-') != -1:
        text = text.removeprefix('- ')
    if text.find("\\") != -1:
        text = text.replace("\\", '')
    l = len(text)
    if text.count('"') == 1:
        text = text.strip('"')
    if text.find('"') == 0 and text.rfind('"') == l-1:
        if text.count('"') > 2:
                text = list(text)
                text.pop(0)
                text.pop(-1)
                text = "".join(text)
                return text
        return text.strip('"')
    else:
        return text.strip().strip("'")
    
def remove_commants(text:list):
    lines = []
    for line in text:
        t= line.find('#')
        if t != -1:
            quotesIndexes = [i for i, char in enumerate(line) if char == '"']
            if len(quotesIndexes) == 2:
                a,b = quotesIndexes
                if a >= t >= b:
                    line = line[:t]
            else: 
                line = line[:t]
        lines.append(line)
    return lines

def yaml(text:str):
    l = len(text)
    if text.rfind(":") == l-1:
        text = text + ' null'
    if text.find(":\n") != -1:
        text = text.replace(":\n", ": null\n")
    items = text.split("\n")
    if '#' in text:
        items = remove_commants(items)
    isTable = False
    for item in items:
        if item.find('-') == 0:
            isTable = True
            break
    if isTable:
        table = [converter(preparing(item)) for item in items if '' not in [item, item.strip()]]
        return table
    lexicon = [converter(preparing(string)) for item in items for string in item.split(": ") if '' not in [string, string.strip()]]
    return dict(sorted(zip(lexicon[0::2], lexicon[1::2])))


if __name__ == '__main__':
    print("Example:")
    print(yaml('- write some\n- "Alex Chii"\n- 89'))
    print(yaml('# comment\n'
 '- write some # after\n'
 '# one mor\n'
 '- "Alex Chii #sir "\n'
 '- 89 #bl'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert yaml('- write some\n- "Alex Chii"\n- 89') == ['write some', 'Alex Chii', 89]
    assert yaml('# comment\n'
 '- write some # after\n'
 '# one mor\n'
 '- "Alex Chii #sir "\n'
 '- 89 #bl') == ['write some', 'Alex Chii #sir ', 89]
    assert yaml('- 1\n- 2\n- 3\n\n- 4\n\n\n\n- 5') == [1, 2, 3, 4, 5]
    assert yaml('-\n-\n-\n- 7') == [None, None, None, 7]
    print("Coding complete? Click 'Check' to earn cool rewards!")