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

- [uv](https://docs.astral.sh/uv/getting-started/installation/) >= 0.12

uv downloads and manages the Python interpreter itself, so a separate Python
installation is not required. Supported versions are 3.11 up to 3.14.

### Install

Run:

```bash
uv sync
```

To include the optional `performance` extra (uvloop, not available on Windows):

```bash
uv sync --extra performance
```

### Linting and typechecking

Setup pre-commit hooks:

```bash
uv run pre-commit install
```

Run on all files:

```bash
uv run pre-commit run -a
```

### Testing

Run tests with coverage report:

```bash
uv run pytest
```

or run in watch mode:

```bash
uv run ptw --now .
```
