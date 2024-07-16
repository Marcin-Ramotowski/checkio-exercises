#!/usr/bin/env checkio --domain=py run node-crucial

# Citizens of GridLand are sending emails to each other all the time. They send everything - what they just ate, a funny picture, questions or thoughts that are bothering them right now. All the citizens are happy because they have such a wonderful network that keeps them connected.
# 
# The main goal of the Mayor is to control the city's happiness. The city's happiness is a sum of all citizens' happiness. And the happiness of each citizen is equal to the number of citizens (always including oneself) that one can send emails to.
# 
# Because the city is growing, the citizens have decided that the Mayor needs an assistant to focus on the node protection.
# 
# Your mission is to figure out what will be the first nodes to investigate and protect for the new assistant. Remember, you should choose the most important node in the network. If several nodes have the maximal importance, find all of them
# 
# Input:Two arguments: the network structure (as a list of connections between the nodes), users on each node (as dict where keys are the node-names and values are the amounts of users).
# 
# Output:List of the most cruсial nodes.
# 
# 
# END_DESC

def most_crucial(net, users):
    return ['B']

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_crucial([
            ['A', 'B'],
            ['B', 'C']
        ],{
            'A': 10,
            'B': 10,
            'C': 10
        }) == ['B'], 'First'

    assert most_crucial([
            ['A', 'B']
        ],{
            'A': 20,
            'B': 10
        }) == ['A'], 'Second'

    assert most_crucial([
            ['A', 'B'],
            ['A', 'C'],
            ['A', 'D'],
            ['A', 'E']
        ],{
            'A': 0,
            'B': 10,
            'C': 10,
            'D': 10,
            'E': 10
        }) == ['A'], 'Third'

    assert most_crucial([
            ['A', 'B'],
            ['B', 'C'],
            ['C', 'D']
        ],{
            'A': 10,
            'B': 20,
            'C': 10,
            'D': 20
        }) == ['B'], 'Forth'

    print('Nobody expected that, but you did it! It is time to share it!')