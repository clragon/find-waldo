#!/usr/bin/env python3

from config import *
import math
from .Logger import Logger


class Robot:
    # orientation variables
    x_source = 0
    y_source = 0
    a_source = 0
    driver = None
    point = False

    def __init__(self, driver, scale_factor=1):
        self.driver = driver
        self.scale_factor = scale_factor
        # Data structure where to store coordinates
        self.coordinates = []

        # variable for pointing status of the robot
        self.point = False

    def move_hypo(self, x_target, y_target):
        x_distance = self._distance(self.x_source, x_target)
        y_distance = self._distance(self.y_source, y_target)
        Logger.debug("Move to (X,Y): (" + str(x_target) + ", " + str(y_target) + ")")
        Logger.debug("X distance (mm):", x_distance)
        Logger.debug("Y distance (mm):", y_distance)
        hypo = math.sqrt(x_distance**2 + y_distance**2)
        angle = 90-math.degrees(math.asin(y_distance / hypo))
        Logger.debug("Hypo:", hypo)
        Logger.debug("Angle:", angle)
        self.driver.drive(ROBOT_ARM_SIZE)
        self.driver.turn(angle)
        self.driver.drive(hypo-ROBOT_ARM_SIZE)

    # move to new coordinates.
    def move_to(self, x_target, y_target):
        # x and y are in pixel
        # but the robot knows only millimeters
        x_distance = self._distance(self.x_source, x_target)
        y_distance = self._distance(self.y_source, y_target)
        self.driver.unpoint()
        Logger.debug("Move to (X,Y): (" + str(x_target) + ", " + str(y_target) + ")")
        Logger.debug("X distance (mm):", x_distance)
        Logger.debug("Y distance (mm):", y_distance)
        self.driver.drive(y_distance+ROBOT_ARM_SIZE)
        self.driver.turn(90)
        self.driver.drive(x_distance-ROBOT_ARM_SIZE)
        self._set_position(x_target, y_target)
        self.driver.point()
        self.driver.speak("Ciao Wally!")

    def retreat(self):
        Logger.debug("Retreat")
        x_distance = self._distance(self.x_source, 0)
        y_distance = self._distance(self.y_source, 0)
        Logger.debug("Retreat to (X,Y): (" + str(self.x_source) + ", " + str(self.y_source) + ")")
        Logger.debug("X distance: ", x_distance)
        Logger.debug("Y distance: ", y_distance)
        self.driver.unpoint()
        self.driver.drive(-x_distance+ROBOT_ARM_SIZE)
        self.driver.turn(-90)
        self.driver.drive(-ROBOT_ARM_SIZE-y_distance)

    def reset(self):
        # reset to initial status
        Logger.debug("Reset to the default values")
        self.driver.point()

    def get_driver(self):
        return self.driver

    def _set_position(self, x, y):
        Logger.debug("Setting new position ({},{})".format(x,y))
        self.x_source = x
        self.y_source = y

    def _distance(self, source, target):
        return self._pixel_to_millimeters(abs(target-source))

    def _pixel_to_millimeters(self, pixel_range):
        return pixel_range/self.scale_factor

