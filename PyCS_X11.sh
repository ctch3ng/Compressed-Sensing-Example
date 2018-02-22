#!/bin/bash

sudo docker run -it \
    --user=$(id -u) \
    --env="DISPLAY" \
    --workdir="/home/CS" \
    --volume="/home/$USER:/home/$USER" \
    --volume="/etc/group:/etc/group:ro" \
    --volume="/etc/passwd:/etc/passwd:ro" \
    --volume="/etc/shadow:/etc/shadow:ro" \
    --volume="/etc/sudoers.d:/etc/sudoers.d:ro" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    --name PyCS \
    ubuntu_py_comp_sense

sudo docker rm /PyCS


