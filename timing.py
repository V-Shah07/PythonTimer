from this import d
from utils import *

class Clock:
    def getTime():
        return QTime.currentTime().toString('hh:mm:ss.zzz')[:-1]



#----------------------------------------------------------------

class Stopwatch:
    def __init__(self):
        self.totalMilliseconds = 0
        self.currentlyOn = False
    def startTime(self):
        self.currentlyOn = True
    def stopTime(self):
        self.currentlyOn = False
    def resetTime(self):
        self.currentlyOn = False
        self.totalMilliseconds = 0
    def getTime(self):
        if self.currentlyOn:
            self.totalMilliseconds += 10
        seconds = (self.totalMilliseconds//1000)%60
        minutes = (self.totalMilliseconds//(1000*60))%60
        hours = (self.totalMilliseconds//(1000*60*60))%24
        milliseconds = ((self.totalMilliseconds)%1000)//10
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"