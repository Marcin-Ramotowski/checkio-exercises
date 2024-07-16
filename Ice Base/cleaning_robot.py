#!/usr/bin/env checkio --domain=py run cleaning-robot

# Dr. Asimov, a robotics researcher, loves to research, but hates houseworks and his house were really dirty. So, he has developed a cleaning robot.
# 
# As shown in the following figure, his house has 9 rooms, where each room is identified by a letter of the alphabet:
# 
# 
# 
# The robot operates as follows:
# 
# if the battery runs down, the robot stops;if not so, the robot chooses a direction from four cardinal points with equal probability, and moves to the room in that direction. Then, the robot cleans the room and consumes 1 point of the battery;However, if there is no room in that direction, the robot does not move and remains in the same room. In addition, there is a junk room in the house where the robot can not enter, and the robot also remains when it tries to enter the junk room. The robot also consumes 1 point of the battery when it remains in the same place.A battery charger for the robot is in a room. It would be convenient for Dr. Asimov if the robot stops at the battery room when its battery runs down. Your task is to write a program which computes the probability of the robot stopping at the battery room.
# 
# You are given battery capacitycapandstart, bat, junkrespectively represent the room where the robot is initially, the battery room, and the junk room.
# 
# Input:One integer (int) and three strings (str).
# 
# Output:Float (float).
# 
# Examples:
# 
# assert cleaning_robot(1, "E", "A", "C") == 0.0
# assert cleaning_robot(1, "E", "B", "C") == 0.25
# assert cleaning_robot(2, "E", "A", "B") == 0.0625
# This mission was taken fromAIZU ONLINE JUDGE
# 
# 
# END_DESC

def cleaning_robot(cap: int, start: str, bat: str, junk: str) -> float:
    # your code here
    return 0


print("Example:")
print(cleaning_robot(1, "E", "A", "C"))

# These "asserts" are used for self-checking
assert cleaning_robot(1, "E", "A", "C") == 0.0
assert cleaning_robot(1, "E", "B", "C") == 0.25
assert cleaning_robot(2, "E", "A", "B") == 0.0625

print("The mission is done! Click 'Check Solution' to earn rewards!")