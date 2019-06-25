#!/usr/bin/env python3

from modules.robot import Robot
from modules.driver import Driver
from modules.logger import Logger
from modules.local_image import LocalImage
from config import *
import os
import time


def test_robot():
    Logger.debug("Testing robot")
    image = LocalImage("docs/imgs/2.jpg")
    robot = Robot(Driver(ROBOT_ADDRESS), image)
    robot.get_driver().drive(200)
    robot.get_driver().turn(-90)
    robot.point()
    time.sleep(1)
    robot.get_driver().turn(+180)
    robot.get_driver().turn(-90)
    robot.get_driver().drive(-200)


if __name__ == '__main__':
    try:
        os.mkdir("heads")
        print("Directory heads created")
    except OSError:
        print("Directory heads already initialized")
        pass
    test_robot()
