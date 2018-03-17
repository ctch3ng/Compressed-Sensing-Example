FROM ubuntu:latest

RUN apt-get update && install -y wget gedit git g++ gfortran build-essential automake python3 python3-pip python3-dev python3-setuptools python3-numpy python3-tk python3-scipy python3-pillow python3-matplotlib

WORKDIR /home
RUN mkdir /home/CS

WORKDIR /home/CS

RUN wget https://github.com/downloads/chokkan/liblbfgs/liblbfgs-1.10.tar.gz
RUN wget http://ftpmirror.gnu.org/libtool/libtool-2.4.6.tar.gz
RUN git clone https://bitbucket.org/rtaylor/pylbfgs.git

RUN tar -xvzf liblbfgs-1.10.tar.gz
RUN tar -xvzf libtool-2.4.6.tar.gz

WORKDIR /home/CS/libtool-2.4.6
RUN ./configure
RUN make
RUN make install

WORKDIR /home/CS/liblbfgs-1.10
RUN ./configure --enable-sse2
RUN make
RUN make install

WORKDIR /home/CS/pylbfgs
RUN python3 setup.py install

WORKDIR /home/CS

ADD Sample.png /home/CS
ADD CS_Original_2D_png.py /home/CS
