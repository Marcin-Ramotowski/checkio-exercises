#!/usr/bin/env checkio --domain=py run find-friends

# Sophia's drones are not soulless and stupid drones; they can make and have friends.    In fact, they already are working for the their own social network just for drones!    Sophia has received the data about the connections between drones and she wants to know more about relations between them.
# 
# We have an array of straight connections between drones.    Each connection is represented as a string with two names of friends separated by hyphen.    For example: "dr101-mr99" means what thedr101andmr99are friends.    Your should write a function that allow determine more complex connection between drones.    You are given two names also. Try to determine if they are related through common bonds by any depth.    For example: if two drones have a common friends or friends who have common friends and so on.
# 
# 
# 
# Let's look at examples:
# scout2andscout3have the common friendscout1so they are related.superandscout2are related throughsscout,scout4andscout1.    Butdr101andsscoutare not related.
# 
# Input:Three arguments: Information about friends as a tuple of strings; first name as a string;    second name as a string.
# 
# Output:Are these drones related or not as a boolean.
# 
# Precondition:len(network) ≤ 45
# if"name1-name2"innetwork, then"name2-name1"not innetwork
# 3 ≤ len(drone_name) ≤ 6
# first_nameandsecond_nameinnetwork.
# 
# 
# END_DESC

def check_connection(network, first, second):
    future = [first]
    l = len(future)
    i = 0
    while i < l:
        checking = future[i]
        for relation in network:
            if relation.find(checking) != -1:
                checked = True
                drones = relation.split("-")
                for drone in drones:
                    if drone != checking:
                        if drone not in future:
                            future.append(drone)
                            l += 1
                        if drone == second:
                            return True
        i += 1
    return False


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."