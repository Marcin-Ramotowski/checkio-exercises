#!/usr/bin/env checkio --domain=py run cipher-dict-decryption

# In this mission, you need to convert a nested cipher dictionary to a plain text to according to the following steps. This conversion is opposite to one inCipher Dictmission.
# 
# Starting from top dictionary, take keys and sort them in correct order into a block of digits. Blocks order should be strictly alternated and the first block must be ascending. Check value (dict as well) of each key in its turn to find next block and get new keys to check later in their turns.
# 
# Concatenate all founded blocks into single decimal number.
# 
# Convert this decimal value into a hexadecimal number and convert the result to string.
# 
# The description may be confusing, so let's look at the example.
# 
# 
# 
# Input:A cipher data as a dictionary.
# 
# Output:An original text as a string.
# 
# Precondition:The text contain only ASCII symbols >= 32.
# 
# 
# END_DESC

def get_plain(cipher: dict) -> str:
    # your code here
    return ""


if __name__ == "__main__":
    print("Example:")
    print(
        get_plain(
            {
                1: {6: {3: {}}},
                2: {6: {5: {}}, 9: {0: {}, 5: {}}},
                3: {4: {5: {}}},
                6: {6: {4: {}}},
            }
        )
    )

    # These "asserts" are used for self-checking and not for an auto-testing
    assert (
        get_plain(
            {
                1: {6: {3: {}}},
                2: {6: {5: {}}, 9: {0: {}, 5: {}}},
                3: {4: {5: {}}},
                6: {6: {4: {}}},
            }
        )
        == "python"
    )
    assert (
        get_plain(
            {
                1: {
                    1: {
                        8: {
                            8: {
                                8: {
                                    0: {
                                        0: {
                                            1: {3: {9: {6: {}, 9: {}}}, 6: {2: {0: {}}}}
                                        },
                                        1: {
                                            8: {
                                                0: {
                                                    1: {1: {}, 7: {}, 9: {}},
                                                    7: {0: {}, 2: {}, 3: {}},
                                                },
                                                5: {7: {8: {}}},
                                            }
                                        },
                                        2: {
                                            1: {0: {2: {2: {}}}},
                                            4: {8: {9: {0: {}, 5: {}}}},
                                        },
                                    }
                                }
                            }
                        }
                    }
                }
            }
        )
        == "You can read me."
    )

    print("Coding complete? Click 'Check' to earn cool rewards!")