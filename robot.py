#!/usr/bin/env python3

# libraries for calculations
import math
import time

# Import all libraries necessary to run ev3
from ev3dev.ev3 import Sound, LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C

class robot():

    # create objects for left motor (output B) and right motor (output C) as well as a pointer motor (output A)
    mP = MediumMotor('outA'); mP.stop_action = 'hold'
    mL = LargeMotor('outB'); mL.stop_action = 'hold'
    mR = LargeMotor('outC'); mR.stop_action = 'hold'
    

    # default motor speed value
    base_speed = 400

    # default motor ramping up/down value (ms)
    base_ramp=600


    # radius of a wheel (mm)
    radius = 15

    # diameter between the two wheels (mm)
    diameter = 140

    
    # pointer length (mm)
    pointer = 160


    def __init__(self):

        # calcultaing the circumfence (mm)
        self.circ = 2 * math.pi * self.radius

        # degrees for one mm
        self.one_mm = 1 / (self.circ / 360)

        # circumfence of the turning circle of both wheels
        self.rob_circ = 2 * math.pi * (self.diameter / 2)

        # how much degrees both wheels have to turn to turn the entire robot for 1 degree
        self.turn_deg = 360 / self.circ * ( self.rob_circ / 360)


    # go x mm straight.
    def drive(self, mm, anfahren=base_ramp, bremsen=base_ramp):
        self.mL.run_to_rel_pos(position_sp=mm * self.one_mm, speed_sp=self.base_speed, ramp_up_sp=anfahren, ramp_down_sp=bremsen)
        self.mR.run_to_rel_pos(position_sp=mm * self.one_mm, speed_sp=self.base_speed, ramp_up_sp=anfahren, ramp_down_sp=bremsen)
        self.mR.wait_while('running')
        self.mL.wait_while('running')
            

    # turn right by x degrees
    def turn(self, degrees):
        self.mL.run_to_rel_pos(position_sp=-degrees * self.turn_deg, speed_sp=self.base_speed)
        self.mR.run_to_rel_pos(position_sp=+degrees * self.turn_deg, speed_sp=self.base_speed)
        self.mL.wait_while('running')
        self.mR.wait_while('running')


    # robot text to speak
    def speak(self, text):
        Sound.speak(text)


    # point for x ms
    def point(self, do_point):
        if (do_point):
            self.mP.run_to_abs_pos(position_sp=90)
        else:
            self.mP.run_to_rel_pos(position_sp=0)




