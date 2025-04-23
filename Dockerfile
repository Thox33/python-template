FROM python:3.11-alpine3.17

# Install pre-requisites
RUN apk add --update make curl build-base

# Non root user for safety
RUN adduser -D nonroot
USER nonroot

WORKDIR /usr/src/app

# Install and setup poetry
RUN curl -sSL 'https://install.python-poetry.org' | POETRY_HOME=/home/nonroot/poetry python3 - --version 1.6.1 --y
RUN /home/nonroot/poetry/bin/poetry --version

# Install dependencies
RUN mkdir boilerplate_python && touch boilerplate_python/__init__.py
COPY --chown=nonroot:nonroot README.md ./README.md
COPY --chown=nonroot:nonroot poetry.lock ./poetry.lock
COPY --chown=nonroot:nonroot pyproject.toml ./pyproject.toml
RUN /home/nonroot/poetry/bin/poetry install

ENTRYPOINT ["/home/nonroot/poetry/bin/poetry", "run"]
