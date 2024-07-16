#!/usr/bin/env checkio --domain=py run latest-iso-datetime

# In this task, you need to return the later datetime string between the given two.
# 
# Input:Two strings.
# 
# Output:String.
# 
# Examples:
# 
# assert get_latest("2007-03-04T21:08:12", "2007-03-04T21:08:12") == "2007-03-04T21:08:12"
# assert get_latest("2027-09-01T01:03:10", "1997-04-15T11:18:14") == "2027-09-01T01:03:10"
# assert get_latest("0001-01-01T01:01:01", "3000-11-16T13:27:02") == "3000-11-16T13:27:02"
# Preconditions:Datetime arguments >= 0001-01-01T01:01:01.
# 
# 
# END_DESC

def get_latest(dt1str: str, dt2str: str) -> str:
    # your code here
    return ""


print("Example:")
print(get_latest("2027-09-01T01:03:10", "1997-04-15T11:18:14"))

assert get_latest("2007-03-04T21:08:12", "2007-03-04T21:08:12") == "2007-03-04T21:08:12"
assert get_latest("2027-09-01T01:03:10", "1997-04-15T11:18:14") == "2027-09-01T01:03:10"
assert get_latest("0001-01-01T01:01:01", "3000-11-16T13:27:02") == "3000-11-16T13:27:02"

print("The mission is done! Click 'Check Solution' to earn rewards!")