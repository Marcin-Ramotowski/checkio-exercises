#!/usr/bin/env checkio --domain=py run gate-puzzles

# Aoccdrnig to a rscheearch at Cmabrigde Uinervtisy, it deosn't mttaer in waht oredr the        ltteers in a wrod are,        the olny iprmoetnt tihng is taht the frist and lsat ltteer be at the rghit pclae. The rset        can be a toatl mses        and you can sitll raed it wouthit porbelm. Tihs is bcuseae the huamn mnid deos not raed        ervey lteter by istlef,        but the wrod as a wlohe.
# -- Unknown Author.
# 
# "Ennyn Durin Aran Moria. Pedo mellon a Minno. Im Narvi hain echant. Celebrimbor o Eregion        tethant. I thiw        hin"
# "The Doors of Durin, Lord of Moria. Speak friend and enter. I Narvi made them. Celebrimbor        of Hollin drew these        signs."
# -- "The Fellowship of the Ring" J. R. Tolkien
# 
# The Doors of Durin were opened by Gandalf and the Fellowship entered inMoria.    As they found, this underground kingdom has gates on every passageway. Each gate has a written    message which    contains the key word. Luckily, Gimli knows how to recognize the key in these messages. It's the    most "like" word,    which has the greatest average "likeness" coefficient with other words in the message.
# 
# You are given a message. You need to pick out all words (a consecutive sequence of letters or a    single letter),    calculate the "likeness" coefficients with other words, take an average of them and choose the    greatest. Count    "likeness" coefficient even for the same words (of course it's 100). If several words have the    same resulting value,    then choose the word closest to the end of the message. Words in the message can be separated by    whitespaces and    punctuation. There are no numbers.
# 
# "Likeness" coefficient for two words is measured in percentages using the following rules:
# - Letter case does not matter ("A" == "a");
# - If the first letters of the words are equal, then add 10%;
# - If the last letters of the words are equal, then add 10%;
# - Add length comparison as
# (length_of_word1 / length_of_word2) * 30%, if    length_of_word1 ≤ length_of_word2;
# , else    (length_of_word2 / length_of_word1) * 30%
# - Take all unique letters from the both words in one set and count how many letters appear in    the both words. Add to    the coefficient (common_letter_number / unique_letters_numbers) * 50;
# 
# So the maximum coefficient of likeness is 100%. For example: for the words "Bread" and "Beard".
# 
# The result should be given in the lower case.
# 
# Let's look at an example. The message "Friend Fred and friend Ted."    First, pick out words - ("friend", "fred", "and", "friend", "ted").    Next we calculate "likeness" for the first word with other.    "friend" and "fred" have the same first and last letters, so add 20.    Then length comparison: the length of "fred" is lesser than "friend", so add (4/6)*30=20.    The last rule: for these words unique letters are "definr" and the intersected letters are    "defr".    So add (4/6)*50≈33.333. And the summary is 73.333.
# This way we will count all other coefficients and get the following table    (results are rounded just for simplicity). The greatest average is 62.976 and the result is    "friend".
# 
# 
#         | friend  | fred    | and     | friend  | ted     |
# --------|---------|---------|---------|---------|---------|
# friend  | ------  | 73.333  | 39.286  | 100.0   | 39.286  |
# fred    | 73.333  | ------  | 40.833  | 73.333  | 52.5    |
# and     | 39.286  | 40.833  | ------  | 39.286  | 50.0    |
# friend  | 100.0   | 73.333  | 39.286  | ------  | 39.286  |
# ted     | 39.286  | 52.5    | 50.0    | 39.286  | ------  |
# --------|---------|---------|---------|---------|---------|
# sum     | 251.905 | 239.999 | 169.405 | 251.905 | 181.072 |
# average | 62.976  | 60      | 42.351  | 62.976  | 45.268  |
# 
# Input:A message as a string (unicode)
# 
# Output:The keyword as a string.
# 
# Precondition:
# 0 < len(message)
# all(x in (string.ascii_letters + string.punctuation + " ") for x in message)
# 
# 
# END_DESC

import string

def find_word(message: str) ->str:
    # collecting words
    message = message.lower()
    for char in string.punctuation:
        if char in message:
            message = message.replace(char,'')
    words = message.split()
    scoreboard = [[word,[]] for word in words] # it wouldn't be a simple dict, because dict can't store two identical keys
    
    for i1, word1 in enumerate(words):
        for i2, word2 in enumerate(words):
            if i1 != i2:
                # calculating points
                score = 0
                first = [word1[0], word2[0]]
                last = [word1[-1], word2[-1]]
                if first[0] == first[1]:
                    score += 10
                if last[0] == last[1]:
                    score += 10
                score += (len(word1)/ len(word2))* 30 if len(word1) <= len(word2) else (len(word2)/ len(word1))* 30
                unique = set(word1 + word2)
                commons = [letter for letter in unique if letter in word1 and letter in word2]
                score += len(commons)/ len(unique) * 50

                # update scoreboard
                wordscores = scoreboard[i1][1]
                wordscores.append(round(score,3))
                scoreboard[i1][1] = wordscores

    # searching a winner
    n = len(scoreboard[0][1])
    sums = [[score[0],sum(score[1])] for score in scoreboard]
    averages = [[score[0],score[1]/n] for score in sums]
    theBestScore = max(averages, key = lambda x : x[1])[1]
    winners = [avg for avg in averages if avg[1] == theBestScore]
    return winners[-1][0] # name's last of the winners