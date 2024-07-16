#!/usr/bin/env checkio --domain=py run jumbled-letters

# You may have seen the following meme text on Internet (click the text if you want to read its "normal" version):
# 
# Aoccdrnig to a rsceearh at Cmabrigde Uinervtisy, it deosn't mttaer in waht oredr the ltteers in a wrod are, the olny iprmoetnt tihng is taht the frist and lsat ltteer be at the rghit pclae. The rset can be a toatl mses and you can sitll raed it wouthit porbelm. Tihs is bcuseae the huamn mnid deos not raed ervey lteter by istlef, but the wrod as a wlohe.
# 
# According to a research at Cambridge University, it doesn't matter in what order the letters in a word are, the only important thing is that the first and last letter be at the right place. The rest can be a total mess and you can still read it without problem. This is because the human mind does not read every letter by itself but the word as a whole.
# 
# Well, there areelementsof truth in this. Here is a very interestingarticlefrom the real Cambridge University researcher, who is breaking down the meme and explain the phenomena.
# 
# Let's try to evaluate a level of jumbling. In this mission you are given two words - normal and jumbled version. If the jumbled one is not a version of a normal or rule is not followed, you function must return-1. For the totally same looking words return0, of course. Otherwise, exclude first and last characters (they are not jumbled according to the rule) and return an average distance (rounded to 2 digits) between normal position of a character and its jumbled position.
# 
# If there are two or more same letters in a word, consider that the first appearance of a character in a normal version is equivalent to the first appearance of that character in a jumbled version etc.
# 
# Look at the example.
# 
# 
# 
# Input:Two strings(str).
# 
# Output:Float number(float).
# 
# Examples:
# 
# assert jumbled("vehicle", "vheclie") == 1.2
# assert jumbled("checkpoint", "cehkipont") == -1
# assert jumbled("doctor", "doctor") == 0
# assert jumbled("research", "rsceearh") == 1.67
# 
# END_DESC

def jumbled(word1: str, word2: str) -> float:
    # your code here
    return 0


print("Example:")
print(jumbled("vehicle", "vheclie"))

# These "asserts" are used for self-checking
assert jumbled("vehicle", "vheclie") == 1.2
assert jumbled("checkpoint", "cehkipont") == -1
assert jumbled("doctor", "doctor") == 0
assert jumbled("research", "rsceearh") == 1.67
assert jumbled("tango", "ogant") == -1

print("The mission is done! Click 'Check Solution' to earn rewards!")