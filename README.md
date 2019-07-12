# Find Waldo
## Overview
This app is the core of project Waldo for Hackanapp for Managers.  
It contains code for controlling the robots, communicating with the amazon web service AI, the AI to find waldo inside a given picture and handling a smartphone as a webcam.

## Prerequisites
To use this repository, you will need the following:
- Lego Mindstorm ev3
- [Ev3dev-stretch](https://github.com/ev3dev/ev3dev/releases/download/ev3dev-stretch-2019-03-03/ev3dev-stretch-ev3-generic-2019-03-03.zip)
- [Python 3.5.3](https://www.python.org/downloads/release/python-353/)

## Mindstorm
Flash your copy of the ev3dev-stretch zip file into the SD card of your robot with a flash tool like [Rufus](https://github.com/pbatard/rufus/releases/download/v3.5/rufus-3.5p.exe).  
Now put the SD card back into your robot and boot it. Connect it to the same WiFi as your Computer using the robot's own interface. Afterwards connect to it with the IP it will display on the top left corner of its screen with an [SSH](https://www.howtogeek.com/336775/how-to-enable-and-use-windows-10s-built-in-ssh-commands/) client:
```cmd
ssh robot@<IP here>
``` 
The default password should be `maker`.
On the shell, install python and pip with
```bash
sudo apt install python3 python3-pip
```
Debian stretch doesnt currently have a newer version of python than 3.5.3, so this project works only with that.  
As soon as the command above is finished, install [RPyC](https://pypi.org/project/rpyc/) with pip
```bash
pip3 install rpyc==3.3.0
```
which is the latest rpyc version that is distributed with debian stretch.
The final step is to start the RPyC server, so the script can send commands to the robot, with 
```bash
python3 rpyc_classic.py
```
Now, either keep the terminal with this SSH session open or press CTRL+Z and then type
```bash
bg
```
to run the server in the background.

## Physical appearence

The script is built around robots that use two large motors (Out B and C) with wheels and one medium motor (Out D) for a pointer as well as a touch sensor (Out 1). To fully use it, your should now build your robot accordingly.


## Python
To use the provided scripts, you have to install its dependencies.  
Currently, only the face rekognition part of the script is in use, 
since the neural network for finding Waldo isn't very fast or stable.  
The dependencies you need are the following ones:
```cmd
pip install rpyc==3.3.0 pillow boto3
```
If you want to use the neural network as well, you will need extra dependencies:
```cmd
pip install matplotlib keras requests
```
and you will have to uncomment lines 2, 22 and 23 in [image.py](/image.py).


## Usage

The German documentation can be found here:  
- [Robotersteuerung](/docs/Robotersteuerung.docx)  
- [Kamerasteuerung](/docs/Kamerasteuerung.docx)


## Sources
- [remote ev3dev](https://ev3dev-lang.readthedocs.io/projects/python-ev3dev/en/stable/rpyc.html)
- [ev3dev motors](https://ev3dev-lang.readthedocs.io/projects/python-ev3dev/en/stable/motors.html)

### UML class diagram
![class overview](docs/uml.png)

## Known issues
- **Python is complaining about Visual Studio Directory path**  

    change these environment variables:
    ```
    VSINSTALLDIR=""
    VS90COMNTOOLS=""
    ```
