#!/usr/bin/env checkio --domain=py run tricky-string

# ...Samantha sat at her desk, her eyes scanning the words on the page in front of her. She had been reading the same paragraph over and over, 		but her mind couldn't seem to grasp the meaning behind the words. Frustration began to creep in as she tried to focus, but the words seemed 		to blur together. It was as if the author's thoughts were hidden in a maze, and she was struggling to find the right path. Samantha took a 		deep breath and closed her eyes, trying to clear her mind. Finally, a breakthrough. The thought she had been searching for emerged from the 		text, and she continued on with renewed determination. Sometimes, reading is a journey, and finding the right thought can be the most 			challenging part.
# 
# You are given a string. Somewhere in that text a word "CheckIO" has hidden. Your task is to find a place where word is hiding and make the minimum number of replacements to get it. Let's proceed with an example: for a string"xheckIO"you should replace only one symbol ("x" to "C") to get a desired word, on the other hand we can try to find it in more complex string:"CheckzzVSCheckIz", right answer here will be a string"CheckzzVSCheckIO"(only one replacemend has made "z" to "O").
# 
# Every string contains at least one of seven characters of the word "CheckIO" and there are enough symbols around it to obtain the necessary word.If there are several ways to complete the task, just put the word in the first suitable place for that.Input:A string(str).
# 
# Output:A string(str).
# 
# Precondition:The text can contain only [a-z, A-Z],6 < len(string) < 100
# 
# 
# END_DESC

def tricky_string(text: str) -> str:
    # your code here
    return ""


print("Example:")
print(tricky_string("Checkio"))

# These "asserts" are used for self-checking
assert tricky_string("checkIO") == "CheckIO"
assert tricky_string("zcheckzz") == "zCheckIO"
assert tricky_string("SoManyChoicesHere") == "SoManyCheckIOHere"

print("The mission is done! Click 'Check Solution' to earn rewards!")