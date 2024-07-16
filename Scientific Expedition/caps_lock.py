#!/usr/bin/env checkio --domain=py run caps-lock

# Joe Palooka has fat fingers, so he always hits the “Caps Lock” key whenever he actually intends to hit the key  “a” by itself. (When Joe tries to type in some accented version of “a” that needs more keystrokes to conjure the accents, he is more careful in the presence of such raffinated characters ([Shift] + [Char]) and will press the keys correctly.) Compute and return the result of having Joe type in the given text. The “Caps Lock” key affects only the letter keys from “a” to “z” , and has no effect on the other keys or characters. “Caps Lock” key is assumed to be initially off.
# 
# For Joe's keyboard, Caps Lock is always uppercase a letter. That means if Caps Lock is on, and Joe does Shift + b - he gets 'B' (in upper case) printed.
# 
# Input:A string. The typed text.
# 
# Output:A string. The showed text after being typed.
# 
# The mission was taken from Python CCPS 109 Fall 2018. It is taught for Ryerson Chang School of Continuing Education byIlkka Kokkarinen
# 
# 
# END_DESC

def bigger_together(ints):
    ints = sorted(list(map(str,ints)),key=lambda x: x[0])
    for i in range(len(ints)-1):
        if int(ints[i]+ints[i+1])>int(ints[i+1]+ints[i]):
            ints[i],ints[i+1] = ints[i+1],ints[i]
    return int(''.join(ints[::-1]))-int(''.join(ints))


if __name__ == '__main__':
    print("Example:")
    print(caps_lock("Why are you asking me that?"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert caps_lock("Why are you asking me that?") == "Why RE YOU sking me thT?"
    assert caps_lock("Always wanted to visit Zambia.") == "AlwYS Wnted to visit ZMBI."
    print("Coding complete? Click 'Check' to earn cool rewards!")