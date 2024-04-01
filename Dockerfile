FROM python:3.9.6-slim-buster

RUN apt update -y && apt install awscli -y

RUN pip install poetry==1.7.1

# set poetry to not create virtualenvs
ENV POETRY_VIRTUALENVS_CREATE=false
ENV POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

# copy and install dependencies
COPY pyproject.toml poetry.* ./
RUN touch README.md
RUN poetry install --without dev --no-root && rm -rf $POETRY_CACHE_DIR

COPY . /app

CMD ["uvicorn", "app:app"]