FROM ghcr.io/gmainardi/howler-monkey:latest

COPY ./dev-requirements.txt .

RUN pip install -r dev-requirements.txt

RUN sudo apt-get update && sudo apt-get upgrade -y

RUN yolo settings mlflow=false
RUN yolo settings datasets_dir='/workspaces/Howler-Monkey/'

# replace mlflow: true for mlflow: false on file 
ENV PYTHONPATH=/workspaces/HowlerMonkey/src/HowlerMonkey
