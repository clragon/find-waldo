#!/usr/bin/env python3

# libraries for calculations
import math
import time

# library for remote connection
import rpyc

# Import all libraries necessary to run ev3
# obsolete. we import this remotely now.
# TODO: remove line
# from ev3dev.ev3 import Sound, LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C

class Robot(object):    

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


    def __init__(self, adress):

        remote = rpyc.classic.connect(adress) # TODO: get EV3 hostname / IP adress for this field

        # remote import of the ev3dev library
        self.ev3 = remote.modules['ev3dev.ev3']

        # create objects for left motor (output B) and right motor (output C) as well as a pointer motor (output A)
        # create these objects over RPyC
        self.mP = self.ev3.MediumMotor('outA'); self.mP.stop_action = 'hold'
        self.mL = self.ev3.LargeMotor('outB'); self.mL.stop_action = 'hold'
        self.mR = self.ev3.LargeMotor('outC'); self.mR.stop_action = 'hold'

        # no need to do calculations remotely (?).

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


    # robot text to speak; now remotely.
    def speak(self, text):
        self.ev3.Sound.speak(text)


    # point for x ms
    def point(self, do_point):
        if (do_point):
            self.mP.run_to_abs_pos(position_sp=90)
            self.mP.wait_while('running')
        else:
            self.mP.run_to_abs_pos(position_sp=0)
            self.mP.wait_while('running')




