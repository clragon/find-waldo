from modules.robot_conf import *
from turtle import *


class Driver:
    '''A handler class for a turtle.

    Supports all functions a real EV3 Robot would support.
    '''

    def __init__(self, address=ROBOT_ADDRESS,
                 base_speed=MOTOR_BASE_SPEED,
                 base_ramp_up=MOTOR_BASE_RAMP_UP,
                 base_ramp_dw=MOTOR_BASE_RAMP_DOWN,
                 wheel_radius=WHEEL_RADIUS,
                 diameter=WHEEL_DISTANCE,
                 pointer=ROBOT_ARM_SIZE):

        self.speed = base_speed
        self.ramp_up = base_ramp_up
        self.ramp_dw = base_ramp_dw
        self.radius = wheel_radius
        self.diameter = diameter
        self.pointer = pointer

    def drive(self, mm, ramp_up=self.ramp_up, ramp_dw=self.ramp_dw):
        forward(mm)

    def driveL(self, grad, ramp_up=self.ramp_up, ramp_dw=self.ramp_dw):
        turn(-degrees)

    def driveR(self, grad, ramp_up=self.ramp_up, ramp_dw=self.ramp_dw):
        turn(degrees)

    def turn(self, degrees, ramp_up=self.ramp_up, ramp_dw=self.ramp_dw):
        right(degrees)

    def speak(self, text):
        pass

    def beep(self):
        pass

    def point(self):
        pass

    def unpoint(self):
        pass

    def btn_set(self, function, *args):
        pass

    def btn_check(self):
        pass

    def btn_default(self):
        pass
