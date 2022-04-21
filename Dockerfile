FROM ubuntu:latest

RUN apt-get update && apt-get install -y sudo wget vim curl

RUN wget https://repo.continuum.io/archive/Anaconda3-2021.11-Linux-x86_64.sh && \
    sh Anaconda3-2021.11-Linux-x86_64.sh -b  && \
    rm -f Anaconda3-2021.11-Linux-x86_64.sh && 

ENV PATH $PATH:/root/anaconda3/bin

RUN pip install --upgrade pip
RUN conda activate base && \
    conda create -n board python=3.9 && \
    conda activate board
RUN pip install git+https://github.com/a5chin/awesome-board

RUN mkdir /workspace