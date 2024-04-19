# Change to prebuild container
FROM mcr.microsoft.com/devcontainers/python:3.11-bullseye


RUN sudo apt-get update && sudo apt-get upgrade -y
RUN sudo apt-get install -y libgl1-mesa-glx

COPY ./requirements.txt .

RUN pip install -r requirements.txt

ENV DEFAULT_YOLO_DATASET_PATH /workspaces/Howler-Monkey/datasets
ENV NEW_YOLO_DATASET_PATH /workspaces/Howler-Monkey/

RUN sed -i 's|${DEFAULT_YOLO_DATASET_PATH}|${NEW_YOLO_DATASET_PATH}|' settings.yaml