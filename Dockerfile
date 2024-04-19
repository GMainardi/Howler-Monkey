FROM ghcr.io/gmainardi/howler-monkey:latest

WORKDIR /app

COPY . /app

CMD ["uvicorn", "app:app"]