#!/usr/bin/env checkio --domain=py run count-morse

# Everyone and their brother has surely heard of Morse codes, the classic encoding of text into binary symbols canonically denoted with dots and dashes. However, this coding is technically ternary since the pause between two letters is really a separate symbol, analogous to how whitespace between the words you are now reading are characters just the same as those with visible glyphs. Without the pauses separating the individual codewords, the same message could theoretically be decoded in exponentially many different ways.
# 
# Your function receives themessagewithout pauses along with theletterswhose encoding originally produced thatmessage. Your function should count how many different permutations of thoselettersproduce that exact samemessage. Each individual character is guaranteed to appear in letters at most once, all symbols and letters must be used.
# 
# Input:Two arguments: Morse encoded message and letters sequence as strings(str).
# 
# Output:Number of permutations as integer(int).
# 
# Examples:
# 
# assert count_morse("-------.", "omg") == 2
# assert count_morse(".....-.-----", "morse") == 4
# assert count_morse("-..----.......-..-.", "xtmisuf") == 4
# Precondition:len(set(letters)) == len(letters)
# 
# This task is taken from the course CCPS 109 Computer Science I, Version of December 21, 2022, as taught byIlkka Kokkarinen.
# 
# Hey, pss! Click here to get a small hint from the author, if you need it.One of the way of solving is to use recursion, aided by a tasty serving of some@lru_cachemagic to prevent your recursion from redundantly exploring identical subproblems multiple times.
# 
# 
# END_DESC

D = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
}


def count_morse(message: str, letters: str) -> int:
    # your code here
    return 0


print("Example:")
print(count_morse("-------.", "omg"))

# These "asserts" are used for self-checking
assert count_morse("-------.", "omg") == 2
assert count_morse(".....-.-----", "morse") == 4
assert count_morse("-..----.......-..-.", "xtmisuf") == 4

print("The mission is done! Click 'Check Solution' to earn rewards!")