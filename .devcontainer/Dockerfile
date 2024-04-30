FROM ghcr.io/gmainardi/howler-monkey-cuda:latest

COPY ./dev-requirements.txt .

RUN pip install -r dev-requirements.txt

RUN sed -i "s|/usr/src/datasets|/workspaces/Howler-Monkey|" /root/.config/Ultralytics/settings.yaml
RUN sed -i "s|mlflow: true|mlflow: false|" /root/.config/Ultralytics/settings.yaml