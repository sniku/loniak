#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Loniak.

Usage:
  loniak fetch_torrents
  loniak stop
  loniak finished_downloading <guid>

"""
from loniak.services import notify
from loniak.services import fetch_torrents

try:
    from docopt import docopt
except ImportError:
    from loniak.libs import docopt



if __name__ == "__main__":
    args = docopt(__doc__, version='Loniak 0.1')

    if args['fetch_torrents']:
        fetch_torrents()
    elif args['finished_downloading']:
        notify(args['<guid>'])

