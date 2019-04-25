#!/usr/bin/env python3

# library for calculations (turning degrees, etc).
import math

# library for remote connection to the robot.
import rpyc

class Robot(object):
    '''A handler class for an EV3. Connects remotely over RPyC.
    
    Implements basic functions for moving.

    Driving straight, turning, speaking and pointing are supported.
    '''

    # default motor speed value (tc/s).
    base_speed = 400

    # default motor ramping up/down value (ms).
    base_ramp=600


    # radius of a wheel (mm).
    radius = 15

    # diameter between the two wheels (mm).
    diameter = 140

    
    # pointer length (mm).
    pointer = 160


    def __init__(self, adress):
        '''Instantiate a new remote-robot object
        
        Parameters:
            adress (str): Pass the IP of your robot here.
        '''

        # establish a connection to the robot at the given IP.
        self.remote = rpyc.classic.connect(adress)

        # instantiate the EV3 dev module on the robot.
        self.ev3 = self.remote.modules['ev3dev.ev3']

        # create motor control objects with the remote EV3 dev module.
        self.mP = self.ev3.MediumMotor('outA'); self.mP.stop_action = 'hold'
        self.mL = self.ev3.LargeMotor('outB'); self.mL.stop_action = 'hold'
        self.mR = self.ev3.LargeMotor('outC'); self.mR.stop_action = 'hold'

        # calcultaing the circumfence (mm) of a wheel.
        self.circ = 2 * math.pi * self.radius

        # caculating how many degrees a wheel has to turn to move one mm.
        self.one_mm = 1 / (self.circ / 360)

        # calculating the circumfence of the turning circle of the robot.
        self.rob_circ = 2 * math.pi * (self.diameter / 2)

        # calculating how much degrees both wheels have to turn in order for the robot to turn one degree.
        self.turn_deg = 360 / self.circ * ( self.rob_circ / 360)


    # drive straight for the given amount of mm. Optionally, speed and ramping can ge passed as parameters.
    def drive(self, mm, ramp_up=base_ramp, ramp_dw=base_ramp):
        '''Drive straight for the given amount of mm.
        
        Parameters:
            mm (int): The amount of milimeters to drive straight for.
            ramp_up (int): amount of miliseconds until full speed.
            ramp_dw (int): amount of miliseconds until full stop.
        '''
        self.mL.run_to_rel_pos(position_sp=mm * self.one_mm, speed_sp=self.base_speed, ramp_up_sp=ramp_up, ramp_down_sp=ramp_dw)
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
        self.mL.run_to_rel_pos(position_sp=-degrees * self.turn_deg, speed_sp=self.base_speed)
        self.mR.run_to_rel_pos(position_sp=+degrees * self.turn_deg, speed_sp=self.base_speed)
        self.mL.wait_while('running')
        self.mR.wait_while('running')


    # let the robot speak the given text.
    def speak(self, text):
        '''Output given text as speach.
        
        Parameters:
            text (str): The text the robot will speak.
        '''
        self.ev3.Sound.speak(text)


    # raise or lower the pointer of the robot.
    def point(self, do_point):
        '''Raise or lower the pointer of the robot.
        
        Parameters:
            do_point (bool): True means lowered state, False means raised state.
        '''
        if (do_point):
            self.mP.run_to_abs_pos(position_sp=90, speed_sp=self.base_speed)
            self.mP.wait_while('running')
        else:
            self.mP.run_to_abs_pos(position_sp=0, speed_sp=self.base_speed)
            self.mP.wait_while('running')




