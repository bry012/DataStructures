__author__ = 'bryan'
import random

class Baseball:

    def __init__(self, isStrike, speed):
        self.pitchTypes = ["slider", "curve", "fastball", "sinker"]
        self.isStrike = isStrike
        self.speed = speed
        self.pitchType = self.pitchTypes[random.randint(0,len(self.pitchTypes) - 1)]

    def __str__(self):
        return "Ball Stats: \nSpeed: " + str(self.speed) + "\nPitch Type: " + self.pitchType