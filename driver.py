#!/usr/bin/env python3

# library for calculations
import math

class driver:
    '''A class to control an EV3 robot object.
    
    Supports moving inside a coordinate system.
    All coordniates are saved, so the robot can retreat to the starting point later.
    '''

    # default conditions: robot is facing right and is at pos 0,0 at the bottom left of the coordinates system.

    # orientation variables
    x_source = 0
    y_source = 0
    a_source = 0


    def __init__(self, vehicle):
        '''Instantiate a new driver object.

        Parameters:
            vehicle (obj): A robot object the driver will control.
        '''
        self.robot = vehicle

        # array to store past coordinates
        self.log = []

        # variable for pointing status of the robot
        self.pointing = False


    # return angle to turn by for new coordinates.
    def _calc_angle(self, x, y):
        '''Intern function. Do not call this from outside.
        
        Calculate the angle at which to turn by to face the new coordniates.

        Parameters:
            x (int): The new x coordinate.
            y (int): The new y coordinate.
        '''
        if (x == 0):
            if (y < 0):
                return -90
            elif (y > 0):
                return 90
            else:
                return 0
        return math.degrees(math.atan2(y, x))


    # return distance to new coordinates.
    def _calc_hypo(self, x, y):
        '''Intern function. Do not call this from outside.
        
        Calculate the distance to the new coordinates.

        Parameters:
            x (int): The new x coordinate.
            y (int): The new y coordinate.
        '''
        return math.sqrt(((x**2)+(y**2)))


    # unpoint the robot.
    def _unpoint(self):
        '''Intern function. Do not call this from outside.
        
        Revert the robot from pointing to standing on the target coordinates.
        '''

        if (self.pointing):

            self.robot.point(False)
            self.robot.drive(self.robot.pointer)
            self.robot.turn(self.a_source)
            self.a_source = 0

            self.pointing = False


    # move to new coordinates.
    def move(self, x_target, y_target, point=False, logging=True):
        '''Move the robot to new coordinates.

        Parameters:
            x_target (int): The target x coordinates.
            y_target (int): The target y coordinates.
            point (bool): Wether the robot should point at the new coordinates or not. False by default.
            logging (bool): Wether the robot should log the new position for when retreating. True by default.
        '''

        self._unpoint()

        # calculating how much we have to turn and move forward with default conditions

        x_diff = x_target - self.x_source
        y_diff = y_target - self.y_source

        # turning back to default conditions
        self.robot.turn_deg = self.a_source
        self.a_source = 0

        # angle we have to turn by
        angle = self._calc_angle(x_diff, y_diff)

        # length we have to move by
        hypo = self._calc_hypo(x_diff, y_diff)  

        # set pointer variable for next run
        self.pointing = point

        # account pointer for the length we move forward by
        if (point): hypo -= self.robot.pointer
        
        self.robot.turn(-angle)

        # move forward
        self.robot.drive(hypo)

        # point at the coordinates
        if (point): robot.point(True)

        # set new global coordinates
        self.x_source = x_target
        self.y_source = y_target
        self.a_source += angle

        # log movement
        if (logging):
            log_cords(self.x_source, self.y_source)

    # move retreat the robot back to the first coordinates.
    def retreat(self):
        '''Retreate the robot.
        
        Will move back over all coordinates that have been logged, ending with the first.
        '''

        # unpoint, so the calculation fits again
        self._unpoint()
        self.log.reverse()

        # move back to every coordinate that was visited
        for x in self.log:
            self.move(x[0], x[1], point=False, logging=False)
        
        # revert angle at which the turtle rests
        self.robot.turn(self.a_source)
        self.a_source = 0


    # store a new set of coordinates.
    def log_cords(self, x_new, y_new):
        '''Appends coordinates to the log.
        
        You should call this with 0, 0 when instantiating a new driver, 
        to ensure the robot retreating all the way back.

        Parameters:
            x_new (int): The x coordinate to be logged.
            y_new (int): The y coordinate to be logged.
        '''
        self.log.append([x_new, y_new])