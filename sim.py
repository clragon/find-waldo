#!/usr/bin/env python3

# necessary libraries
import turtle

class sim():

    # create a turtle
    window = turtle.Screen()
    turtle = turtle.Turtle()


    # emulating robot values for compatibility. The turtle does not need these.
    mL = None
    mR = None
    base_speed = 400
    base_ramp=600
    radius = 1.5
    diameter = 14
    pointer = 10
    point_dis = 4


    def __init__(self):

        
        # custom unit definition
        unit = 45

        # draw test coordinate system

        field = 16
        self.turtle.penup()
        self.turtle.setx(-(field / 2 * unit))
        self.turtle.sety(-(field / 2 * unit))
        self.turtle.pendown()


        def chess(size): 
            a = int(size / 2)
            self.turtle._tracer(0, 0)
            for x in range(0, int(size / 8)):
                for y in range(0, 2):
                    self.turtle.left(90)
                    self.turtle.forward(a * unit)
                    self.turtle.backward(a * unit)
                    self.turtle.right(90)
                    for z in range(0, a):
                        self.turtle.forward(unit)
                        self.turtle.left(90)
                        self.turtle.forward(a * unit)
                        self.turtle.right(90)
                        self.turtle.forward(unit)
                        self.turtle.right(90)
                        self.turtle.forward(a * unit)
                        self.turtle.left(90)
                    
                    self.turtle.left(90)
            self.turtle._tracer(1, 10)

        chess(field)

        self.turtle.setx(0)
        self.turtle.sety(0)
        self.turtle.color("red")


    # go x cm straight.
    def forward(self, cm, speed=base_speed, wait=True):
        # times 10 to accumulate for size
        self.turtle.forward(cm * 10)

    # turn right by x degrees
    def right(self, degrees, speed=base_speed, wait=True):
        self.turtle.right(degrees)

    # turn left by x degrees
    def left(self, degrees, speed=base_speed, wait=True):
        self.turtle.left(degrees)

