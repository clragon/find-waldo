#!/usr/bin/env python3

from robot import Robot
import time
import os


def test_robot():
    robot = Robot()
    robot.Vorwärts(200)
    robot.Rechts(90)
    robot.Zeigen()
    time.sleep(1)
    robot.Rechts(180)
    robot.Links(90)
    robot.Rückwärts(200)


if __name__ == '__main__':
    os.makedirs("heads", exist_ok=True)
    test_robot()
