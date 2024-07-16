#!/usr/bin/env checkio --domain=py run postfix-evaluation

# When arithmetic expressions are given in the familiarinfixnotation2 + 3 × 4, parentheses nudge the different evaluation order to differ from the usualPEMDASorder determined byprecedenceand associativity of each operator. The alternativepostfixnotation (also known asReverse Polish Notation) may first look weird to people accustomed to the conventional infix. However, postfix notation turns out to be easier for machines, since it allows encodinganyintended evaluation order without any parentheses!
# 
# A postfix expression is given as list ofitemsthat can be either individual integers, or one of the strings '+', '-', '*' and '/' to denote the four basic arithmetic operators. To evaluate a postfix expression use an initially empty stack. Loop through the items one by one, from left to right. Whenever the current item is an integer, just append it to the end of the list. Otherwise, pop two items from the end of the list to perform that operation on, and append the result back to the list. Assuming that items is a legal postfix expression, which is guaranteed in this problem so that you don’t need to perform any error detection or recovery, once all items have been processed, the lone number left in the stack becomes the final answer.
# 
# To avoid the intricacies of floating point arithmetic, you should perform the division operation using the Python integer division operator//that truncates the result to the integer part. Furthermore, to avoid the crash from dividing by zero, this problem comes with an artificial (yetmathematicallyperfectly sound) rule that division by zero gives a zero result, instead of crashing.
# 
# 
# 
# By adding more operators and another auxiliary stack, an entire Turing-complete programming language can be built around postfix evaluation. Visit“Forth”page to learn more of this ingeniously simple concatenative programming language.
# 
# Input:List of integers(int)and strings(str).
# 
# Output:Integer(int).
# 
# Examples:
# 
# assert postfix_evaluate([2, 3, "+", 4, "*"]) == 20
# assert postfix_evaluate([2, 3, 4, "*", "+"]) == 14
# assert postfix_evaluate([3, 3, 3, "-", "/", 42, "+"]) == 42
# The mission was taken from Python CCPS 109. It is taught for Ryerson Chang School of Continuing Education byIlkka Kokkarinen
# 
# 
# END_DESC

from typing import Union


def postfix_evaluate(items: list[Union[int, str]]) -> int:
    # your code here
    return 0


print("Example:")
print(postfix_evaluate([1, 2, "+"]))

# These "asserts" are used for self-checking
assert postfix_evaluate([2, 3, "+", 4, "*"]) == 20
assert postfix_evaluate([2, 3, 4, "*", "+"]) == 14
assert postfix_evaluate([3, 3, 3, "-", "/", 42, "+"]) == 42

print("The mission is done! Click 'Check Solution' to earn rewards!")