************
Code Testing
************

We use the `pytest <https://docs.pytest.org/en/7.3.x/>`_ package to test our code.

To run the tests, simply run `pytest` in the root directory of the project.

.. code-block:: bash

    pytest

This will automatically run all tests in the `tests/` directory and additionally creates an code coverage report
displayed at the end of the test run.

We configured a few plugins for pytest:

- `pytest-cov <https://pypi.org/project/pytest-cov/>`_ to generate a code coverage report
- `pytest-mock <https://pypi.org/project/pytest-mock/>`_ to mock objects in tests
- `pytest-asyncio <https://pypi.org/project/pytest-asyncio/>`_ to test async code
- `pytest-sugar <https://pypi.org/project/pytest-sugar/>`_ to make the test output more readable
- `pytest-icdiff <https://pypi.org/project/pytest-icdiff/>`_ to make the test output more readable

To run pytest in watch mode, use the following command:

.. code-block:: bash

    pytest-watch -n

.. hint:: -n deactivates an annoying beep sound when tests run is done

If you haven't installed python on your system, you can use the docker container to run the tests:

.. code-block:: bash

    docker compose up --build tests

.. hint:: This will run the tests in watch mode.
