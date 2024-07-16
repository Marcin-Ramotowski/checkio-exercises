#!/usr/bin/env checkio --domain=py run landing-site

# In this mission the size of the hexagonal grid is 12x9 ('A1' to 'L9').
# 
# It’s characteristics:it’s flat-topped;the alphabet letters represent columns and numbers represent rows;the even columns are being pushed down.You are given a set of obstacle hexes on the Moon as an input value.You have to return a set of all the candidate landing sites.
# 
# The conditions for the  landing site hex:the hex isn't an obstacle hex;there’re no obstacle hexes in equidistant ( 1 or more ) hexes;the above radius is the longest.NOTE:The outside of the hexagonal grid is always considered as an obstacle hex.If there aren’t any  landing sites, return an empty set.Input:The obstacles on the Moon (a set of strings).
# 
# Output:A set of all the candidate landing sites (a set of strings).
# 
# Precondition:
# 
# all(re.fullmatch('[A-L][1-9]', i) for i in input)How it is used:For finding the needed area.
# 
# 
# END_DESC

from typing import Set

def landing_site(obstacles: Set[str]) -> Set[str]:
    return set()


if __name__ == '__main__':
    assert landing_site({'E5', 'E7', 'F4', 'F6', 'G4', 'G6', 'H3', 'H5'}) == {'C3', 'J7'}, 'crevasse'
    assert landing_site({'A4', 'C2', 'C6', 'C9', 'D4', 'D7', 'F1', 'F5',
                         'F8', 'G4', 'H7', 'I2', 'I5', 'I9', 'K3', 'K8', 'L5'}) == {'B7', 'E3', 'J6'}, 'stones'
    assert landing_site({'D3', 'D4', 'D5', 'D6', 'E3', 'E7', 'F2', 'F7', 'G2',
                         'G8', 'H2', 'H7', 'I3', 'I7', 'J3', 'J4', 'J5', 'J6'}) == {'G5'}, 'crater'
    assert landing_site(set()) == {'E5', 'F5', 'G5', 'H5'}, 'plane'
    assert landing_site({chr(c+65)+str(r+1) for c in range(12) for r in range(9)}) == set(), 'wasteland'

    print('The local tests are done. Click on "Check" for more real tests.')