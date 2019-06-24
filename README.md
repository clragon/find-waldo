# Find Waldo
## Introduction
This is an app to find Waldo on a sheet of paper with a mobile phone camera, a Lego Mindstorms robot and AI face recognition for the workshop hack an app for Managers. 

# Prerequisites
- Lego Mindstorm ev3
- Python 3.5.3
- Pip
- Anaconda (https://repo.anaconda.com/archive/Anaconda3-2019.03-Windows-x86_64.exe)
    - Be sure the two boxes are checked
    ![class overview](docs/anaconda_install.png)
- Hotspot with IP Forwarding enabled

## Getting started
### Setup Network
Connect the notebook to the internet. Check if WLAN hotspot is active. Start robot and connect to the hotspot, find the IP adress of the robot in the windows WLAN hotspot settings.

### Start Remote python call on the robot
1. Open putty and connect via SSH to the IP of the robot:
	username robot
	password maker 
2. Run ./rpyc_server.sh

### Setup Windows
#### Create an environment with Anaconda
Open the Command Prompt and move inside the find-waldo folder
```bash
cd path for windows
```

Type the following commands
```bash
conda create -n waldo python=3.5.3 pip
conda activate waldo
```

And then install all the dependencies with
```bash
conda install tensorflow
pip install rpyc==3.3.0
conda install matplotlib
conda install keras
conda install pillow # this is for PIL
conda install requests
conda install boto3

```

#### Setup the PYTHONPATH environment variable
```bash
cd modules
setx PYTHONPATH "%cd%"
```

### Setup Linux
Open a terminal and move inside the find-waldo folder
```bash
cd path for linux
# install dependencies for CentOS/Fedora
sudo yum install freetype-devel libpng-devel
```

Then, create the Anaconda environment with
```
conda create -n waldo python=3.5.3
conda activate waldo
```

Then, install all the dependencies
```
conda install tensorflow
pip3 install rpyc==3.3.0
conda install matplotlib
conda install keras
conda install pillow # this is for PIL
conda install requests
conda install boto3
```

#### Setup the PYTHONPATH environment variable
```
cd modules
export PYTHONPATH=/usr/lib/python2.7/site-packages:`pwd`:`pwd`/slim
```

### Start the application
```
./find_waldo.py
```

## Further documentation
RPyC (pronounced as are-pie-see), or Remote Python Call:
[remote ev3dev](https://ev3dev-lang.readthedocs.io/projects/python-ev3dev/en/stable/rpyc.html)

### UML class diagram
![class overview](docs/class_overview.png)

## Issues
**Python is complaining against Visual Studio Directory path**
change environment variables
```
VSINSTALLDIR=""
VS90COMNTOOLS=""
```