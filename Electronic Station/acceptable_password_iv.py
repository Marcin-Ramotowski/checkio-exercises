#!/usr/bin/env checkio --domain=py run acceptable-password-iv

# In this mission you need to create a password verification function.
# 
# Those are the verification conditions:
# 
# the length should be bigger than 6;should contain at least one digit, but it cannot consist of just digits;if the password is longer than 9 - previous rule (about one digit), is not required.Input:A string.
# 
# Output:A bool.
# 
# 
# END_DESC

# Taken from mission Acceptable Password III

# Taken from mission Acceptable Password II

# Taken from mission Acceptable Password I

def is_acceptable_password(password: str) -> bool:
    x=len(password)
    if x > 9:
        return True
    y = False if x <= 6 else True
    if password.isdigit() is True:
        return False
    z = False
    if y is True:
        for char in password:
            if char.isdigit() is True:
                z = True
    return z


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('short54') == True
    assert is_acceptable_password('muchlonger') == True
    assert is_acceptable_password('ashort') == False
    assert is_acceptable_password('muchlonger5') == True
    assert is_acceptable_password('sh5') == False
    assert is_acceptable_password('1234567') == False
    assert is_acceptable_password('12345678910') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")