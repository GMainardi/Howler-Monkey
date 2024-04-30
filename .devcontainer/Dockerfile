FROM ghcr.io/gmainardi/howler-monkey-cuda:latest

COPY ./dev-requirements.txt .

RUN pip install -r dev-requirements.txt

RUN sudo apt-get update && sudo apt-get upgrade -y
