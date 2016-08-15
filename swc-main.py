"""Test script to check for required functionality.

Execute this code at the command line by typing:

  python swc-main.py

Run the script and follow the instructions it prints at the end.

This script requires at least Python 2.6.  It will first check for the
existing version of python installed on your system, and will proceed further
only if you have at least Python 2.6.

By default, this script will test for all the dependencies your
instructor thinks you need.  If you want to test for a different set
of packages, you can list them on the command line.  For example:

  python swc-main.py git virtual-editor

    This is useful if the original test told you to install a more recent
    version of a particular dependency, and you just want to re-test that
    dependency.
    """
# Some details about the implementation:

# CHECKS list stores a list of the dependencies which are to be checked in
# the current workshop.

# In the "__name__ == '__main__'" block, we launch all the checks with
# check() function of requirements_check.py, which prints information about the tests as they run
# and details about the failures after the tests complete. In case of
# failure, the functions print_system_info() and print_suggestions()
# are called after this, where the former prints information about the
# user's system for debugging purposes while the latter prints some
# suggestions to follow.


import requirements_check
from requirements_check import InvalidCheck, CHECKER
import api as API
import optparse as _optparse
import sys as _sys

HOST = "installation.software-carpentry.org"

# Comment out any entries you don't need
CHECKS = [
    # Shell
    'virtual-shell',
    # Editors
    'virtual-editor',
    # Browsers
    'virtual-browser',
    # Version control
    'git',
    'hg',              # Command line tool
    # 'mercurial',       # Python package
    'EasyMercurial',
    # Build tools and packaging
    'make',
    'virtual-pypi-installer',
    'setuptools',
    # 'xcode',
    # Testing
    'nosetests',       # Command line tool
    'nose',            # Python package
    'py.test',         # Command line tool
    'pytest',          # Python package
    # SQL
    'sqlite3',         # Command line tool
    'sqlite3-python',  # Python package
    # Python
    'python',
    'ipython',         # Command line tool
    'IPython',         # Python package
    'argparse',        # Useful for utility scripts
    'numpy',
    'scipy',
    'matplotlib',
    'pandas',
    # 'sympy',
    # 'Cython',
    # 'networkx',
    # 'mayavi.mlab',
]


def python_version_check():
    print("Checking for python version...")
    if _sys.version_info < (2, 6):
        print('check for Python version (python):')
        print('outdated version of Python: ' + _sys.version)
        return False
    return True

if __name__ == '__main__':

    if python_version_check():
        print('Passed')
    else:
        print('Failed')
        print('Install the newest version from https://www.python.org/downloads/ or ask instructors for help')
        _sys.exit(1)

    parser = _optparse.OptionParser(usage='%prog [options] [check...]')
    epilog = __doc__
    parser.format_epilog = lambda formatter: '\n' + epilog
    parser.add_option(
        '-v', '--verbose', action='store_true',
        help=('print additional information to help troubleshoot '
              'installation issues'))
    parser.add_option(
        '-H', '--host', action='store', type="string",
        help=('Change the server to which the data will be sent'), dest="host_name")
    parser.add_option(
        '-n', '--no_reporting', action='store_true',
        help=('Turn off sending the data to server'))
    options, args = parser.parse_args()
    try:
        if not args:
            args = CHECKS
        passed, successes_list, failures_list = requirements_check.check(args)
        """Check whether host name is specified as a command line argument"""
        if options.host_name:
            HOST = options.host_name
        """Check whether sending data to server is turned off using
           command line argument"""
        if options.no_reporting is None:
            API.submit(successes_list, failures_list, HOST)
    except InvalidCheck as e:
        print("I don't know how to check for {0!r}".format(e.check))
        print('I do know how to check for:')
        for key, checker in sorted(CHECKER.items()):
            if checker.long_name != checker.name:
                print('  {0} {1}({2})'.format(
                    key, ' ' * (20 - len(key)), checker.long_name))
            else:
                print('  {0}'.format(key))
        _sys.exit(1)
    if not passed:
        if options.verbose:
            print()
            requirements_check.print_system_info()
            requirements_check.print_suggestions(instructor_fallback=True)
        _sys.exit(1)
