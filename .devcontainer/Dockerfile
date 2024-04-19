FROM ghcr.io/gmainardi/howler-monkey:latest

COPY ./dev-requirements.txt .

RUN pip install -r dev-requirements.txt


RUN sed -i "s|/datasets|/|" /home/vscode/.config/Ultralytics/settings.yaml