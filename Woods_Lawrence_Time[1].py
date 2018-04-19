'''
Lawrence Woods
3/3/2018
Class StopWatch
(Stopwatch) Design a class named StopWatch. The class contains:

The private data fields startTime and endTime with get methods.

A constructor that initializes startTime with the current time.

A method named start() that resets the startTime to the current time.

A method named stop() that sets the endTime to the current time.

A method named getElapsedTime() that returns the elapsed time for the stop watch in milliseconds.

Draw the UML diagram for the class, and then implement the class.

Write a test program that measures the execution time of adding numbers from 1 to 1,000,000.
'''

import time


class Stopwatch:
    # initialize the private fields of Stopwatch

    def __init__(self):
        self.startTime = time.clock()

        self.endTime = None

    # method to get the startTime



    def getStartTime(self):
        return self.startTime

    # method to get the endTime

    def getEndTime(self):
        return self.endTime

    # method to start the stopwatch

    def start(self):
        self.startTime = time.time()

    # method to stop the stopwatch

    def stop(self):
        self.endTime = time.time()

    # method to get the elapsedTime

    def getElapsedTime(self):
        elapsedTime = None;

        if (self.endTime != None):
            elapsedTime = (self.endTime - self.startTime) * 1000

        return elapsedTime


# method to test the class

def main():
    timer = Stopwatch()

    timer.start()

    sum = 0

    for i in range(1, 1000001):
        sum = sum + i

    timer.stop()

    print("Execution time :" + str(timer.getElapsedTime()) + " milliseconds");


# call the main method

main()