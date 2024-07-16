#!/usr/bin/env checkio --domain=py run exec-quine

# "If, however, in our perversity we are still bent on constructing    a sentence that does attribute falsity unequivocally to itself, we can do so thus:
# 
# `Yields a falsehood when appended to its own quotation` yields a falsehood when appended to its own quotation.
# 
# This sentence specifies a string of nine words and says of this string that if you put it down twice,    with quotation marks around the first of the two occurrences, the result is false.    But that result is the very sentence that is doing the telling. The sentence is true if and only if it is false,    and we have our antinomy."
# -- "The Ways of Paradox and Other Essays" W.V. Quine 1976
# 
# A quine is a computer program which takes no input and produces a copy of its own source code as the only output.    These types of programs are often known as "self-replicating programs", "self-reproducing programs",    or"self-copying programs" in the computer sciences fields.
# 
# You should implement a function (this function will be called “quine”)    which will reproduce itself within an environment.    Lets refer to the entire code as ANSWER_CODE, and this code contains the quine function definition.    If we executequine(), the result should be a string which is a copy of ANSWER_CODE.    You can check this in your local environment with the following:exec(ANSWER_CODE);quine()
# 
# In this mission, there is only one test. You should be careful with newlines, tabs and white-spaces,    because the test compares ANSWER_CODE and the functions result as they are.    In this mission the main goal is to develop an original and creative solution.    This missions rewards are based on peer reviews, so the votes from other users, will give you increased exp points.
# 
# Input:Nothing.
# 
# Output:The code as a string.
# 
# 
# END_DESC

def quine():
    return "def quine()\n    return foobar"