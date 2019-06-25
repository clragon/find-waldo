#!/usr/bin/env python3

import os
from config import *
from modules.tf_brain import TFBrain as Brain
from modules.driver import Driver
from modules.robot import Robot
from modules.camera import Camera
from modules.local_image import LocalImage
from modules.aws_brain import AWSBrain


def find_waldo():
    target_image = LocalImage("docs/imgs/1.jpg")
    # Setup the Robot
    # Setup the brain
    brain = Brain(target_image, 'models/frozen_inference_graph.pb')
    if brain.find_waldo() is True:
        (x, y) = brain.get_coords()
        target_image.set_scale_factor()
        # Move to Wally
        robot = Robot(Driver(ROBOT_ADDRESS), target_image)
        robot.move_to(x, y)
        robot.retreat()
        robot.reset()
    else:


def find_face():
    # source face
    cam = Camera(CAMERA_ADDRESS, 8080)
    cam.set_offline()
    cam.take_photo()
    group_image = LocalImage("docs/photo/ti8m-group.jpg")

    aws_brain = AWSBrain(cam, group_image)
    if aws_brain.find_face():
        (x, y) = aws_brain.get_coords()
        # move the robot here 748.0361535549164, 1389.703828215599
        LocalImage("docs/photo/ti8m-group.jpg").mark(aws_brain.get_box())
        robot = Robot(Driver(ROBOT_ADDRESS), LocalImage("docs/photo/ti8m-group.jpg"))
        robot.move_to(x, group_image.get_height()-y)
        robot.retreat()
        robot.reset()
    else:


if __name__ == '__main__':
    try:
        os.mkdir("heads")
        print("The heads directory has been created")
    except OSError:
        print("The heads folder already exists")
        pass
    find_face()
