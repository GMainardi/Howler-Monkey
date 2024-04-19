# Change to prebuild container
FROM mcr.microsoft.com/devcontainers/python:3.11-bullseye


RUN sudo apt-get update && sudo apt-get upgrade -y
RUN sudo apt-get install -y libgl1-mesa-glx

COPY ./requirements.txt .

RUN pip install -r requirements.txt

RUN sed -i 's|/datasets|/}|' /home/vscode/.config/Ultralytics/settings.yaml