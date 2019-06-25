# library for calculations (turning degrees, etc).
import math
# configuration file
from config import *
# library for remote connection to the robot.
import rpyc
# logging class
from logger import Logger


class Driver:
    '''A handler class for an EV3. Connects remotely over RPyC.
    
    Implements basic functions for moving.

    Driving straight, turning, speaking and pointing are supported.
    '''
    remote_ip = ''
    base_speed = 0
    base_ramp_up = 0
    base_ramp_dw = 0
    radius = 0
    diameter = 0
    pointer = 0
    status = 1

    def __init__(self, address,
                 base_speed=MOTOR_BASE_SPEED,
                 base_ramp_up=MOTOR_BASE_RAMP_UP,
                 base_ramp_dw=MOTOR_BASE_RAMP_DOWN,
                 wheel_radius=WHEEL_RADIUS,
                 diameter=ROBOT_DISTANCE_WHEEL,
                 pointer=ROBOT_ARM_SIZE):


        try:
            # Try to connect to the robot
            self.remote_ip = rpyc.classic.connect(address)
            # instantiate the EV3 dev module on the robot.
            self.ev3 = self.remote_ip.modules['ev3dev.ev3']

        except:
            Logger.error("The Robot isn't reachable at", address)
            Logger.error("Setting offline mode")
            self.set_offline()

        try:
            # create motor control objects with the remote EV3 dev module.
            self.mP = self.ev3.MediumMotor('outA'); self.mP.stop_action = 'hold'
            self.mL = self.ev3.LargeMotor('outB'); self.mL.stop_action = 'hold'
            self.mR = self.ev3.LargeMotor('outC'); self.mR.stop_action = 'hold'
        
        except:
            Logger.error("Motors arent set up correctly.")
            os.exit()

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
        self.rob_circ = 2 * math.pi * (self.diameter / 2)

        # calculating how much degrees both wheels have to turn in order for the robot to turn one degree.
        self.turn_deg = 360 / self.circ * self.rob_circ
        self.set_online()


    def is_online(self):
        return self.status == 1

    def set_offline(self):
        self.status = 0

    def set_online(self):
        self.status = 1

    # drive straight for the given amount of mm. Optionally, speed and ramping can ge passed as parameters.
    def drive(self, mm, ramp_up=MOTOR_BASE_RAMP_UP, ramp_dw=MOTOR_BASE_RAMP_DOWN):
        '''Drive straight for the given amount of mm.

        Parameters:
            mm (int): The amount of milimeters to drive straight for.
            ramp_up (int): amount of miliseconds until full speed.
            ramp_dw (int): amount of miliseconds until full stop.
        '''
        self.mL.run_to_rel_pos(position_sp=mm * self.one_mm, speed_sp=self.base_speed, ramp_up_sp=ramp_up, ramp_down_sp=ramp_dw)
        self.mR.run_to_rel_pos(position_sp=mm * self.one_mm, speed_sp=self.base_speed, ramp_up_sp=ramp_up/2, ramp_down_sp=ramp_dw)
        self.mL.wait_while('running')
        self.mR.wait_while('running')

    # turn the robot to the right by given degrees. Minus degrees can be given to turn to the left.
    def turn(self, degrees, ramp_up=MOTOR_BASE_RAMP_UP, ramp_dw=MOTOR_BASE_RAMP_DOWN):
        '''Turn to the right by the given degrees.
        
        It is possible to pass negative degrees resulting in turning to the left.
        Parameters:
            degrees (int): How many degrees to turn to the right by.
        '''

        arc=(degrees*self.rob_circ/(4*360))*(ROBOT_ARM_SIZE/10)
        print("Arc: ", arc)
        self.mL.run_to_rel_pos(position_sp=-arc, speed_sp=self.base_speed, ramp_up_sp=ramp_up, ramp_down_sp=ramp_dw)
        self.mR.run_to_rel_pos(position_sp=+arc, speed_sp=self.base_speed, ramp_up_sp=ramp_up/2, ramp_down_sp=ramp_dw)
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


class DriverOffline(Driver):
    def __init__(self, base_speed=MOTOR_BASE_SPEED,
                 base_ramp_up=MOTOR_BASE_RAMP_UP,
                 base_ramp_dw=MOTOR_BASE_RAMP_DOWN,
                 wheel_radius=WHEEL_RADIUS,
                 diameter=ROBOT_DISTANCE_WHEEL,
                 pointer=ROBOT_ARM_SIZE):
        Logger.debug("Init Offline Driver")
        self.base_speed = base_speed
        self.base_ramp_up = base_ramp_up
        self.base_ramp_dw = base_ramp_dw
        self.radius = wheel_radius
        self.diameter = diameter
        self.pointer = pointer

    def drive(self, mm, ramp_up=MOTOR_BASE_RAMP_UP, ramp_dw=MOTOR_BASE_RAMP_DOWN):
        Logger.debug("Offline drive")

    def turn(self, degrees, ramp_up=MOTOR_BASE_RAMP_UP, ramp_dw=MOTOR_BASE_RAMP_DOWN):
        Logger.debug("Offline turn")

    def speak(self, text):
        Logger.debug("Offline speak")

    def beep(self):
        Logger.debug("Offline beep")

    def point(self):
        Logger.debug("Offline point")

    def unpoint(self):
        Logger.debug("Offline unpoint")


