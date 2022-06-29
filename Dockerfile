FROM library/python:3.9-slim

RUN mkdir /opt/project
RUN mkdir /opt/project/scripts
RUN mkdir /opt/project/results

WORKDIR /opt/project

RUN apt-get update --allow-insecure-repositories && \
    apt-get -y --allow-unauthenticated install \
    curl \
    netcat\
    ca-certificates \
    gnupg \
    lsb-release \
    docker.io \
    docker-compose && \
    apt-get clean

RUN python -m pip install --upgrade pip
RUN pip install poetry

COPY poetry.lock        /opt/project/poetry.lock
COPY pyproject.toml     /opt/project/pyproject.toml

RUN poetry install
