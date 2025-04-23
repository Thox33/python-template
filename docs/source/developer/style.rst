**********
Code Style
**********

Linting and formatting
======================

We orientate our code style on the `Google Python Style Guide <https://google.github.io/styleguide/pyguide.html>`_
and `PEP 8 <https://peps.python.org/pep-0008/>`_.

To enforce this rules we use pre-commit. To run them locally use:

.. code-block:: bash

    pre-commit run -a

See `pre-commit <https://pre-commit.com/>`_ for more information.

This will lint your code with `flake8 <https://flake8.pycqa.org/en/latest/>`_ and automatically try to fix some issues with `black <https://black.readthedocs.io/en/stable/>`_.

We also configured a few more packages to run with pre-commit:

- `isort <https://pycqa.github.io/isort/>`_ to sort imports
- `mypy <https://mypy.readthedocs.io/en/stable/>`_ for type hints checking
- `bandit <https://bandit.readthedocs.io/en/latest/>`_ for security checking

See the .pre-commit-config.yaml file for more.

Type hints
==========

As Python itself is a dynamically typed language, we use their `typing <https://docs.python.org/3.10/library/typing.html>`_ support to add type hints to our code.
This helps to understand the code and to find bugs.

To enforce type hints we use `mypy <https://mypy.readthedocs.io/en/stable/>`_. Its configured to be strict and to fail on any type hint error.
If you run pre-commit you will also run mypy.


Security
========

We use `bandit <https://bandit.readthedocs.io/en/latest/>`_ to find common security issues in our code.
If you run pre-commit you will also run bandit.
