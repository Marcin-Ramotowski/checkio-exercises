#!/usr/bin/env checkio --domain=py run network-attack

# Nicola regularly inspects the local networks for security issues.    He uses a smart and aggressive program which takes control of computers on the network.    This program attacks all connected computers simultaneously,    then uses the captured computers for further attacks.    Nicola started the virus program in the first computer and took note of the time    it took to completely capture the network. We can help him improve his process by modeling and improving his inspections.
# 
# We are given information about the connections in the network and the security level for each computer.    Security level is the time (in minutes) that is required for the virus to capture a machine.    Capture time is not related to the number of infected computers attacking the machine.    Infection start from the 0th computer (which is already infected).    Connections in the network are undirected. Security levels are not equal to zero (except infected).
# 
# Information about a network is represented as a matrix NxN size, whereNis a number of computers.    Ifith computer connected withjth computer, then matrix[i][j] == matrix[j][i] == 1, else 0.    Security levels are placed in the main matrix diagonal, so matrix[i][i] is the security level for theith computer.
# 
# 
# 
# You should calculate how much time is required to capture the whole network in minutes.
# 
# Input:Network information as a list of lists with integers.
# 
# Output:The total time of taken to capture the network as an integer.
# 
# Precondition:
# 3 ≤ len(matrix) ≤ 10
# matrix[0][0] == 0
# all(len(row) == len(matrix[0]) for row in matrix)
# all(matrix[i][j] == matrix[j][i] for i in range(len(matrix)) for j in range(len(matrix)))
# all(0 < matrix[i][i] < 10 for i in range(1, len(matrix)))
# all(0 ≤ matrix[i][j] ≤ 1 for i in range(len(matrix)) for j in range(len(matrix)) if i != j)
# 
# 
# 
# END_DESC

class Computer:
    def __init__(self, number, defense) -> None:
        self.number = number
        self.defense = defense

    @property
    def is_captured(self):
        """The is_captured property."""
        return self.defense <= 0

    def __repr__(self) -> str:
        return f"Number: {self.number}, Defense: {self.defense}"


def capture(matrix):
    N = len(matrix)
    powers = [matrix[i][i] for i in range(N)]
    computers = [Computer(i, powers[i]) for i in range(N)]
    infected = [computers[0]]
    defenders = [computers[1:]]
    time = 0

    while defenders:
        attacked = []
        for attacker in infected:
            i = attacker.number
            for j in range(N):
                if j != i and matrix[j][i]:
                    if computers[j] not in attacked and computers[j] not in infected:
                        attacked.append(computers[j])

        powers = [defender.defense for defender in attacked]
        attack = min(powers)
        time += attack
        for defender in attacked:
            defender.defense -= attack
        fallen = [computer for computer in attacked if computer.is_captured]
        infected += fallen
        defenders = [computer for computer in computers if not(
            computer.is_captured)]
    return time