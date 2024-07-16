#!/usr/bin/env checkio --domain=py run convert-date

# This function should take a date string in the formatdd/mm/yyyyand convert it to the formatyyyy-mm-dd. If the input is not in the correct format, the function should return an error message"Error: Invalid date.".
# 
# 
# 
# Input:String(str).
# 
# Output:String(str).
# 
# Examples:
# 
# assert convert_date("25/12/2021") == "2021-12-25"
# assert convert_date("01/01/2000") == "2000-01-01"
# assert convert_date("15/06/1995") == "1995-06-15"
# assert convert_date("29/02/2020") == "2020-02-29"
# Preconditions:the input should be a string: date ∈ string.
# 
# 
# END_DESC

def convert_date(date: str) -> str:
    # your code here
    return ""


print("Example:")
print(convert_date("01/01/2023"))

# These "asserts" are used for self-checking
assert convert_date("25/12/2021") == "2021-12-25"
assert convert_date("01/01/2000") == "2000-01-01"
assert convert_date("15/06/1995") == "1995-06-15"
assert convert_date("29/02/2020") == "2020-02-29"
assert convert_date("10/10/2010") == "2010-10-10"
assert convert_date("31/05/1985") == "1985-05-31"
assert convert_date("07/08/1960") == "1960-08-07"
assert convert_date("02/09/1999") == "1999-09-02"
assert convert_date("30/04/1975") == "1975-04-30"
assert convert_date("29/02/2019") == "Error: Invalid date."
assert convert_date("30/04/1975/1") == "Error: Invalid date."

print("The mission is done! Click 'Check Solution' to earn rewards!")