#!/usr/bin/env python3
import os


# Import all libraries necessary to run ev3
from ev3dev.ev3 import *
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM
from ev3dev2.motor import MoveSteering, OUTPUT_B, OUTPUT_C


# libraries for calculation and wait time
import math
import time


# create objects for left motor (output B) and right motor (output C)
mL = LargeMotor('outB'); mL.stop_action = 'hold'
mR = LargeMotor('outC'); mR.stop_action = 'hold'


# default speed value
base_speed = 400

# default ramping value
base_ramp=600

# radius of a wheel
radius = 1.5

# calcultaing the circumfence so we can find out 
# how much degrees we need to turn forward to move 1 cm
circ = 2 * math.pi * radius
# degrees for one cm
one_cm = 1 / (circ / 360)

# diameter between the two wheels
diameter = 14

# circumfence of the turning circle of both wheels
rob_circ = 2 * math.pi * (diameter / 2)
# how much degrees both wheels have to turn to turn the entire robot for 1 degree
turn = 360 / circ * ( rob_circ / 360)

# one unit of the coordinate system in cm
unit = 4.5

# gobal orientation variables
x_source = 0
y_source = 0
a_source = 0

# pointer calculations

# pointer length
pointer = 10
# pointer distance to mid point
point_dis = 4
point_angle = calc_angle(point_dis, pointer)
pointing = False

# array to store past coordinates
log = []


# go x cm straight.
def straight(cm, speed=base_speed, wait=True):
    mL.run_to_rel_pos(position_sp=cm * one_cm, speed_sp=speed, ramp_up_sp=base_ramp, ramp_down_sp=base_ramp)
    mR.run_to_rel_pos(position_sp=cm * one_cm, speed_sp=speed, ramp_up_sp=base_ramp, ramp_down_sp=base_ramp)
    if (wait):
        mR.wait_while('running')
        mL.wait_while('running')


# turn right by x degrees
def right(degrees, speed=base_speed, wait=True):
    mL.run_to_rel_pos(position_sp= -degrees * turn, speed_sp = base_speed)
    mR.run_to_rel_pos(position_sp= +degrees * turn, speed_sp = base_speed)
    if (wait):
        mL.wait_while('running')
        mR.wait_while('running')


# turn left by x degrees
def left(degrees, speed=base_speed, wait=True):
    mL.run_to_rel_pos(position_sp= +degrees * turn, speed_sp = base_speed)
    mR.run_to_rel_pos(position_sp= -degrees * turn, speed_sp = base_speed)
    if (wait):
        mL.wait_while('running')
        mR.wait_while('running')


# return angle to turn by for new coordinates
def calc_angle(x, y):
    if (x == 0):
        if (y < 0):
            return -90
        elif (y > 0):
            return 90
        else:
            return 0
    return math.degrees(math.atan2(y, x))


# return distance to new coordinates
def calc_hypo(x, y):
    return math.sqrt(((x**2)+(y**2)))


# unpoint the robot
def unpoint():

    global pointing
    global pointer
    global a_source

    if (pointing):

        left(point_angle)
        forward(pointer)
        right(a_source)
        a_source = 0

        pointing = False


# move to new coordinates
def move(x_target, y_target, point=False, logging=True):
    
    global pointing
    global pointer
    global point_angle
    global x_source
    global y_source
    global a_source
    global log

    unpoint()

    # calculating how much we have to turn and move forward with default conditions

    x_diff = x_target - x_source
    y_diff = y_target - y_source

    # turning back to default conditions
    right(a_source)
    a_source = 0

    # angle we have to turn by
    angle = calc_angle(x_diff, y_diff)

    # length we have to move by
    hypo = calc_hypo(x_diff, y_diff)  

    # debug print for calculated variables
    print("move: {} | x: {} | y: {} | {} | {} | a: {} | ang: {} | hy: {} | xd: {} | yd: {}".format(len(log), (x_target / unit), (y_target / unit), x_diff < 0, y_diff < 0, a_source, angle, hypo, x_diff, y_diff))

    # set pointer variable for next run
    pointing = point

    # account pointer for the length we move forward by
    if (point): hypo -= pointer
    
    left(angle)

    # move forward
    forward(hypo)

    # point at the coordinates
    if (point): right(point_angle)

    # set new global coordinates
    x_source = x_target
    y_source = y_target
    a_source += angle

    # log movement
    if (logging):
        mov = [x_source, y_source]
        log.append(mov)

    
def retreat():
    
    global a_source

    # unpoint, so the calculation fits again
    unpoint()
    log.reverse()

    # move back to every coordinate that was visited
    for x in log:
        move(x[0], x[1], point=False, logging=False)
    
    # revert angle at which the turtle rests
    turtle.right(a_source)
    a_source = 0


def main():

    # starting at 0,0
    log.append([0, 0])
    # move to random coordinates
    # should actually get coordinates from AI here
    if(True):
        for x in range(0, 10): move(int(randint(-4, 4)) * unit, int(randint(-4, 4)) * unit)
    # go back to starting point
    retreat()



if __name__ == '__main__':
    main()