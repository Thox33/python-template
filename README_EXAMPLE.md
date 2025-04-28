# Boilerplate Python

TODO: Description

## Prerequisites

TODO: Prerequisites

## Install

TODO: Install information

## Starting

TODO: How to start and use

## Configuration

TODO: Configuration information

## Development

### Prerequisites

Make sure to install:

- Python >= 3.11
- Poetry >= 1.4.0

### Install

Run:

```bash
poetry install
```

### Linting and typechecking

Setup pre-commit hooks:

```bash
poetry run pre-commit install
```

Run on all files:

```bash
poetry run pre-commit run -a
```

### Testing

Run tests with coverage report:

```bash
poetry run pytest
```

or run in watch mode:

```bash
poetry run pytest-watch -n
```

## Documentation

We are using Sphinx with the ReadTheDocs html theme.

You have the following ways to run a live reloading server to develop this documentation

- Run `poetry run python docs/docs_livereload.py`
- Run `docker compose up --build docs`

Both will run a webserver listing on http://localhost:5500 and will automatically rebuild the documentation (and
reloading the website inside your browser) if a file in docs or boilerplate_python directory changes.

(Third option would be to manually call `make html` or `./make.bat html` inside the docs directory.)
