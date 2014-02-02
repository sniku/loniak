#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Loniak.

Usage:
  loniak fetch_torrents
  loniak stop
  loniak finished_downloading <guid>

"""
from loniak_module.services import notify
from loniak_module.services import fetch_torrents

try:
    from docopt import docopt
except ImportError:
    from loniak_module.libs import docopt



if __name__ == "__main__":
    args = docopt(__doc__, version='Loniak 0.1')

    if args['fetch_torrents']:
        fetch_torrents()
    elif args['finished_downloading']:
        notify(args['<guid>'])

