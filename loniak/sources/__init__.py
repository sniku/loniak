
# This module implements all the source types.
# Source type is a "way of retrieving the torrent URLs or magnet links"
# You could implement a Source that fetches .torrent files from a folder on your HDD, internet RSS feed, HTML webpage.
# Currently only RSS type is fully implemented.

from loniak.sources.rss import RssSource
from loniak.sources.html import HtmlSource

ALL_MODULES = [RssSource()] # TODO: implement other source types

def get_module(name):
    modules = dict([(cls.__unicode__(), cls) for cls in get_available_modules()])
    return modules.get(name, None)

def get_available_modules():
    return ALL_MODULES

