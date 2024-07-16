#!/usr/bin/env checkio --domain=py run cut-sentence

# Your task in this mission is to truncate a sentence to a length that does not exceed a  given number of characters.
# 
# If the given sentence already is short enough, you don't have to do anything to it. But  if it needs to be truncated, the omission must be indicated by concatenating an ellipsis  ("...") to the end of the shortened sentence.
# 
# The shortened sentence can contain complete words and spaces.
# It must neither contain truncated words nor trailing spaces.
# The ellipsis has been taken into account for the allowed number of characters, so it  does not count against the given length.
# 
# Input:Two arguments:one-line sentence as a string,max length of the truncated sentence as an int.
# 
# Output:The shortened sentence plus the ellipsis (if required) as a  one-line string.
# 
# Precondition:
# line.startswith(' ') == False0 < len(line) ≤ 790 < length ≤ 76all(char in string.ascii_letters + ' ' for char in line)
# 
# 
# END_DESC

cut_sentence = lambda line,n: line if line.isspace() or n >= len(line) else line[:line[:n+1].rfind(' ')] + '...' if n > line.find(' ') else '...'