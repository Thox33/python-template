.. _developer-introduction:

************
Introduction
************

Prerequisites
=============

Make sure to install:

- Python >= 3.10
- Poetry >= 1.4.0

See `Poetry documentation <https://python-poetry.org/docs/>`_ for more information.

Installation
============

You have to install all development dependencies:

.. code-block:: bash

    poetry install

This will install all dependencies and create a virtual environment. Our development dependencies are divided into three groups:

1. **testing**: dependencies for testing like pytest, pytest-cov, pytest-mock, etc.
2. **linting**: dependencies for code style and code formatting like flake8, black, isort, etc.
3. **docs**: dependencies for documentation like sphinx, sphinx-autodoc-typehints, etc.

Post-Installation
=================

After installation perform the following steps:

1. Setup pre-commit hooks (this will prevent you from pushing changes not formatted according to our code style):

.. code-block:: bash

    poetry run pre-commit install
