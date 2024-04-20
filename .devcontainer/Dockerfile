FROM ghcr.io/gmainardi/howler-monkey:latest

COPY ./dev-requirements.txt .

RUN pip install -r dev-requirements.txt

RUN sudo apt-get update && sudo apt-get upgrade -y

RUN sed -i "s|/datasets|/|" /home/vscode/.config/Ultralytics/settings.yaml
RUN sed -i "s|mlflow: true|mlflow: false|" /home/vscode/.config/Ultralytics/settings.yaml