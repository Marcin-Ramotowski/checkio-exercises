#!/usr/bin/env checkio --domain=py run voice-tv-control

# The technologies are rapidly evolving - only 50 years ago a simple black-and-white TV was a luxury! And now even a cool big color TV with remote control is a common thing. Let's try to improve our TV and add the voice control to it! To begin with, we’ll write the simple prototype in Python. It’ll use the following commands:
# 
# first_channel()- turns on the first channel from the list.
# last_channel()- turns on the last channel from the list.
# turn_channel(N)- turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
# next_channel()- turns on the next channel. If the current channel is the last one, turns on the first channel.
# previous_channel()- turns on the previous channel. If the current channel is the first one, turns on the last channel.
# current_channel()- returns the name of the current channel.
# is_exist(N/'name')- gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name' exists in the list, or "No" - in the other case.
# 
# The default channel turned on before all commands is №1.
# Your task is to create the VoiceCommand class and methods described above.
# In this mission you could use theIteratordesign pattern.
# 
# Example:
# CHANNELS = ["BBC", "Discovery", "TV1000"]
# 
# controller = VoiceCommand(CHANNELS)
# 
# controller.first_channel() == "BBC"
# controller.last_channel() == "TV1000"
# controller.turn_channel(1) == "BBC"
# controller.next_channel() == "Discovery"
# controller.previous_channel() == "BBC"
# controller.current_channel() == "BBC"
# controller.is_exist(4) == "No"
# controller.is_exist("BBC") == "Yes"
# 
# 
# 
# Input:The voice commands.
# 
# Output:The channel name or result of the is_exist method.
# 
# Precondition:All commands and channel names are correct.
# 
# 
# END_DESC

class VoiceCommand:
    def __init__(self, channels: list) -> None:
        self.channels = channels
        self.channel = self.channels[0]
    
    def first_channel(self):
        self.channel = self.channels[0]
        return self.channel
    
    def last_channel(self):
        self.channel = self.channels[-1]
        return self.channel
    
    def turn_channel(self, N):
        self.channel = self.channels[N-1]
        return self.channel
    
    def next_channel(self):
        i = self.channels.index(self.channel)
        if i + 1 > len(self.channels) - 1:
            i = -1
        self.channel = self.channels[i+1]
        return self.channel
    
    def previous_channel(self):
        i = self.channels.index(self.channel)
        self.channel = self.channels[i-1]
        return self.channel
    
    def current_channel(self):
        return self.channel
    
    def is_exist(self, arg):
        N, name = None, None
        if type(arg) == str:
            name = arg
        else:
            N = arg
        if N != None:
            return 'Yes' if 0 < N <= len(self.channels) else "No"
        if name != None:
            return 'Yes' if name in self.channels else "No"