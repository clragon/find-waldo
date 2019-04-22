import turtle
import math
import time
from random import randint


window=turtle.Screen()
turtle = turtle.Turtle()


# return angle to turn by for new coordinates
def calc_angle(x, y):
    if (x == 0):
        if (y < 0):
            return -90
        elif (y > 0):
            return 90
        else:
            return 0
    return math.degrees(math.atan2(y, x))

# return distance to new coordinates
def calc_hypo(x, y):
    return math.sqrt(((x**2)+(y**2)))

# unit to cm conversion
unit = 45

# gobal orientation variables
x_source = 0
y_source = 0

a_source = 0

# throw this away later
x_target = 6 * unit
y_target = 7 * unit

# distance from mid point to pointer
point_dis = 4

# pointer calculations
pointer = 10
point_angle = calc_angle(point_dis, pointer)
pointing = False

# array to store past coordinates
log = []


# draw test coordinate system

field = 16
turtle.penup()
turtle.setx(-(field / 2 * unit))
turtle.sety(-(field / 2 * unit))
turtle.pendown()


def chess(size): 
    a = int(size / 2)
    # hideturtle()
    turtle._tracer(0, 0)
    for x in range(0, int(size / 8)):
        for y in range(0, 2):
            turtle.left(90)
            turtle.forward(a * unit)
            turtle.backward(a * unit)
            turtle.right(90)
            for z in range(0, a):
                turtle.forward(unit)
                turtle.left(90)
                turtle.forward(a * unit)
                turtle.right(90)
                turtle.forward(unit)
                turtle.right(90)
                turtle.forward(a * unit)
                turtle.left(90)
            
            turtle.left(90)
    turtle._tracer(1, 10)
    time.sleep(1)

chess(field)

turtle.setx(0)
turtle.sety(0)
turtle.color("red")

log.append([0, 0])    



# default conditions: robot is facing right and is at pos 0,0 at the bottom left of the coordinates system.


# unpoint the robot
def unpoint():

    global pointing
    global pointer
    global a_source

    if (pointing):

        turtle.left(point_angle)
        turtle.forward(pointer)
        turtle.right(a_source)
        a_source = 0

        pointing = False


# move to new coordinates
def move(x_target, y_target, point=False, logging=True):
    
    global pointing
    global pointer
    global point_angle
    global x_source
    global y_source
    global a_source
    global log

    unpoint()

    # calculating how much we have to turn and move forward with default conditions

    x_diff = x_target - x_source
    y_diff = y_target - y_source

    # turning back to default conditions
    turtle.right(a_source)
    a_source = 0

    # angle we have to turn by
    angle = calc_angle(x_diff, y_diff)

    # length we have to move by
    hypo = calc_hypo(x_diff, y_diff)  

    # debug print for calculated variables
    print("move: {} | x: {} | y: {} | {} | {} | a: {} | ang: {} | hy: {} | xd: {} | yd: {}".format(len(log), (x_target / unit), (y_target / unit), x_diff < 0, y_diff < 0, a_source, angle, hypo, x_diff, y_diff))

    # set pointer variable for next run
    pointing = point

    # account pointer for the length we move forward by
    if (point): hypo -= pointer
    
    turtle.left(angle)

    # move forward
    turtle.forward(hypo)

    # point at the coordinates
    if (point): turtle.right(point_angle)

    # set new global coordinates
    x_source = x_target
    y_source = y_target
    a_source += angle

    # log movement
    if (logging):
        mov = [x_source, y_source]
        log.append(mov)

    
def retreat():
    
    global a_source

    turtle.color("blue")

    # unpoint, so the calculation fits again
    unpoint()
    log.reverse()

    # move back to every coordinate that was visited
    for x in log:
        move(x[0], x[1], point=False, logging=False)
    
    # revert angle at which the turtle rests
    turtle.right(a_source)
    a_source = 0


# move to random coordinates
if(True):
    for x in range(0, 10): move(int(randint(-4, 4)) * unit, int(randint(-4, 4)) * unit)

# move(3 * unit, 4 * unit)
# move(3 * unit, 0 * unit)

# go back to starting point
retreat()

# leave the turtle window open
while True:
    time.sleep(1)

