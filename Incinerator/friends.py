#!/usr/bin/env checkio --domain=py run friends

# pre.example {        border: 1px solid #aaa;        border-radius: 3px;        background: #eee;        margin-left: 20px;        padding: 5px;        overflow: auto;    }    p.indent {        margin-left: 20px;    }For the mission"How to find friends", it’s nice to have access to a specially made data structure. In this mission we will    realize a data structure which we will use to store and work with a friend network.
# 
# The class "Friends" should contains names and the connections between them. Names are    represented as strings and are case sensitive. Connections are undirected, so if "sophia" is    connected with "nikola", then it's also correct in reverse.
# 
# classFriends(connections)
# 
# Returns a new Friends instance."connections"is an iterable of sets with two elements    in each. Each connection contains two names as strings. Connections can be repeated in the    initial data, but inside it's stored once. Each connection has only two states - existing or not.
# 
# 
# >>> Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
# >>> Friends([{"1", "2"}, {"3", "1"}])
# 
# add(connection)
# 
# Add a connection in the instance."connection"is a set of two names (strings).    Returns True if this connection is new.    Returns False if this connection exists already.
# 
# 
# >>> f = Friends([{"1", "2"}, {"3", "1"}])
# >>> f.add({"1", "3"})
# False
# >>> f.add({"4", "5"})
# True
# 
# remove(connection)
# 
# Remove a connection from the instance."connection"is a set of two names (strings).    Returns True if this connection exists.    Returns False if this connection is not in the instance.
# 
# 
# >>> f = Friends([{"1", "2"}, {"3", "1"}])
# >>> f.remove({"1", "3"})
# True
# >>> f.remove({"4", "5"})
# False
# 
# names()
# 
# Returns a set of names. The set contains only names which are connected with somebody.
# 
# 
# >>> f = Friends(({"a", "b"}, {"b", "c"}, {"c", "d"}))
# >>> f.names()
# {"a", "b", "c", "d"}
# >>> f.remove({"d", "c"})
# True
# >>> f.names()
# {"a", "b", "c"}
# 
# connected(name)
# 
# Returns a set of names which is connected with the given"name".    If "name" does not exist in the instance, then return an empty set.
# 
# 
# >>> f = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}))
# >>> f.connected("a")
# {"b", "c"}
# >>> f.connected("d")
# set()
# >>> f.remove({"c", "a"})
# True
# >>> f.connected("c")
# {"b"}
# >>> f.remove({"c", "b"})
# True
# >>> f.connected("c")
# set()
# 
# In this mission all data will be correct and you don't need to implement value checking.
# 
# Input:Statements and expression with the Friends class.
# 
# Output:The behaviour as described.
# 
# Precondition:All data is correct.
# 
# 
# END_DESC

from itertools import chain

class Friends:
    def __init__(self,connections) -> None:
        self.connections = []
        for connect in connections:
            if connect not in self.connections:
                self.connections.append(connect)
    def add(self,connection):
        score = True if connection not in self.connections else False
        if score:
            self.connections.append(connection)
        return score
    def remove(self,connection):
        state = True if connection in self.connections else False
        if state:
            self.connections.remove(connection)
        return state
    def names(self):
        return set(chain.from_iterable(self.connections))
    def connected(self, name):
        friends = set()
        for connect in self.connections:
            if name in connect:
                a, b = connect
                friend = a if a != name else b
                friends.add(friend)
        return friends