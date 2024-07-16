#!/usr/bin/env checkio --domain=py run power-plants

# This mission is another version of the”Power Supply”mission     originated fromoduvan's idea.
# You have to properly place the given power plants and supply power to all the cities.
# 
# The intercity network and the range of each power plant are given as input values.A power plant can provide power to the city where it’s been placed and within its range.You have to return a dictionary, where the key is the city in which you’ll place the power plant and the value is its range.
# 
# NOTE:
# 
# You will always be given enough or more power-plants.So it isn't always necessary to return all power-plant placements.
# 
# Input:The intercity network represented as a set of connections, where each connection is a tuple of two nodes connected with each other.The range of each power plant, represented as a list of integers.
# 
# Output:A dictionary of placements, where each key is the city in which you’ll place the power plant and each value is the corresponding range.
# 
# Precondition:3 ≤ number of cities ≤ 501 ≤ number of power-plantsrange of power-plant ≥ 0
# 
# 
# 
# 
# END_DESC

from typing import Set, Tuple, List, Dict
from itertools import chain

def power_plants(network: Set[Tuple[str, str]], powers: List[int], isRepeated=False) -> Dict[str, int]:
    graf = {}
    cities = {n for net in network for n in net}
    cities = sorted(cities)
    for city in cities:
        connections = sorted([n[0] if n[0] != city else n[1] for n in network if city in n])
        graf[city] = connections
    edges = [city for city in cities if len(graf[city]) == 1]
    samotni = cities
    wykaz = {}

    for power in powers:
        if power == 0:
            wykaz.update({samotni[0]:0})
            samotni.pop(0)
            continue
        slownik = {}
        for start in cities:
            odwiedzeni = [start]
            sasiedzi = [start]
            for i in range(power):
                    sasiedzi = [graf[city] for city in sasiedzi]
                    sasiedzi = list(chain.from_iterable(sasiedzi))
                    sasiedzi = [city for city in sasiedzi if city in samotni]
                    odwiedzeni.extend(sasiedzi)
            odwiedzeni = set(odwiedzeni)
            slownik[start] = (len(odwiedzeni),odwiedzeni)
        Max = max(slownik.items(), key=lambda x:x[1])
        maxNumber = Max[1][0]
        candidates = [city for city in slownik.items() if city[1][0] == maxNumber]
        
        if len(candidates) > 1 and len(edges) > 0:
            tcandidates = [candidate for candidate in candidates for edge in edges if edge in candidate[1][1]]
            candidates = []
            for candidate in tcandidates:
                if candidate in candidates:
                    continue
                for edge in edges:
                    if edge in candidate[1][1]:
                        candidates.append(candidate)
                        break
            protocole = {}
            for index in range(len(candidates)):
                candidate = candidates[index]
                j = 0
                for edge in edges:
                    if edge in candidate[1][1]:
                        j += 1
                protocole[index] = j
            index = max(protocole.items())
            Max = candidates[index[0]]
            
        wykaz.update({Max[0][0]:power})
        odwiedzeni = Max[1][1]
        samotni = [city for city in samotni if city not in odwiedzeni]
        if len(samotni) == 0:
            break
    return wykaz
    


if __name__ == '__main__':
    assert power_plants({('A', 'B'), ('B', 'C')}, [1]) == {'B': 1}
    assert power_plants({('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E')}, [2]) == {'C': 2}
    assert power_plants({('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F')}, [1, 1]) == {'B': 1, 'E': 1}
    assert power_plants({('A', 'B'), ('B', 'C'), ('A', 'D'), ('B', 'E')}, [1, 0]) == {'B': 1, 'D': 0}

    print('The local tests are done. Click on "Check" for more real tests.')