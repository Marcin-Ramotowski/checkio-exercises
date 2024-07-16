#!/usr/bin/env checkio --domain=py run power-supply

# You are given the power grid and power-plant's information    (plant-number and supply-range). You should find out which cities blacked out.    A power plant can supply itself and connected cities with power, but the range is    limited.
# 
# 
# 
# Input:Two arguments. The first one is the network, represented as a list of connections.    Each connection is a list of two nodes that are connected. A city or power plant can    be a node. Each city or power plant is a unique string. The second argument is a dict    where keys are power plants and values are the power plant's range.
# 
# Output:A set of strings.         Each string is the name of a blacked out city.
# 
# Precondition:len(set(chain(*networks))) <= 25
# 
# 
# END_DESC

from itertools import chain

def power_supply(network, plants):
    cities = {n for net in network for n in net}
    cities = sorted(cities)
    graph = {}
    for city in cities:
        connections = sorted([n[0] if n[0] != city else n[1] for n in network if city in n])
        graph[city] = connections
    powered = []
    powered.extend(plants.keys())
    for plant, power in plants.items():
        neighbors = [plant]
        for i in range(power):
            neighbors = [graph[city] for city in neighbors]
            neighbors = list(chain.from_iterable(neighbors))
            powered.extend(neighbors)
    return {city for city in cities if city not in powered}