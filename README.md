For learners
============

This directory contains script for testing your machine to make sure
you have the software you'll need for your workshop installed.  See
the comments at the head of each script for more details, but you'll
basically want to see something like:

    $ python swc-main.py
    Checking for python version...
    Passed
    check command line shell (virtual-shell)... pass
    ...
    Successes:

    virtual-shell Bourne Again Shell (bash) 4.2.37
    …

If you see something like:

    $ python swc-main.py
    Checking for python version...
    Passed
    check virtual-shell...  fail
    …
    check for command line shell (virtual-shell) failed:
      command line shell (virtual-shell) requires at least one of the following dependencies
      For instructions on installing an up-to-date version, see
      http://software-carpentry.org/setup/
      causes:
      check for Bourne Again Shell (bash) failed:
        could not find 'bash' executable for Bourne Again Shell (bash)
        For instructions on installing an up-to-date version, see
        http://software-carpentry.org/setup/
    …

follow the suggestions to try and install any missing software.  For
additional troubleshooting information, you can use the `--verbose`
option:

    $ python swc-main.py --verbose
    check virtual-shell...  fail
    …
    ==================
    System information
    ==================
    os.name            : posix
    …

For instructors
===============

`swc-main.py` first checks that the students have a recent enough 
version of Python installed that they'll be able to parse
`swc-main.py` completely.  If python version is found to be at least 2.6,
then it checks for a list of dependencies and prints error messages if a
package is not installed, or if the installed version is not current
enough.  By default, the script checks for pretty much anything that
has ever been used at a Software Carpentry workshop, which is probably
not what you want for your particular workshop.

Before your workshop, you should go through
`swc-main.py` and comment any dependencies you don't
need out of the `CHECKS` list.  You might also want to skim through
the minimum version numbers listed where particular dependencies are
defined (e.g. `('git', 'Git', (1, 7, 0), None)`).  For the most part,
fairly conservative values have been selected, so students with modern
machines should be fine.  If your workshop has stricter version
requirements, feel free to bump them accordingly.

Similarly, the virtual dependencies can be satisfied by any of several
packages.  If you don't want to support a particular package (e.g. if
you have no Emacs experience and don't want to be responsible for
students who show up with Emacs as their only editor), you can comment
out that particular `or_dependency`.

Finally, don't forget to post your modified scripts somewhere where
your students can download them!
