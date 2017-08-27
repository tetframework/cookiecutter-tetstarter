from tet.config import application_factory

@application_factory
def main(config: 'tet.config.Configurator'):
    config.scan('{{cookiecutter.package}}')

    engine = engine_from_config(config.registry.settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

{% if cookiecutter.persistence == 'sqlalchemy' -%}
    config.include('.models')
{% endif %}

    config.add_static_view('static', '{{cookiecutter.package}}:static', cache_max_age=3600)
    config.add_route('home', '/')

