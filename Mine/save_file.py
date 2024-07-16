#!/usr/bin/env checkio --domain=py run save-file

# You are given a sequence of names of existing files and a single filename that need to be saved into the sequence.
# 
# If a file with the same name already exists in the sequence, a numerical suffix(n)should be added to the file name (the first integern, with which a new filename is not present in the sequence). Note, that filename may already include one or more suffixes.
# 
# The function should return the name with which the file will be saved into the sequence.
# 
# Input:Tuple of strings(str)and a string.
# 
# Output:String.
# 
# Examples:
# 
# assert save_file((), "name.txt") == "name.txt"
# assert save_file(("test.txt",), "name.txt") == "name.txt"
# assert save_file(("name.txt",), "name.txt") == "name(1).txt"
# assert (
#     save_file(("name(56).txt", "name(56)(1).txt", "name(56)(2).txt"), "name(56).txt")
#     == "name(56)(3).txt"
# )
# 
# END_DESC

def save_file(files: tuple[str, ...], file: str) -> str:
    # your code here
    return ""


print("Example:")
print(save_file(("name.txt",), "name.txt"))

# These "asserts" are used for self-checking
assert save_file((), "name.txt") == "name.txt"
assert save_file(("test.txt",), "name.txt") == "name.txt"
assert save_file(("name.txt",), "name.txt") == "name(1).txt"
assert (
    save_file(("name(56).txt", "name(56)(1).txt", "name(56)(2).txt"), "name(56).txt")
    == "name(56)(3).txt"
)

print("The mission is done! Click 'Check Solution' to earn rewards!")