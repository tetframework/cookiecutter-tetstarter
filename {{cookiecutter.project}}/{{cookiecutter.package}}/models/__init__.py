from pyramid.config import Configurator

# include the models first so that we can safely call configure_mappers
from .meta import Base
from .example import MyModel


def includeme(config: Configurator):
    # include the simple sqlalchemy extension
    config.include('tet.sqlalchemy.simple')

    # set up sqlalchemy using defaults
    config.setup_sqlalchemy()

