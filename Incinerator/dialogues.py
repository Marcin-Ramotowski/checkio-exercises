#!/usr/bin/env checkio --domain=py run dialogues

# The modern world is filled with means of communication - the social networks, messengers, phone calls, SMS etc.But sometimes in every communication channel a flaw can be detected and in the moments like that you think to yourself: "I should create my own messenger which won’t have problems like this one".
# In this mission you’ll get your chance.
# Your task is to create a Chat class which could help a Human(name) and Robot(serial_number) to make a conversation. This class should have a few methods:
# connect_human()- connects human to the chat.
# connect_robot()- connects robot to the chat.
# show_human_dialogue()- shows the dialog as the human sees it - as simple text.
# show_robot_dialogue()- shows the dialog as the robot perceives it - as the set of ones and zeroes. To simplify the task, just replace every vowel ('aeiouAEIOU') with "0", and the rest symbols (consonants, white spaces and special signs like ",", "!", etc.) with "1".
# Dialog for the human should be displayed like this:
# (human name) said: message text
# (robot serial number): message text
# For the robot:
# (human name) said: 11100100011
# (robot serial number) said: 100011100101
# Interlocutors should have asend()method for sending messages to the dialog.
# In this mission you could use theMediatordesign pattern.
# 
# Example:
# chat = Chat()
# karl = Human("Karl")
# bot = Robot("R2D2")
# chat.connect_human(karl)
# chat.connect_robot(bot)
# karl.send("Hi! What's new?")
# bot.send("Hello, human. Could we speak later about it?")
# chat.show_human_dialogue() == """Karl said: Hi! What's new?
# R2D2 said: Hello, human. Could we speak later about it?"""
# chat.show_robot_dialogue() == """Karl said: 101111011111011
# R2D2 said: 10110111010111100111101110011101011010011011"""
# 
# 
# 
# Input:Interlocutors and the text of messages.
# 
# Output:A dialog (the multiline string).
# 
# Precondition:2 interlocutors.
# 
# 
# END_DESC

class Chat:
    def __init__(self) -> None:
        self.humanMessages = []
        self.robotMessages = []
        self.vowels = 'aeiouAEIOU'
    
    def notify(self, sender: object, message: str) -> None:
        humanMessage = f"{sender.name} said: {message}"
        self.humanMessages.append(humanMessage)
        robotMessage = f"{sender.name} said: "
        for char in message:
            if char in self.vowels:
                robotMessage += '0'
            else:
                robotMessage += '1'
        self.robotMessages.append(robotMessage)

    def connect_human(self,human):
        human.connected = True
        human._mediator = self

    def connect_robot(self,robot):
        robot.connected = True
        robot._mediator = self

    def show_human_dialogue(self):
        return '\n'.join(self.humanMessages)

    def show_robot_dialogue(self):
        return '\n'.join(self.robotMessages)

class Interlocutor:
    def __init__(self, name, mediator: Chat = None) -> None:
        self.name = name
        self._mediator = mediator
        self.connected = False
        
    @property
    def mediator(self) -> Chat:
        return self._mediator

    @mediator.setter
    def mediator(self, name, mediator: Chat) -> None:
        self.name = name
        self._mediator = mediator

class Human(Interlocutor):
    def send(self,message) -> None:
        if self.connected:
            self.mediator.notify(self,message)

class Robot(Interlocutor):
    def send(self,message) -> None:
        if self.connected:
            self.mediator.notify(self,message)