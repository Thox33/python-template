.. _developer-repository:

**********
Repository
**********

The repository branching strategy is based on the `GitFlow` model. The main
branches are:

* ``main``
* ``develop``
* ``feature-*``

Branching
=========

The ``main`` branch is the main branch of the repository. It contains the
latest stable version of the code. The ``develop`` branch is the main branch
for development. All new features are merged into this branch. The
``feature-*`` branches are used for developing new features. They are branched
off the ``develop`` branch and merged back into it when the feature is
complete.

Releasing
=========

Each ``feature-*`` branch releases new `alpha` versions of the code. When a
feature is complete, the ``feature-*`` branch is merged into the ``develop``
branch. This will create a new `rc` version and release this. When the
``develop`` branch is ready for a new release, it is merged into the ``main``
branch. This then will create a new stable release version of the code.
