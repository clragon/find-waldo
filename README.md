# Find Waldo
## Introduction
This is an app to find Waldo on a sheet of paper with a mobile phone camera, a Lego Mindstorms robot and AI face recognition for the workshop hack an app for Managers. 

# Prerequisites
- Lego Mindstorm ev3
- Python 3.5.3
- Pip
- Anaconda
- Hotspot with IP Forwarding enabled

## Run the application

### Setup Network
Connect the notebook to the internet. Check if WLAN hotspot is active. Start robot and connect to the hotspot, find the IP adress of the robot in the windows WLAN hotspot settings.

### Start Remote python call on the robot
1. Open putty and connect via SSH to the IP of the robot:
	username robot
	password maker 
2. Run ./rpyc_server.sh

### Install dependencies
#### Create an environment with Anaconda
##### Windows
Open "Anaconda Prompt", change directory to project find-waldo and type:
```
conda create -n waldo python=3.5.3
conda activate waldo
```
Then, install all the dependencies with `conda update --file ./environment-win.yml`
```
conda install tensorflow
pip install rpyc==3.3.0
conda install matplotlib
conda install keras
conda install pillow # this is for PIL
conda install requests
```

##### Linux/Unix
Open a terminal, change directory to project find-waldo and type:
```
sudo yum install freetype-devel libpng-devel
conda create -n waldo python=3.5.3
conda activate waldo
```
Then, install all the dependencies with `conda update --file ./environment-linux.yml`
```
conda install tensorflow
pip3 install rpyc==3.3.0
conda install matplotlib
conda install keras
conda install pillow # this is for PIL
conda install requests
pip install object-detection
```

#### Export/Import the environment
```
conda env export > environment.yml
```

```
conda update --file ./environment.yml
```

### Run main application
```
python find_waldo.py
```

## Further documentation
RPyC (pronounced as are-pie-see), or Remote Python Call:
[remote ev3dev](https://ev3dev-lang.readthedocs.io/projects/python-ev3dev/en/stable/rpyc.html)

## Issues
**Python is complaining against Visual Studio Directory path**
change environment variables
```
VSINSTALLDIR=""
VS90COMNTOOLS=""
```