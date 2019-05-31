#!/usr/bin/env python3
from PIL import Image
import os
from config import *
from modules.Brain import Brain
from modules.Driver import Driver
from modules.Robot import Robot


def move_to_wally(robot, x, y):
    #robot.move_hypo(x, y)
    #robot.move_to(x, y)
    #robot.retreat()
    #robot.reset()
    # test
    robot.get_driver().point()
    robot.get_driver().drive(400)
    robot.get_driver().turn(90)
    robot.get_driver().turn(-90)
    robot.get_driver().drive(-400)


def search_wally(image):
    brain = Brain(image,'models/frozen_inference_graph.pb')
    if brain.find_waldo() is True:
        (x, y) = brain.get_waldo_coords()
        print("Waldo found! at ({}.{})".format(x, y))
        return (x, y)
    else:
        print("Waldo not found")
        return (50, 50)


def setup_robot(scale_factor):
    # Create the Driver : The driver is the interface with the robot
    driver = Driver(IP_ADDRESS, MOTOR_BASE_SPEED, MOTOR_BASE_RAMP_UP, MOTOR_BASE_RAMP_DOWN, WHEEL_RADIUS, ROBOT_DISTANCE_WHEEL, ROBOT_ARM_SIZE)
    # Create the Robot : It performs actions through the driver
    return Robot(driver, scale_factor)


def main():
    # Code here
    image=Image.open("docs/imgs/2.jpg")
    (width, height) = image.size
    # 310 is the A3 size
    scale_factor = (width/340)

    robot = setup_robot(scale_factor)
    robot.get_driver().beep()
    #(x, y) = search_wally(image)
    move_to_wally(robot, 50, 50)


################################
# Don't change the code below
#
if __name__ == '__main__':
    try:
        os.mkdir("heads")
        print("The heads directory has been created")
    except OSError:
        print("The heads folder already exists")
        pass
    main()
