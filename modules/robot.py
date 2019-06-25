from config import *
from driver import *
import math


class Robot:
    # orientation variables
    x_source = 0
    y_source = 0
    driver = None
    point = False
    source_image = None

    def __init__(self, driver, source_image):
        if not driver.is_online():
            self.driver = DriverOffline()
        else:
            self.driver = driver

        self.source_image = source_image
        # Data structure where to store coordinates
        self.coordinates = []

        # variable for pointing status of the robot
        self.point = False

    def move_hypo(self, x_target, y_target):
        x_distance = self._distance(self.x_source, x_target)
        y_distance = self._distance(self.y_source, y_target)
        hypo = math.sqrt(x_distance**2 + y_distance**2)
        angle = 90-math.degrees(math.asin(y_distance / hypo))
        self.driver.drive(ROBOT_ARM_SIZE)
        self.driver.turn(angle)
        self.driver.drive(hypo-ROBOT_ARM_SIZE)
        self._set_position(x_target, y_target)
        self.driver.point()

    # move to new coordinates.
    def move_to(self, x_target, y_target):
        # x and y are in pixel
        # but the robot knows only millimeters
        x_distance = self._distance(self.x_source, x_target)
        y_distance = self._distance(self.y_source, y_target)
        self.driver.unpoint()
        self.driver.drive(y_distance+ROBOT_ARM_SIZE)
        self.driver.turn(90)
        self.driver.drive(x_distance-ROBOT_ARM_SIZE)
        self._set_position(x_target, y_target)
        self.driver.point()
        self.driver.speak("Ciao Wally!")

    def retreat(self):
        x_distance = self._distance(self.x_source, 0)
        y_distance = self._distance(self.y_source, 0)
        self.driver.unpoint()
        self.driver.drive(-x_distance+ROBOT_ARM_SIZE)
        self.driver.turn(-90)
        self.driver.drive(-ROBOT_ARM_SIZE-y_distance)

    def reset(self):
        # reset to initial status
        self.driver.point()

    def get_driver(self):
        return self.driver

    def _set_position(self, x, y):
        self.x_source = x
        self.y_source = y

    def _distance(self, source, target):
        return self._pixel_to_millimeters(abs(target-source))

    def _pixel_to_millimeters(self, pixel_range):
        scale_factor = self.source_image.get_scale_factor()
        return pixel_range/scale_factor

