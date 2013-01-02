#! /usr/bin/env python
"""A thin replacement for ETSProjectTools. Performs checkout, update, install,
build, etc, of all actively maintained ETS packages, and allows arbitrary
shell commands to be run on all packages.
"""

import sys
import subprocess

usage = """\
Usage: ets -h | --help | co | COMMAND [args] | ALIAS [args]
   -h, --help  Print this message.

   co          Check out the entire ETS repository into the current working
               directory, each actively maintained package placed in its own
               sub-directory.

   COMMAND     Run this shell command, with any following arguments, inside
               each package's sub-directory. If any command arguments must be
               quoted, you may need to use nested quotes, depending on the
               quote handling in your shell. For example:
                  ets svn ci "'check-in comment for all packages'"

   ALIAS       Each alias is shorthand for a shell command with arguments.
               The available aliases are pre-defined by this script, not by
               the user. Any alias may be followed by optional additional
               arguments.


   The available aliases and their equivalent commands are:%s

   Examples:
      Fresh install all packages from trunk:
         mkdir ETS
         cd ETS
         ets co
         ets develop

      Update all packages from trunk:
         ets up

   The ETS packages referenced, in order of processing, are:\n%s"""

aliases = """\
      diff     svn diff
      rev      svn revert
      status   svn status
      up       svn update
      setup    python setup.py
      build    python setup.py build
      bdist    python setup.py bdist
      develop  python setup.py develop
      sdist    python setup.py sdist"""

"""\
======================================================================
ETS installation dependencies (documentation only).
Derived from ets_dependends.log, holding the output of ets_depends.py.
Dependent packages are listed below and to the right of their dependencies.
======================================================================
EnthoughtBase & Traits
    CodeTools  (depends on Traits only)
    SciMath
        BlockCanvas*
    TraitsGUI
        ETSDevTools
            BlocCanvas*
        TraitsBackendQt
        TraitsBackendWX
        Enable
            Chaco
               BlockCanvas*
        AppTools
            Mayavi
            EnvisageCore
                EnvisagePlugins
            BlockCanvas*

Notes:
1.  * BlockCanvas's multiple dependencies are listed individually.
2. This string is for documentation only. Unlike the ets_package_names string
   below, this  is not used programatically. However, string ets_package_names
   *is* manually derived from the info in this string.
3. This string does not list ETS run-time, nor any non-ETS, dependencies.
4. To avoid clutter, this string does not list redundant dependencies. For
   example, it does not list Traits or EnthoughtBase dependencies for packages
   which depend on TraitsGUI, because TraitsGUI itself depends on both of these.
"""


ets_package_names = """\
      EnthoughtBase      Traits             CodeTools
      TraitsGUI          ETSDevTools        SciMath
      TraitsBackendQt    TraitsBackendWX    Enable
      AppTools           EnvisageCore       EnvisagePlugins
      Chaco              Mayavi             GraphCanvas
      BlockCanvas"""

ets_url = "https://svn.enthought.com/svn/enthought/%s/trunk"

alias_dict = {}
for line in aliases.split('\n'):
    tokens = line.split()
    if tokens:
         alias_dict[tokens[0]] = tokens[1:]


def main():
    if len(sys.argv) < 2 or sys.argv[1].startswith('-'):
        print usage % (aliases, ets_package_names)
        return

    arg1 = sys.argv[1]
    checkout = bool(arg1 == 'co')

    if not checkout:
        if arg1 in alias_dict:
            cmd = alias_dict[arg1] + sys.argv[2:]
            if cmd[0] == 'python':
                cmd[0] = sys.executable
        else:
            cmd = sys.argv[1:]

    for ets_pkg_name in ets_package_names.split():
        if checkout:
            print "Checking out package %s" % ets_pkg_name
            pkg_url = ets_url % ets_pkg_name
            subprocess.check_call(['svn', 'co', pkg_url, ets_pkg_name])
        else:
            print "Running command %r in package %s" % (cmd, ets_pkg_name)
            try:
                subprocess.check_call(cmd, cwd=ets_pkg_name)
            except (OSError, subprocess.CalledProcessError), detail:
                print "   Error running command in package %s:\n   %s" % (
                                      ets_pkg_name, detail)
                raw_input("   Press enter to process remaining packages.")


if __name__ == "__main__":
    main()
