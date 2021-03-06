# Compressed-Sensing-Example
Dockerfile (Ubuntu, gedit, wget, python3, libLBFGS, Libtool, pylbfgs, sample code, and sample data)

The aim of this repository is to prepare a docker image for running a demonstration on compressed sensing for images.

The sample code included in this repository is largely extracted from http://www.pyrunner.com/weblog/2016/05/26/compressed-sensing-python/

The sample data used in the demonstration is obtained from http://people.sc.fsu.edu/~jburkardt/data/png/png.html

**The following procedures are for Ubuntu 16.04 with Docker 17.12.0-ce installed**

In the terminal:
```
sudo chmod u+x PyCS_build.sh
sudo chmod u+x PyCS_X11.sh 

#Create a docker image ubuntu_py_comp_sense
./PyCS_build.sh 

#Create a container PyCS using the docker image ubuntu_py_comp_sense
./PyCS_X11.sh 
```

**The following procedures are for macOS 10.13.2 with Docker 17.12.0-ce and XQuartz installed**

[XQuartz](https://www.xquartz.org/): Preferences -> Security -> (Check) Allow connections from network clients

In the terminal:
```
sudo chmod u+x PyCS_build.sh
sudo chmod u+x PyCS_XQuartz.sh 

#Create a docker image ubuntu_py_comp_sense
./PyCS_build.sh 

#Create a container PyCS using the docker image ubuntu_py_comp_sense
./PyCS_XQuartz.sh 
```

**In the container,** to run the example,
```
python3 CS_Original_2D_png.py
```
To terminate, close all the pop-up figures and type ```exit```
