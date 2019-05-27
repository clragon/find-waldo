#!/usr/bin/env python3

from config import *
import math

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
        # array to store past coordinates
        self.log = []

        # variable for pointing status of the robot
        self.point = False

    def print_debug(self, msg, val=None):
        if val is None:
            print("DEBUG: " + str(msg))
        else:
            print("DEBUG: " + str(msg) + " = " + str(val))

    def move_hypo(self, x_target, y_target):
        x_distance = self._distance(self.x_source, x_target)
        y_distance = self._distance(self.y_source, y_target)
        self.print_debug("X target (pixel):", x_target)
        self.print_debug("Y target (pixel):", y_target)
        self.print_debug("X distance (mm):", x_distance)
        self.print_debug("Y distance (mm):", y_distance)
        hypo = math.sqrt(x_distance**2 + y_distance**2)
        angle = 90-math.degrees(math.asin(y_distance / hypo))
        self.print_debug("Hypo:", hypo)
        self.print_debug("Angle:", angle)
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
        self.print_debug("X target (pixel):", x_target)
        self.print_debug("Y target (pixel):", y_target)
        self.print_debug("X distance (mm):", x_distance)
        self.print_debug("Y distance (mm):", y_distance)
        # robot distance between the arm and the center = 16cm
        self.driver.drive(y_distance+ROBOT_ARM_SIZE)
        self.driver.turn(90)
        self.driver.drive(x_distance-ROBOT_ARM_SIZE)
        self._set_position(x_target, y_target)
        # self.driver.speak("Ehi Wally!")
        self.driver.point()

    def retreat(self):
        self.print_debug("Retreat")
        x_distance = self._distance(self.x_source, 0)
        y_distance = self._distance(self.y_source, 0)
        self.print_debug("X source: ", self.x_source)
        self.print_debug("Y source: ", self.y_source)
        self.print_debug("X distance: ", x_distance)
        self.print_debug("Y distance: ", y_distance)
        self.driver.unpoint()
        self.driver.drive(-x_distance+ROBOT_ARM_SIZE)
        self.driver.turn(-90)
        self.driver.drive(-ROBOT_ARM_SIZE-y_distance)

    def reset(self):
        # reset to initial status
        self.print_debug("Reset")
        self.driver.point()

    def get_driver(self):
        return self.driver

    def _set_position(self, x, y):
        self.x_source = x
        self.y_source = y

    def _distance(self, source, target):
        return self._pixel_to_millimeters(abs(target-source))

    def _pixel_to_millimeters(self, pixel_range):
        return pixel_range/self.scale_factor

