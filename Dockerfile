FROM ghcr.io/gmainardi/howler-monkey:latest

RUN apt update -y && apt upgrade -yam

WORKDIR /app
COPY . /app

RUN sed -i "s|/datasets|/|" /home/vscode/.config/Ultralytics/settings.yaml
RUN sed -i "s|mlflow: true|mlflow: false|" /home/vscode/.config/Ultralytics/settings.yaml

CMD ["uvicorn", "app:app"]