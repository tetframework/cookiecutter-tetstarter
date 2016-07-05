import re
import sys


PACKAGE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

package_name = '{{ cookiecutter.package }}'

if not re.match(PACKAGE_REGEX, package_name):
    print('ERROR: {} is not a valid Python module name!'.format(package_name))

    # exits with status 1 to indicate failure
    sys.exit(1)

