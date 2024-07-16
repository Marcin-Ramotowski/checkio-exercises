#!/usr/bin/env checkio --domain=py run huffman-encode

# Huffman code is a specific type of optimal prefix code that is commonly used for lossless data compression. The algorithm was developed by David A. Huffman while he was a Sc.D. student at MIT and was published in 1952.
# 
# The output from Huffman's algorithm can be viewed as a variable-length code table for encoding a source symbol.The algorithm derives this table from the estimated probability or frequency of occurrence (weight) for each possible value of the source symbol.As in other entropy encoding methods, more common symbols are generally represented using fewer bits than less common symbols.
# 
# The simplest construction algorithm uses a priority queue, where the node with the lowest frequency is given the highest priority.
# 
# Create a leaf node for each symbol and add it to the priority queue.While there is more than one node in the queue:Remove the two nodes of highest priority (lowest frequency) from the queue.Create a new internal node with these two nodes as children and with a frequency equal to the sum of the two nodes' frequencies.Add the new node to the queue.The remaining node is the root node, and the tree is complete.It'simportant to notethat for our task, nodes with the same frequency have different priorities. Symbols with lower ASCII code have a higher priority, for example, 'A' has a higher priority than 'B', and 'DZ' has a higher priority than 'E'.
# 
# Mark the connections between nodes with 0 and 1 (the connection with the higher priority node with 0, and the other with 1).The digits along the way from the root node to the leaf form the code for the leaf's symbol.The result for our task is a source string in which all the symbols have been replaced by their codes.
# 
# Input:String(str).
# 
# Output:String(str).
# 
# Precondition:Given string maximum length is 32000. String contains letters and spaces (a-z, A-Z, " ").
# 
# Idea for the mission was taken from local school challenge for kids.
# 
# Screen by Cmglee forwiki.
# 
# 
# END_DESC

def huffman_encode(s: str) -> str:
    # your code here
    return ""


print("Example:")
print(huffman_encode("BADABUM"))

# These "asserts" are used for self-checking
assert huffman_encode("BADABUM") == "1001110011000111"
assert (
    huffman_encode("A DEAD DAD CEDED A BAD BABE A BEADED ABACA BED")
    == "1000011101001000110010011101100111001001000111110010011111011111100010001111110100111001001011111011101000111111001"
)
assert (
    huffman_encode("no devil lived on")
    == "100101111000001110010011111011010110001000111101100"
)
assert huffman_encode("an assassin sins") == "110111100110001100010111110001011110"
assert huffman_encode("aaaa") == "0000"
assert huffman_encode("") == ""
assert huffman_encode("T isnt t") == "01000011101100110011"
assert (
    huffman_encode("how quickly daft jumping zebras vex")
    == "00101011011011011001111101000111111110100101010111001100000011110000011001011001000101001011011100011011000010011011101000111111010000111101000111010011000110111"
)
assert (
    huffman_encode("amazingly few discotheques provide jukeboxes")
    == "1100100010110011100001110001111110100001011011101111100100010111101111010111101111100110100011111111010000101010010010111101001000011010100101001111110110011011111110100000001001110001010011001001011"
)

print("The mission is done! Click 'Check Solution' to earn rewards!")