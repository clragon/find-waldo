#!/usr/bin/env python3
import os
from config import *
from modules.TFBrain import TFBrain as Brain
from modules.Driver import Driver
from modules.Robot import Robot
from modules.Camera import Camera
from modules.LocalImage import LocalImage
from modules.Logger import Logger


def main():
    # Setup the Head and get a picture
    image = LocalImage("docs/imgs/2.jpg")
    # image = LocalImage("docs/imgs/1.jpg")

    # Setup the Robot
    robot = Robot(Driver(ROBOT_ADDRESS), image)

    # Setup the Brain
    brain = Brain(image, 'models/frozen_inference_graph.pb')
    if brain.find_waldo() is True:
        (x, y) = brain.get_coords()
        print("Waldo found! at ({}.{})".format(x, y))
    else:
        print("Waldo not found")
        (x, y) = (50, 50)
    image.get_scale_factor()
    # Move to Wally
    robot.move_to(x, y)
    robot.retreat()
    robot.reset()


def test_head():
    Logger.debug("Testing head")
    image = LocalImage("docs/imgs/1.jpg")
    Logger.info("Local image loaded")
    image = Camera(CAMERA_ADDRESS)
    image.take_photo()
    Logger.info("Take photo")
    image.show()


def test_brain():
    Logger.debug("Testing brain")
    # Setup the Brain
    image = LocalImage("docs/imgs/1.jpg")
    brain = Brain(image,'models/frozen_inference_graph.pb')
    if brain.find_waldo() is True:
        (x, y) = brain.get_coords()
        Logger.debug("Waldo found! at ({}.{})".format(x, y))
    else:
        Logger.debug("Waldo not found!")


def test_robot():
    Logger.debug("Testing robot")
    image = LocalImage("docs/imgs/2.jpg")
    robot = Robot(Driver(ROBOT_ADDRESS), image)
    # robot.get_driver().drive(200)
    robot.get_driver().turn(-90)
    # robot.get_driver().drive(400)
    robot.get_driver().turn(+180)
    # robot.get_driver().drive(400)
    robot.get_driver().turn(-90)
    # robot.get_driver().drive(-200)


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
