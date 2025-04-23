*************
Documentation
*************

We are using `Sphinx <https://www.sphinx-doc.org/>`_ with the `ReadTheDocs html theme <https://github.com/readthedocs/sphinx_rtd_theme>`_.

Its configured to provide a Html version of the documentation but could be easily extended to provide a PDF or EPub version as well.

This extensions are configured to enrich the documentation:

* `sphinx.ext.autodoc – Include documentation from docstrings <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_
* `sphinx_autodoc_typehints - Include typehints in autodoc documentation <https://pypi.org/project/sphinx-autodoc-typehints/>`_
* `sphinx.ext.autosectionlabel – Allow reference sections using its title <https://www.sphinx-doc.org/en/master/usage/extensions/autosectionlabel.html>`_
* `sphinx.ext.coverage – Collect doc coverage stats <https://www.sphinx-doc.org/en/master/usage/extensions/coverage.html>`_
* `sphinx.ext.doctest – Test snippets in the documentation <https://www.sphinx-doc.org/en/master/usage/extensions/doctest.html>`_
* `sphinx.ext.duration – Measure durations of Sphinx processing <https://www.sphinx-doc.org/en/master/usage/extensions/duration.html>`_
* `sphinx.ext.extlinks – Markup to shorten external links <https://www.sphinx-doc.org/en/master/usage/extensions/extlinks.html>`_
* `sphinx.ext.intersphinx – Link to other projects’ documentation <https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html>`_
* `sphinx.ext.napoleon – Support for NumPy and Google style docstrings <https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html>`_
* `sphinx.ext.viewcode – Add links to highlighted source code <https://www.sphinx-doc.org/en/master/usage/extensions/viewcode.html>`_
* `sphinxcontrib.autodoc_pydantic - Include pydantic models with constraints <https://autodoc-pydantic.readthedocs.io/en/stable/index.html>`_
* `enum_tools.autoenum - A Sphinx directive for documenting Enums in Python <https://enum-tools.readthedocs.io/en/latest/api/autoenum.html>`_

Development
===========

Use one of the following options to build the documentation:

- Run the live reload server with Python directly:

.. code-block:: bash

    poetry run python docs/docs_livereload.py

- Or use `Docker <https://www.docker.com/>`_:

.. code-block:: bash

    docker compose up --build docs

Both will run a webserver listing on http://localhost:5500 and will automatically rebuild the documentation (and
reloading the website inside your browser) if a file in docs or newtron_cdc directory changes.

Build
=====

To finally build the documentation run the following command inside the docs directory:

.. code-block:: bash

    make html

Or on Windows:

.. code-block:: bash

    ./make.bat html
