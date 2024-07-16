#!/usr/bin/env checkio --domain=py run unique-email-addresses

# Every valid email consists of name and domain, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'. For example, in "alex@checkio.org", "alex" is the name, and "checkio.org" is the domain.
# 
# If you add periods '.' between some characters in the name part of an email address, mail sent there will be delivered to the same address without dots in the name. Note that this rule does not apply to domain names. For example, "a.lyabah@checkio.org" and "alyabah@checkio.org" delivered to the same email address.
# 
# If you add a plus '+' in the  name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. Note that this rule does not apply to domain names. For example, "alex+home@checkio.org" will be delivered to "alex@checkio.org".
# 
# It is possible to use both of these rules at the same time.
# 
# Given an array of strings - valid emails, return the number of unique emails.
# 
# Input:Array of strings(valid emails)
# 
# Output:Int.
# 
# 
# END_DESC

def unique_emails(emails: list[str]) -> int:
    scores = []
    for email in emails:
        name, domain = email.split('@')
        if '+' in name:
            name = name[:name.index('+')]
        if '.' in name:
            name = name.replace('.', '')
        new = (name + '@' + domain).lower()
        scores.append(new)
    scores = set(scores)
    return len(scores)


print("Example:")
print(unique_emails(["alex@checkio.org", "mike@google.com", "lili@apple.com"]))

assert unique_emails(["alex@checkio.org", "mike@google.com", "lili@apple.com"]) == 3
assert (
    unique_emails(
        ["mi.ke@google.com", "alex@checkio.org", "mike@google.com", "lili@apple.com"]
    )
    == 3
)
assert (
    unique_emails(
        [
            "alex+home@checkio.org",
            "lili+work@apple.com",
            "alex@checkio.org",
            "lili@apple.com",
        ]
    )
    == 2
)
assert (
    unique_emails(
        [
            "l.ili+work@apple.com",
            "a.lex@checkio.org",
            "alex+home@checkio.org",
            "lili+work@apple.com",
            "alex@checkio.org",
            "lili@apple.com",
        ]
    )
    == 2
)
assert unique_emails(["Alex@checkIO.org", "alex@checkio.org", "alex@check.io.org"]) == 2
assert unique_emails([]) == 0

print("The first mission is done! Click 'Check' to earn cool rewards!")