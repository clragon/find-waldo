#!/usr/bin/env python3

#import robot
import sim
import driver
import time

def main():

    vehicle = sim.sim()
    drivee = driver.driver(vehicle)

    # starting at 0,0
    drivee.log.append([0, 0])

    # move to random coordinates
    # should actually get coordinates from AI here
    from random import randint

    # one unit of the coordinate system in cm
    unit = 45

    if(True):
        for x in range(0, 10): drivee.move(int(randint(-4, 4)) * unit, int(randint(-4, 4)) * unit)
    
    
    # go back to starting point
    drivee.retreat()

    # in case of turtle
    while True: time.sleep(1)


if __name__ == '__main__':
    main()