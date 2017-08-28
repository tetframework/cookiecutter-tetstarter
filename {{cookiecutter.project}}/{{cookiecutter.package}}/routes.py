def includeme(config):
    config.add_static_view('static', '{{cookiecutter.package}}:static', cache_max_age=3600)
    config.add_route('home', '/')
