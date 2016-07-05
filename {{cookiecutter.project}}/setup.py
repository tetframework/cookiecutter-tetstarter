import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()


requires = [
    'pyramid',
    'transaction',
    'pyramid_tm',
    'pyramid_debugtoolbar',
    'waitress',
    'tet',
    'pyramid_chameleon',
    {% if cookiecutter.persistence == 'sqlalchemy' -%}
    'zope.sqlalchemy',
    'SQLAlchemy',
    {% endif -%}
]

setup_requires = [
    'setuptools>=17.1',
]

docs_extras = [
    'Sphinx'
]

testing_extras = [
    'nose',
    'coverage',
    'mock',
    'virtualenv'
]

i18n_extras = [
    'Babel',
    'transifex-client',
    'lingua<2.0'
]


setup(
    name='{{cookiecutter.project}}',
    version='0.0',
    description='{{cookiecutter.project}}',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
      "Programming Language :: Python",
      "Framework :: Pyramid",
      "Programming Language :: Python :: 3.4",
      "Programming Language :: Python :: 3.5",
      "Programming Language :: Python :: 3 :: Only",
      "Topic :: Internet :: WWW/HTTP",
      "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      ],
    author='',
    author_email='',
    url='',
    keywords='web wsgi tet pyramid',
    packages=find_packages(),
    include_package_data=True,
    license="BSD",
    zip_safe=False,
    test_suite='{{cookiecutter.package}}',
    install_requires=requires,
    message_extractors={
        '{{ cookiecutter.package }}': [
            ('**.py', 'python', None),  # babel extractor supports plurals
            ('**.pt', 'lingua_xml', None),
        ],
    },
    extras_require = {
        'testing':testing_extras,
        'docs':docs_extras,
        'i18n':i18n_extras,
    },
    entry_points="""\
    [paste.app_factory]
    main = {{cookiecutter.package}}:main
    {% if cookiecutter.persistence == 'sqlalchemy' -%}[console_scripts]
    initialize_{{cookiecutter.package}}_db = {{cookiecutter.package}}.scripts.initializedb:main
    {% endif -%}
    """,
)
