# Change to prebuild container
FROM mcr.microsoft.com/devcontainers/python:3.11-bullseye


RUN sudo apt-get update && sudo apt-get upgrade -y
RUN sudo apt-get install -y libgl1-mesa-glx

COPY ./requirements.txt .

RUN pip install -r requirements.txt


RUN yolo

RUN yolo settings mlflow=false
RUN yolo settings datasets_dir='/workspaces/Howler-Monkey/'

ENV PYTHONPATH=/workspaces/HowlerMonkey/src/HowlerMonkey