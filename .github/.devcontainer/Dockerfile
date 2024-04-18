# Change to prebuild container
FROM mcr.microsoft.com/devcontainers/python:3.11-bullseye


RUN sudo apt-get update && sudo apt-get upgrade -y

COPY ./requirements.txt .

RUN pip install -r requirements.txt