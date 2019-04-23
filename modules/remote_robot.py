#!/usr/bin/env python3

import rpyc

def robot_go(coord_x, coord_y):
    print("Initializing remote connection to robot...")
    conn = rpyc.classic.connect('ev3dev') # host name or IP address of the EV3
    ev3 = conn.modules['ev3dev.ev3']      # import ev3dev.ev3 remotely
    m = ev3.LargeMotor('outA')
    m.run_timed(time_sp=1000, speed_sp=600)