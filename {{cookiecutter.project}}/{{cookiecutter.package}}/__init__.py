from tet.config import application_factory
{% if cookiecutter.persistence == 'sqlalchemy' -%}
from sqlalchemy import engine_from_config

from .models import DBSession, Base
{% endif %}

@application_factory
def main(config: 'tet.config.Configurator'):
    config.scan('{{cookiecutter.package}}')

    engine = engine_from_config(config.registry.settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    config.add_static_view('static', '{{cookiecutter.package}}:static', cache_max_age=3600)
    config.add_route('home', '/')
