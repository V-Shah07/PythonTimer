from PyQt5.QtCore import QTime


class Clock:
    def getTime(self):
        return QTime.currentTime().toString('hh:mm:ss.zzz')[:-1]


class Stopwatch:
    def __init__(self):
        self.total_milliseconds = 0
        self.currently_on = False

    def startTime(self):
        self.currently_on = True

    def stopTime(self):
        self.currently_on = False

    def resetTime(self):
        self.currently_on = False
        self.total_milliseconds = 0

    def getTime(self):
        if self.currently_on:
            self.total_milliseconds += 10
        seconds = (self.total_milliseconds//1000) % 60
        minutes = (self.total_milliseconds//(1000*60)) % 60
        hours = (self.total_milliseconds//(1000*60*60)) % 24
        milliseconds = ((self.total_milliseconds) % 1000)//10
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"
