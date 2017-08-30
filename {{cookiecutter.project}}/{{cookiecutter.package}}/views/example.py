from tet.response import Response
from tet.view import view_config, ServiceViews
from tet.services import autowired

from sqlalchemy.exc import DBAPIError
from sqlalchemy.orm import Session

from ..models import MyModel

class ExampleViews(ServiceViews):
    db_session = autowired(Session)

    @view_config(route_name='home',
                 renderer='{{cookiecutter.package}}:templates/index.tk')
    def my_view(self):
        try:
            one = (self.db_session.query(MyModel)
                   .filter(MyModel.name == 'one').first())
        except DBAPIError:
            return Response(conn_err_msg,
                            content_type=str('text/plain'),
                            status_int=500)

        return {'one': one, 'project': '{{cookiecutter.project}}'}

conn_err_msg = """\
Tet is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to initialize the database using the default
    migration: "alembic upgrade head" to initialize your database
    tables.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the application to
try it again.
"""

