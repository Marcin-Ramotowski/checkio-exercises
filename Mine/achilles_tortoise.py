#!/usr/bin/env checkio --domain=py run achilles-tortoise

# p.quote-source {        float: right;        font-size: 10px;    }In a race, the quickest runner can never overtake the slowest,        since the pursuer must first reach the point whence the pursued started,        so that the slower must always hold a lead.
# 
# – as recounted by Aristotle, Physics VI:9, 239b15
# 
# "Achilles and the tortoise" is one of the famousZeno's paradoxes.    Nikola wants to check the validity of the paradox and constructed two robots for this purpose:    Achilleborg (A1 -- fast agile prototype) and Tortoimenator (T2 -- heavy slow cyborg).
# 
# A1 is faster than T2, so it has aXseconds head start on A1.    ForXseconds T2 will move att2_speed*Xmetres.    So A1 must first reach the point whence T2 already reached.    But T2 is moving and next step for A1 is to reach the next point and so on toinfinity.    The paradox is correct in theory,    but in practice A1 easily outruns T2. Hm... maybe we can calculate when A1 will catch up to T2.
# 
# 
# 
# You are given A1 and T2’s speed in m/s as well as the length of the advantage T2 has in seconds.    Try to count the time when from when A1 come abreast with T2 (count from T2 start).    The result should be given in seconds with precious ±10-8.
# 
# Input:Three arguments. Speeds of A1 and T2 and advantage as integers.
# 
# Output:The time when A1 catch up T2 (count from T2 start) as an integer or float.
# 
# Precondition:
# t2_speed < a1_speed < 343
# 0 < advantage ≤ 60
# 
# 
# END_DESC

chase = lambda A1, T2, a: T2* a/(A1-T2) + a
# the result to the right of the ":" character is the zero point of Tutle's advantage function: s =  T2*a / (A-T) + a