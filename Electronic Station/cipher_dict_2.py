#!/usr/bin/env checkio --domain=py run cipher-dict-2

# In this mission, you need to convert a plain text to a nested cipher dictionary according to the following steps. This conversion is opposite to one inCipher Dict (decryption)mission.
# 
# Encode the given plain text to utf-8.
# 
# Convert this value as a hexadecimal number, then convert the result it to a decimal number. (Every digit of this number will be a key in some level of nested dictionary.)
# 
# Split decimal number into blocks with strict ascending/descending order (no same digit repetition allowed in the same block, instead it starts a new one). Blocks order should be strictly alternated and the first block must be ascending. A block may contain one digit of it's necessary to keep alternated order.
# 
# Now, you need to fill nested dictionary. Each separate block of digit includes keys of the same dictionary, the values as always empty dictionaries. Taking blocks from left to right, you create a nested dictionary in such a way that digits of every next block become keys in the next (in creation order) empty dictionary. Keep in mind the order of blocks and order of digits inside each block.
# 
# 
# 
# The description may be confusing, so let's look at the example.
# 
# 
# 
# Input:A plain text as a string.
# 
# Output:A cipher data as a nested dictionary.
# 
# Precondition:The text contain only ASCII symbols >= 32.
# 
# 
# END_DESC

def get_cipher(plain):
    # your code here
    return None


if __name__ == "__main__":
    print("Example:")
    print(get_cipher("hello"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert get_cipher("hello") == {
        4: {4: {8: {3: {7: {0: {4: {}, 7: {}}, 2: {2: {}}}, 8: {3: {}}}}}}
    }
    assert get_cipher("This is a plain text.") == {
        1: {
            3: {
                2: {
                    1: {
                        4: {
                            7: {
                                4: {1: {0: {}, 2: {}, 7: {}}, 4: {9: {}}, 8: {3: {}}},
                                6: {8: {1: {}, 4: {}, 9: {}}},
                            }
                        },
                        9: {5: {5: {6: {1: {}, 4: {}}, 8: {}}}},
                    }
                }
            }
        },
        2: {6: {2: {8: {4: {9: {5: {2: {}, 8: {}}}}}}}},
        3: {
            2: {4: {1: {4: {8: {3: {0: {}, 2: {}}}}}, 3: {5: {3: {5: {4: {}, 7: {}}}}}}}
        },
    }

    print("Coding complete? Click 'Check' to earn cool rewards!")