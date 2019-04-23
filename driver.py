#!/usr/bin/env python3

# libraries for calculation and waiting
from __future__ import print_function
import math
import time
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

class driver(object):

    # default conditions: robot is facing right and is at pos 0,0 at the bottom left of the coordinates system.

    # orientation variables
    x_source = 0
    y_source = 0
    a_source = 0


    def __init__(self, arg):

        self.robot = arg

        # array to store past coordinates
        self.log = []

        # variable for pointing status of the robot
        self.pointing = False


    # return angle to turn by for new coordinates
    def calc_angle(self, x, y):
        if (x == 0):
            if (y < 0):
                return -90
            elif (y > 0):
                return 90
            else:
                return 0
        return math.degrees(math.atan2(y, x))


    # return distance to new coordinates
    def calc_hypo(self, x, y):
        return math.sqrt(((x**2)+(y**2)))


    # unpoint the robot
    def unpoint(self):

        if (self.pointing):

            self.robot.point(False)
            self.robot.drive(self.robot.pointer)
            self.robot.turn(self.a_source)
            self.a_source = 0

            self.pointing = False


    # move to new coordinates
    def move(self, x_target, y_target, point=False, logging=True):

        self.unpoint()

        # calculating how much we have to turn and move forward with default conditions

        x_diff = x_target - self.x_source
        y_diff = y_target - self.y_source

        # turning back to default conditions
        eprint("debug robot: ")
        eprint(self.robot.turn)
        eprint("debug a source: ")
        eprint(self.a_source)
        self.robot.turn_deg = self.a_source
        self.a_source = 0

        # angle we have to turn by
        angle = self.calc_angle(x_diff, y_diff)

        # length we have to move by
        hypo = self.calc_hypo(x_diff, y_diff)  

        # set pointer variable for next run
        self.pointing = point

        # account pointer for the length we move forward by
        if (point): hypo -= self.robot.pointer
        
        self.robot.turn(-angle)

        # move forward
        self.robot.drive(hypo)

        # point at the coordinates
        if (point): robot.point(True)

        # set new global coordinates
        self.x_source = x_target
        self.y_source = y_target
        self.a_source += angle

        # log movement
        if (logging):
            mov = [self.x_source, self.y_source]
            self.log.append(mov)


    def retreat(self):

        # unpoint, so the calculation fits again
        self.unpoint()
        self.log.reverse()

        # move back to every coordinate that was visited
        for x in self.log:
            self.move(x[0], x[1], point=False, logging=False)
        
        # revert angle at which the turtle rests
        self.robot.turn(self.a_source)
        self.a_source = 0