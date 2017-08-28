{{ cookiecutter.project }}
{% for _ in cookiecutter.project %}={% endfor %}

Getting Started
---------------

- cd <directory containing this file>

- $VENV/bin/python -mpip install -e .

- $VENV/bin/alembic upgrade head

- $VENV/bin/pserve development.ini

