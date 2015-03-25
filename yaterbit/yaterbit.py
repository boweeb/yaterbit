#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''yaterbit

Usage:
  yaterbit ship new <name>...
  yaterbit ship <name> move <x> <y> [--speed=<kn>]
  yaterbit ship shoot <x> <y>
  yaterbit mine (set|remove) <x> <y> [--moored|--drifting]
  yaterbit -h | --help
  yaterbit --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --speed=<kn>  Speed in knots [default: 10].
  --moored      Moored (anchored) mine.
  --drifting    Drifting mine.
'''

from __future__ import unicode_literals, print_function
from docopt import docopt

__version__ = "0.5"
__author__ = "Jesse Butcher"
__license__ = "MIT"


def main():
    '''Main entry point for the yaterbit CLI.'''
    args = docopt(__doc__, version=__version__)
    print(args)

if __name__ == '__main__':
    main()