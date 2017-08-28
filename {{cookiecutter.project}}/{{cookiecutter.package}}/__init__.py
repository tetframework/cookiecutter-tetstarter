from tet.config import application_factory

@application_factory
def main(config: 'tet.config.Configurator'):
    """
    This function is the factory for the Tet application
    """

    config.include('.models')
    config.include('.routes')
    config.scan('{{cookiecutter.package}}')
