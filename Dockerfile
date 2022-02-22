FROM python:3.9-buster

RUN apt -y update
RUN apt install -y --fix-missing \
    build-essential \
    cmake \
    gfortran \
    git \
    wget \
    curl \
    pkg-config \
    python3-dev \
    python3-numpy \
    python3-opencv\
    software-properties-common \
    zip \
    && apt clean && rm -rf /tmp/* /var/tmp/*

COPY backend.py backend.py
COPY requirements.txt requirements.txt
RUN pip install -U pip
RUN pip install -r requirements.txt

CMD uvicorn backend:app --host 0.0.0.0 --port 8888 
