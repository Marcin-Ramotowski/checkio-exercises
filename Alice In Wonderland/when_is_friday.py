#!/usr/bin/env checkio --domain=py run when-is-friday

# Friday is an awesome day. It's the end of the week after which you can just relax and attend to all of the things you've been pushing away. It's really good to know how many days you still have to wait, isn't it?
# 
# Your task is to write a function that will count how many days are left from a certain date to Friday. The argument will be a particular date in a string format looking like this: 'dd.mm.yyyy', where 'dd' - day, 'mm' - month, and 'yyyy' - year.
# For example, if that given day is Thursday, then the answer will be 1. If that day is Monday, the result is 4. And if that day is Friday, the function should return 0.
# 
# 
# 
# Input:Date as a string.
# 
# Output:The amount of days left until Friday.
# 
# Precondition:
# 1 <= year <= 3000
# 
# 
# END_DESC

from datetime import datetime as d

weekday = lambda x: d.strptime(x, '%d.%m.%Y').weekday()
friday = lambda x: 4 - weekday(x) if weekday(x) < 5 else 11 - weekday(x)