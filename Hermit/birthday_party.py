#!/usr/bin/env checkio --domain=py run birthday-party

# I want to know when I will celebrate my birthday.
# 
# The only problem is that often I can't organize a party on the same day as my birthday, because I want to invite a lot of my friends and the most convenient day for them to celebrate is the weekend.
# 
# I was hoping you could help me calculate the party date by the given birthday date, but, as I said before, the date should meet specific requirements:
# 
# It should always be the closes weekend to my birthday.I don't want to celebrate before the birthday.But I'm ok with marking in the day.Input:Date of my birthday.
# 
# Output:Date of the party.
# 
# 
# END_DESC

import datetime

def birthday_party(birthday: datetime.date) -> datetime.date:
    x = birthday.weekday()
    return birthday + datetime.timedelta(days= 5 - x) if x < 5 else birthday

print('Example:')
print(birthday_party(datetime.date(2022, 1, 5)))

assert birthday_party(datetime.date(2022, 1, 5)) == datetime.date(2022, 1, 8)
assert birthday_party(datetime.date(2022, 2, 21)) == datetime.date(2022, 2, 26)
assert birthday_party(datetime.date(2022, 3, 26)) == datetime.date(2022, 3, 26)
assert birthday_party(datetime.date(2022, 4, 17)) == datetime.date(2022, 4, 17)
assert birthday_party(datetime.date(2022, 3, 30)) == datetime.date(2022, 4, 2)

print("The first mission is done! Click 'Check' to earn cool rewards!")