#!/usr/bin/env checkio --domain=py run morse-clock

# "di-dah di-di-di-dit di-dah-dah di-dah-dah-dah dah-di-dit dah-di-di-dah",        sound of Morszelizer clanked out loud.
# 
# "What're you doing?" Nikola asked curiously.
# 
# "I'm sending our time logs for the last expedition to headquarters, but it's not an easy task..."        Stephen grumbled, "Can you imagine that with all the computer power at our disposal,        I STILL have to convert this message to Morse-code with only an on/off button... Hrmph... what a pain."        He grumbled at the inconvenience.
# 
# "Let me look at it." Nikola offered his help, "It looks like a pretty easy solution, we could        automate the process."
# 
# "Oh.. you hero of my day." Stephen started excitedly. "So, how do we start        it?"
# 
# "With Python!" Nikola exclaimed.
# 
# Help Stephen to create a module for converting a normal time string to a morse time string.    As you can see in the illustration, a gray circle means on, while a white circle means off.    Every digit in the time string contains a different number of slots.    The first digit for the hours has a length of 2 while the second digit for the hour has a length of 4.    The first digits for the minutes and seconds have a length of 3 while the second digits for the minutes and    seconds have a length of 4.    Every digit in the time is converted to binary representation.    You will convert every on (or 1) signal to dash ("-") and every off (or 0) signal to dot (".").
# 
# 
# 
# An time string could be in the follow formats:"hh:mm:ss","h:m:s"or"hh:m:ss".    The "missing" digits are zeroes. For example, "1:2:3" is the same as "01:02:03".
# 
# The result will be a morse time string with specific format:"h h : m m : s s"where each digits represented as sequence of "." and "-"
# Input:A normal time string as a string (unicode).
# 
# Output:The morse time string as a string.
# Precondition:
# time_stringcontains correct time.
# 
# 
# END_DESC

def checkio(time:str):

    if len(time) < 8:
        time = time.split(":")
        time = map(int,time)
        h,m,s = time
        time = f'{h:02}:{m:02}:{s:02}'
    digits = [int(char) for char in time if char.isdigit()]
    dividers = [8,4,2,1]
    seq = [2,4,3,4,3,4]
    lamps = []

    for i, digit in enumerate(digits):
        signals = [False for i in range(0,seq[i])]
        start = 4 - seq[i]
        k = 0
        for j in range(start,4):
            div = dividers[j]
            q = digit // div
            factor = div * q
            if q >= 1:
                digit -= factor
                signals[k] = True
            k += 1
        lamps.append(signals)

    score = ""
    for n, signals in enumerate(lamps):
        if n in [2,4]:
            score += ": "
        for signal in signals:
            if signal:
                score += "-"
            else:
                score += "."
        score += " "
    return score.rstrip()

if __name__ == '__main__':
    print("Example:")
    print(checkio("10:37:49"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"
    print("Coding complete? Click 'Check' to earn cool rewards!")