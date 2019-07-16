from modules.robot_conf import *
import threading
import time
import math
import rpyc
import os


class Driver:
    '''A handler class for an EV3. Connects remotely over RPyC.
    
    Implements basic functions for moving.

    Driving straight, turning, speaking and pointing are supported.'''

    def __init__(self, address,
                 base_speed=MOTOR_BASE_SPEED,
                 base_ramp_up=MOTOR_BASE_RAMP_UP,
                 base_ramp_dw=MOTOR_BASE_RAMP_DOWN,
                 wheel_radius=WHEEL_RADIUS,
                 diameter=WHEEL_DISTANCE,
                 pointer=ROBOT_ARM_SIZE):

        try:
            # Try to connect to the robot
            self.remote_ip = rpyc.classic.connect(address)
            # instantiate the EV3 dev module on the robot.
            self.ev3 = self.remote_ip.modules['ev3dev.ev3']
        except:
            raise Exception("Robot couldnt be reached at {}".format(address))

        try:
            # create motor control objects with the remote EV3 dev module.
            self.mP = self.ev3.MediumMotor('outD'); self.mP.stop_action = 'hold'
            self.mL = self.ev3.LargeMotor('outB'); self.mL.stop_action = 'hold'
            self.mR = self.ev3.LargeMotor('outC'); self.mR.stop_action = 'hold'
        except:
            raise Exception("Motors couldn't be reached")

        try:
            self.btn = self.ev3.TouchSensor()
        except:
            print("no button found")

        self.btn_event = self.btn_default
        self.btn_args = None
        threading.Thread(target = self.btn_check).start()

        self.base_speed = base_speed
        self.base_ramp_up = base_ramp_up
        self.base_ramp_dw = base_ramp_dw
        self.radius = wheel_radius
        self.diameter = diameter
        self.pointer = pointer

        # calculating the circumference (mm) of a wheel.
        self.circ = 2 * math.pi * self.radius

        # calculating how many degrees a wheel has to turn to move one mm.
        self.one_mm = 1 / (self.circ / 360)

        # calculating the circumference of the turning circle of the robot.
        self.rob_circ = math.pi * self.diameter

        # calculating how much degrees both wheels have to turn in order for the robot to turn one degree.
        self.turn_deg = ( self.rob_circ / self.circ )


    # drive straight for the given amount of mm. Optionally, speed and ramping can ge passed as parameters.
    def drive(self, mm, ramp_up=MOTOR_BASE_RAMP_UP, ramp_dw=MOTOR_BASE_RAMP_DOWN):
        '''Drive straight for the given amount of mm.

        Parameters:
            mm (int): The amount of milimeters to drive straight for.
            ramp_up (int): amount of miliseconds until full speed.
            ramp_dw (int): amount of miliseconds until full stop.'''
        
        self.mL.run_to_rel_pos(position_sp=mm * self.one_mm, speed_sp=self.base_speed, ramp_up_sp=ramp_up, ramp_down_sp=ramp_dw)
        self.mR.run_to_rel_pos(position_sp=mm * self.one_mm, speed_sp=self.base_speed, ramp_up_sp=ramp_up/2, ramp_down_sp=ramp_dw)
        self.mL.wait_while('running')
        self.mR.wait_while('running')

    # drive one Motor for the given amount of degree. Optionally, speed and ramping can ge passed as parameters.
    def driveL(self, grad, ramp_up=MOTOR_BASE_RAMP_UP, ramp_dw=MOTOR_BASE_RAMP_DOWN):  
        self.mL.run_to_rel_pos(position_sp=grad, speed_sp=self.base_speed, ramp_up_sp=ramp_up, ramp_down_sp=ramp_dw)
        self.mL.wait_while('running')
 
     # drive one Motor for the given amount of degree. Optionally, speed and ramping can ge passed as parameters.
    def driveR(self, grad, ramp_up=MOTOR_BASE_RAMP_UP, ramp_dw=MOTOR_BASE_RAMP_DOWN):
        self.mR.run_to_rel_pos(position_sp=grad, speed_sp=self.base_speed, ramp_up_sp=ramp_up, ramp_down_sp=ramp_dw)
        self.mR.wait_while('running')
 
    # turn the robot to the right by given degrees. Minus degrees can be given to turn to the left.
    def turn(self, degrees, ramp_up=MOTOR_BASE_RAMP_UP, ramp_dw=MOTOR_BASE_RAMP_DOWN):
        '''Turn to the right by the given degrees.
        
        It is possible to pass negative degrees resulting in turning to the left.
        Parameters:
            degrees (int): How many degrees to turn to the right by.'''

        self.mL.run_to_rel_pos(position_sp= - (degrees * self.turn_deg), speed_sp=self.base_speed, ramp_up_sp=ramp_up, ramp_down_sp=ramp_dw)
        self.mR.run_to_rel_pos(position_sp= + (degrees * self.turn_deg), speed_sp=self.base_speed, ramp_up_sp=ramp_up/2, ramp_down_sp=ramp_dw)
        self.mL.wait_while('running')
        self.mR.wait_while('running')

    def speak(self, text):
        if ENABLE_SOUND:
            self.ev3.Sound.speak(text, espeak_opts='-a 200 -s 130').wait()

    def beep(self):
        if ENABLE_SOUND:
            self.ev3.Sound.beep()

    def point(self):
        self.mP.run_to_abs_pos(position_sp=90, speed_sp=self.base_speed/2)
        self.mP.wait_while('running')

    def unpoint(self):
        self.mP.run_to_abs_pos(position_sp=0, speed_sp=self.base_speed/2)
        self.mP.wait_while('running')

    def btn_set(self, function, *args):
        self.btn_event = function
        self.btn_args = args

    def btn_check(self):
        while True:
            if self.btn.is_pressed:
                if (self.btn_args is not None):
                    self.btn_event(*self.btn_args)
                else:
                    self.btn_event()

    def btn_default(self):
        self.beep()

