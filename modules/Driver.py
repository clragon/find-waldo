#!/usr/bin/env python3

# library for calculations (turning degrees, etc).
import math
from config import *
# library for remote connection to the robot.
import rpyc


class Driver:
    '''A handler class for an EV3. Connects remotely over RPyC.
    
    Implements basic functions for moving.

    Driving straight, turning, speaking and pointing are supported.
    '''
    base_speed = 0
    base_ramp = 0
    radius = 0
    diameter = 0
    pointer = 0

    def __init__(self, address, base_speed=MOTOR_BASE_SPEED, base_ramp=MOTOR_BASE_RAMPING, wheel_radius=WHEEL_RADIUS,
                 diameter=ROBOT_DISTANCE_WHEEL, pointer=ROBOT_ARM_SIZE):
        # Setup parameters
        self.remote = rpyc.classic.connect(address)
        self.base_speed = base_speed
        self.base_ramp = base_ramp
        self.radius = wheel_radius
        self.diameter = diameter
        self.pointer = pointer

        # instantiate the EV3 dev module on the robot.
        self.ev3 = self.remote.modules['ev3dev.ev3']

        # create motor control objects with the remote EV3 dev module.
        self.mP = self.ev3.MediumMotor('outA'); self.mP.stop_action = 'hold'
        self.mL = self.ev3.LargeMotor('outB'); self.mL.stop_action = 'hold'
        self.mR = self.ev3.LargeMotor('outC'); self.mR.stop_action = 'hold'

        # calculating the circumference (mm) of a wheel.
        self.circ = 2 * math.pi * self.radius

        # calculating how many degrees a wheel has to turn to move one mm.
        self.one_mm = 1 / (self.circ / 360)

        # calculating the circumference of the turning circle of the robot.
        self.rob_circ = 2 * math.pi * (self.diameter / 2)

        # calculating how much degrees both wheels have to turn in order for the robot to turn one degree.
        self.turn_deg = 360 / self.circ * self.rob_circ

    # drive straight for the given amount of mm. Optionally, speed and ramping can ge passed as parameters.
    def drive(self, mm, ramp_up=base_ramp, ramp_dw=base_ramp):
        '''Drive straight for the given amount of mm.

        Parameters:
            mm (int): The amount of milimeters to drive straight for.
            ramp_up (int): amount of miliseconds until full speed.
            ramp_dw (int): amount of miliseconds until full stop.
        '''
        self.drive_adjusted(mm, ramp_up, ramp_dw)

        #self.mL.run_to_rel_pos(position_sp=mm * self.one_mm, speed_sp=self.base_speed, ramp_up_sp=ramp_up, ramp_down_sp=ramp_dw)
        #self.mR.run_to_rel_pos(position_sp=mm * self.one_mm, speed_sp=self.base_speed, ramp_up_sp=ramp_up, ramp_down_sp=ramp_dw)

        #self.mR.wait_while('running')
        #self.mL.wait_while('running')

    def drive_adjusted(self, mm, ramp_up=base_ramp, ramp_dw=base_ramp):
        '''Drive straight for the given amount of mm.

        Parameters:
            mm (int): The amount of milimeters to drive straight for.
            ramp_up (int): amount of miliseconds until full speed.
            ramp_dw (int): amount of miliseconds until full stop.
        '''
        self.mL.run_to_rel_pos(position_sp=mm * self.one_mm, speed_sp=self.base_speed-23, ramp_up_sp=ramp_up, ramp_down_sp=ramp_dw)
        self.mR.run_to_rel_pos(position_sp=mm * self.one_mm, speed_sp=self.base_speed, ramp_up_sp=ramp_up, ramp_down_sp=ramp_dw)

        self.mR.wait_while('running')
        self.mL.wait_while('running')


    # turn the robot to the right by given degrees. Minus degrees can be given to turn to the left.
    def turn(self, degrees):
        '''Turn to the right by the given degrees.
        
        It is possible to pass negative degrees resulting in turning to the left.
        Parameters:
            degrees (int): How many degrees to turn to the right by.
        '''

        arc=(degrees*self.rob_circ/(4*360))*16
        print("Arc: ", arc)
        self.mL.run_to_rel_pos(position_sp=-arc, speed_sp=self.base_speed)
        self.mR.run_to_rel_pos(position_sp=+arc, speed_sp=self.base_speed)
        self.mL.wait_while('running')
        self.mR.wait_while('running')

    # let the robot speak the given text.
    def speak(self, text):
        if ENABLE_SOUND:
            self.ev3.Sound.speak(text, espeak_opts='-a 200 -s 130').wait()

    def beep(self):
        if ENABLE_SOUND:
            self.ev3.Sound.beep()


    # raise or lower the pointer of the robot.
    def point(self):
        '''Raise or lower the pointer of the robot.
        
        Parameters:
            do_point (bool): True means lowered state, False means raised state.
        '''
        self.mP.run_to_abs_pos(position_sp=0, speed_sp=self.base_speed/2)
        self.mP.wait_while('running')

    def unpoint(self):
        self.mP.run_to_rel_pos(position_sp=-50, speed_sp=self.base_speed/2)




