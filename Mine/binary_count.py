#!/usr/bin/env checkio --domain=py run binary-count

# For the Robots the decimal format is inconvenient. If they need to count to "1",    their computer brains want to count it in the binary representation of that number.    You can read more about binaryhere.
# 
# You are given a number (a positive integer).    You should convert it to the binary format and count how many unities (1) are in the number spelling.    For example: 5 = 0b101 contains two unities, so the answer is 2.
# 
# Input:A number as a positive integer.
# 
# Output:The quantity of unities in the binary form as an integer.
# 
# Precondition:0 < number ≤ 232
# 
# 
# END_DESC

checkio = lambda x: bin(x).count('1')