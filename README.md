# Compressed-Sensing-Example
Dockerfile (Ubuntu, gedit, wget, python3, libLBFGS, Libtool, pylbfgs, sample code, and sample data)

The aim of this repository is to prepare a docker image for running a demonstration on compressed sensing for images.

The sample code included in this repository is largely extracted from http://www.pyrunner.com/weblog/2016/05/26/compressed-sensing-python/

The sample data used in the demonstration is obtained from http://people.sc.fsu.edu/~jburkardt/data/png/png.html

The following procedures are for Ubuntu 16.04 with Docker 17.12.0-ce

In the terminal:
```
sudo chmod u+x PyCS_build.sh #Create the image
sudo chmod u+x PyCS_X11.sh #Creat the container

./PyCS_build.sh
./PyCS_X11.sh
```

Inside the container PyCS:
```
python3 CS_Original_2D_png.py

```

To terminate, close all the pop-up figures and type ```exit```
