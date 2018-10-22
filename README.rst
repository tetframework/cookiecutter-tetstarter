===========================================
Tet starter Cookie Cutter Template - README
===========================================

Cookiecutter template for a Tet application. See https://github.com/audreyr/cookiecutter.

* Choice of either SQLAlchemy or no storage engine
* Virtualenv automatically created and setup in development mode
* Free software: BSD license
* Travis-CI_: Ready for Travis Continuous Integration testing
* Tox_ testing: Setup to easily test for Python 3.5, 3.6, 3.7
* Sphinx_ docs: Documentation ready for generation with, for 
  example, ReadTheDocs_

Usage
-----

Generate a Tet Starter project::

    cookiecutter https://github.com/tetframework/cookiecutter-tetstarter

Then:

- If you chose to create a database, you can install it now

- ``cd <directory containing this file>``

- Create a Python 3.5+ virtual environment; hereinafter the directory is
  referred to as ``$VENV``.

- ``$VENV/bin/pip install -e .``

- Migrate the database to the initial state with 
  ``$VENV/bin/alembic -n dev upgrade head``

  Alternatively you might want to forgo the database creation now, remove the
  ``migrations/versions/INIT_initial.py``, edit the models and create a new
  initial migration with ``alembic -n dev revision --autogenerate``.

- ``$VENV/bin/pserve development.ini --reload``

