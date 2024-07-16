#!/usr/bin/env checkio --domain=py run combining-celebrity-names

# Combining the first names of beloved celebrity couples to a catchy shorthand for mass media consumption turns out to be simple to automate.
# 
# Start by counting how many maximal groups of consecutive vowels (aeiou, as to keep this problem simple, the letteryis always a consonant) exist inside thefirstname. For example, "brad" and "jean" have one vowel group, "jeanie" and "britain" have two, and "angelina" and "alexander" have four. Note that a vowel group can contain more than one vowel, as in the word "queueing" with an entire fiver.
# 
# If the first name has only one vowel group, keep only the consonants before that group and lose everything else. For example, "ben" becomes "b", and "brad" becomes "br". Otherwise, if the first word hasn> 1 vowel groups, keep everything before thesecond lastvowel groupn– 1. For example, "angelina" becomes "angel" and "alexander" becomes "alex".
# 
# Concatenate that string with the string that you get by removing all consonants from the beginning of thesecondname.
# 
# Input:Two strings(str).
# 
# Output:String(str).
# 
# Examples:
# 
# assert brangelina("brad", "angelina") == "brangelina"
# assert brangelina("angelina", "brad") == "angelad"
# assert brangelina("sheldon", "amy") == "shamy"
# Preconditions:firstandsecondnames are guaranteed to consist of the 26 lowercase English letters, and each name will have at least one vowel and one consonant somewhere.
# 
# The mission was taken fromPython CCPS 109. It is taught forRyerson Chang School of Continuing EducationbyIlkka Kokkarinen
# 
# 
# END_DESC

def brangelina(first: str, second: str) -> str:
    # your code here
    return ""


print("Example:")
print(brangelina("brad", "angelina"))

# These "asserts" are used for self-checking
assert brangelina("brad", "angelina") == "brangelina"
assert brangelina("angelina", "brad") == "angelad"
assert brangelina("sheldon", "amy") == "shamy"

print("The mission is done! Click 'Check Solution' to earn rewards!")