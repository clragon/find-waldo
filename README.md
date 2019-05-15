# find-waldo

## Introduction

This is an app to find Waldo on a sheet of paper with a mobile phone camera, a Lego Mindstorms robot and AI face recognition for the workshop hack an app for Managers. 

## Run the application

### Setup Network
Connect the notebook to the internet. Check if WLAN hotspot is active. Start robot and connect to the hotspot, find the IP adress of the robot in the windows WLAN hotspot settings.


### Start Remote phyton call on the robot
1. Open putty and connect via SSH to the IP of the robot:
	username robot
	password maker 
2. Run ./rpyc_server.sh

### Run main application
Open "Anaconda Prompt", change directory to project find-waldo and type:
activate waldo
python find_waldo.py


## Further documentation
RPyC (pronounced as are-pie-see), or Remote Python Call:
[remote ev3dev](https://ev3dev-lang.readthedocs.io/projects/python-ev3dev/en/stable/rpyc.html)
