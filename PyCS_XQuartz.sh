#!/bin/sh
 
echo "Image: ubuntu_py_comp_sense"
echo "Alias: PyCS"

# run xhost and allow connections from your local machine:

ip=$(ifconfig en0 | grep inet | awk '$1=="inet" {print $2}')
xhost + $ip

docker run -it --name PyCS -e DISPLAY=$ip:0 -v /tmp/.X11-unix:/tmp/.X11-unix ubuntu_py_comp_sense

xhost - $ip
docker rm /PyCS
