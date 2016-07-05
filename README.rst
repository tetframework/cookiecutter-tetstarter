===========================================
Tet starter Cookie Cutter Template - README
===========================================

Cookiecutter template for a Tet application. See https://github.com/audreyr/cookiecutter.

* Choice of either SQLAlchemy or no storage engine
* Virtualenv automatically created and setup in development mode
* Free software: BSD license
* Travis-CI_: Ready for Travis Continuous Integration testing
* Tox_ testing: Setup to easily test for Python 3.4 and 3.5
* Sphinx_ docs: Documentation ready for generation with, for example, ReadTheDocs_

Usage
-----

Generate a Pyramid project::

    cookiecutter https://github.com/tetframework/cookiecutter-tetstarter

Then:

* cd to project name given in the last cookiecutter question
* Run bin/pserve development.ini

This is a Cookie Cutter templ

- cd <directory containing this file>

- $VENV/bin/python setup.py develop

- $VENV/bin/initialize_{{cookiecutter.project}}_db development.ini

- $VENV/bin/pserve development.ini

