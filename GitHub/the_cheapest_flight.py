#!/usr/bin/env checkio --domain=py run the-cheapest-flight

# "We need to fly home as cheaply as possible so that more money is left for gifts. Aunt Lidia asked for different kinds of cheeses, and Vasya wanted a new toy car. I’ve been looking at the schedule for quite a while and I’m starting to think that some planes are flying in vain".
# 
# As the input you get the flight schedule as an array, each element of which is the price of a direct flight between 2 cities (an array of 3 elements - 2 city names as a string, and a flight price).
# 
# Planes fly in both directions and the price in both directions is the same. There is a possibility that there are no direct flights between cities.
# 
# Find the price of the cheapest flight between cities that are given as the 2nd and 3rd arguments.
# 
# Input:3 arguments: the flight schedule as an array of arrays, city of departure and destination city.
# 
# Output:Int. The best price.
# 
# Precondition:Price is always int. The flight schedule contains at least one element. Both cities are in the schedule.
# 
# 
# END_DESC

def bfs(graph, start):
    visited = {}
    queue = [(start,0)]
    while queue:
        node, price = queue.pop(0)
        if node in visited:
            if visited[node] > price:
                visited[node] = price
        if node not in visited:
            visited[node] = price
            neighbours = graph[node]
            for neighbour in neighbours:
                queue.append((neighbour, price + neighbours[neighbour]))
    return visited


def cheapest_flight(schedule,start,end):
    cities = {f for flight in schedule for f in flight if type(f) != int}
    cities = sorted(cities)
    graph = {}
    for city in cities:
        connections = [(f[0],f[2]) if f[0] != city else (f[1],f[2]) for f in schedule if city in f]
        graph[city] = dict(connections)
    ways = bfs(graph, start)
    return ways[end] if end in ways else 0


if __name__ == '__main__':
    print("Example:")
    print(cheapest_flight([['A', 'C', 100],
  ['A', 'B', 20],
  ['B', 'C', 50]],
 'A',
 'C'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert cheapest_flight([['A', 'C', 100],
  ['A', 'B', 20],
  ['B', 'C', 50]],
 'A',
 'C') == 70
    assert cheapest_flight([['A', 'C', 100],
  ['A', 'B', 20],
  ['B', 'C', 50]],
 'C',
 'A') == 70
    assert cheapest_flight([['A', 'C', 40],
  ['A', 'B', 20],
  ['A', 'D', 20],
  ['B', 'C', 50],
  ['D', 'C', 70]],
 'D',
 'C') == 60
    assert cheapest_flight([['A', 'C', 100],
  ['A', 'B', 20],
  ['D', 'F', 900]],
 'A',
 'F') == 0
    assert cheapest_flight([['A', 'B', 10],
  ['A', 'C', 15],
  ['B', 'D', 15],
  ['C', 'D', 10]],
 'A',
 'D') == 25
    print("Coding complete? Click 'Check' to earn cool rewards!")

print(cheapest_flight([["A","B",10],["A","C",20],["B","D",15],["C","D",5],["D","E",5],["E","F",10],["C","F",25]],"A","F"))