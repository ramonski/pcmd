# -*- coding: utf-8 -*-
#
# File: config.py
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
import ConfigParser

INIFILE = ".p.ini"

def get_config():
    home = os.environ.get("HOME")
    return os.sep.join([home, INIFILE])

def is_config_there():
    return os.path.exists(get_config())

def get_parser():
    parser = ConfigParser.SafeConfigParser()
    parser.read(get_config())
    return parser

def sections():
    parser = get_parser()
    return parser.sections()

def options():
    parser = get_parser()
    return [parser.options(s) for s in parser.sections()]

def _sections():
    for section in sorted(sections()):
        print section

def _options():
    out = []
    _ = [out.extend(o) for o in options()]
    for option in out:
        print option

# vim: set ft=python ts=4 sw=4 expandtab :
