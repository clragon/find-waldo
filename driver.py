#!/usr/bin/env python3

# libraries for calculation and waiting
import math
import time

class driver(object):

    # default conditions: robot is facing right and is at pos 0,0 at the bottom left of the coordinates system.

    # one unit of the coordinate system in cm
    unit = 4.5

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

        # angle at which to turn to point at a coordinate which is 1 times thepointer away.
        self.point_angle = self.calc_angle(self.robot.point_dis, self.robot.pointer)


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

            self.robot.turn(-point_angle)
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
        self.robot.turn(self.a_source)
        self.a_source = 0

        # angle we have to turn by
        angle = self.calc_angle(x_diff, y_diff)

        # length we have to move by
        hypo = self.calc_hypo(x_diff, y_diff)  

        # debug print for calculated variables
        # print("move: {} | x: {} | y: {} | {} | {} | a: {} | ang: {} | hy: {} | xd: {} | yd: {}".format(len(log), (x_target / unit), (y_target / unit), x_diff < 0, y_diff < 0, a_source, angle, hypo, x_diff, y_diff))

        # set pointer variable for next run
        self.pointing = point

        # account pointer for the length we move forward by
        if (point): hypo -= self.robot.pointer
        
        self.robot.turn(-angle)

        # move forward
        self.robot.drive(hypo)

        # point at the coordinates
        if (point): robot.turn(point_angle)

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