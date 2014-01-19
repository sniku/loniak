#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Loniak.

Usage:
  loniak fetch_torrents
  loniak stop
  loniak finished_downloading <guid>

"""
from docopt import docopt
from services import fetch_torrents
from services.notify import notify

if __name__ == "__main__":
    args = docopt(__doc__, version='Loniak 0.1')

    if args['fetch_torrents']:
        fetch_torrents()
    elif args['finished_downloading']:
        notify(args['<guid>'])

