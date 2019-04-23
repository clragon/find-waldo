#!/usr/bin/env python3

# libraries for calculations
import math

# Import all libraries necessary to run ev3
# from ev3dev.ev3 import *
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM
from ev3dev2.motor import MoveSteering, OUTPUT_B, OUTPUT_C

class robot():

    # create objects for left motor (output B) and right motor (output C)
    mL = LargeMotor('outB'); mL.stop_action = 'hold'
    mR = LargeMotor('outC'); mR.stop_action = 'hold'

    # TODO: implement motor for pointer here

    # default motor speed value
    base_speed = 400

    # default motor ramping up/down value (ms)
    base_ramp=600


    # radius of a wheel (cm)
    radius = 1.5

    # diameter between the two wheels (cm)
    diameter = 14

    
    # pointer length
    pointer = 10

    # pointer distance to the center of the robot
    point_dis = 4


    def __init__(self):

        # calcultaing the circumfence so we can find out 
        # how much degrees we need to turn forward to move 1 cm
        self.circ = 2 * math.pi * self.radius

        # degrees for one cm
        self.one_cm = 1 / (self.circ / 360)

        # circumfence of the turning circle of both wheels
        self.rob_circ = 2 * math.pi * (self.diameter / 2)

        # how much degrees both wheels have to turn to turn the entire robot for 1 degree
        self.turn = 360 / self.circ * ( self.rob_circ / 360)


    # go x cm straight.
    def fahre(self, cm, anfahren=base_ramp, bremsen=base_ramp):
        self.mL.run_to_rel_pos(position_sp=cm * one_cm, speed_sp=self.base_speed, ramp_up_sp=anfahren, ramp_down_sp=bremsen)
        self.mR.run_to_rel_pos(position_sp=cm * one_cm, speed_sp=self.base_speed, ramp_up_sp=anfahren, ramp_down_sp=bremsen)
        self.mR.wait_while('running')
        self.mL.wait_while('running')
            

    # turn left by x degrees
    def drehen(self, degrees):
        self.mL.run_to_rel_pos(position_sp=+degrees * turn, speed_sp=self.base_speed)
        self.mR.run_to_rel_pos(position_sp=-degrees * turn, speed_sp=self.base_speed)
        self.mL.wait_while('running')
        self.mR.wait_while('running')

    # TODO: implement method to lower or rise pointer



