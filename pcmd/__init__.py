# -*- coding: utf-8 -*-
#
# File: __init__.py
#
# Copyright (c) ramonski
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

__author__ = 'Ramon Bartl <ramon_bartl@yahoo.de>'
__docformat__ = 'plaintext'

import os
import argparse
import ConfigParser
import appscript

TERMINAL_ENV = "PTERM"
TERMINAL_APP = "Terminal"
INIFILE = ".p.ini"


def terminal():
    terminal = os.environ.get(TERMINAL_ENV, TERMINAL_APP)
    app = appscript.app(terminal)
    return app


def active_terminal_window():
    app = terminal()
    for window in app.windows():
        if not window.frontmost():
            continue
        return window


def active_terminal_tab():
    win = active_terminal_window()
    return win.selected_tab()


def do_script(cmd):
    tab = active_terminal_tab()
    return tab.do_script(cmd, in_=tab)


def main():
    parser = argparse.ArgumentParser(description='Runs a shell command in the parent shell')

    parser.add_argument('cmd',
                        metavar='COMMAND',
                        type=str,
                        help='Command to execute')

    parser.add_argument('section',
                        metavar='SECTION',
                        type=str,
                        help='Section where the Command is executed')

    args = parser.parse_args()

    config = ConfigParser.ConfigParser()

    # read the config ini
    home = os.environ.get("HOME")
    conf = os.sep.join([home, INIFILE])
    inifile = config.read(conf) # returns an empty list if file not there

    if not inifile:
        msg = "Config not found in: %s\n" % conf
        parser.exit(status=1, message=msg)

    if not config.has_section(args.section):
        msg = "Section %s not in config\n" % args.section
        parser.exit(status=1, message=msg)

    if not config.has_option(args.section, args.cmd):
        msg = "Command %s not in Section %s\n" % (args.cmd,  args.section)
        parser.exit(status=1, message=msg)

    # run the shell command in the parent terminal
    do_script(config.get(args.section, args.cmd))


if __name__ == '__main__':
    main()

# vim: set ft=python ts=4 sw=4 expandtab :
