#!/usr/bin/python
# -*- coding: utf-8 -*-

from sources import get_module
from clients import AVAILABLE_CLIENTS
from config import settings
from loniak_exceptions import ConfigurationError
from utils.matching import match_regex
ALREADY_DOWNLOADED = []

def fetch_torrents():

    if settings.CLIENT not in AVAILABLE_CLIENTS:
        raise ConfigurationError(u'"{0}" is not a valid Loniak client. Choose: {1}'.format(settings.CLIENT, ", ".join(AVAILABLE_CLIENTS)))
    client = AVAILABLE_CLIENTS.get(settings.CLIENT)()

    for source in settings.sources:
        # print source

        module = get_module(source['type'])

        if module:

            torrents = module.extract_torrent_urls(source['url'])

            # filter the torrents against the regex
            if 'match' in source and source['match']:
                torrents = filter(match_regex(source['match']), torrents)

            for t in torrents:
                if t.guid not in ALREADY_DOWNLOADED:
                    client.consume_torrent(t)
                else:
                    print t.guid, "was already added to download list. Skipping."


        else:
            print u"Loniak is not supporting", source['type'], u'yet. '\
                  u"Supported source types: HTML, RSS" #, ", ".join(get_available_modules())


if __name__ == "__main__":
    fetch_forrents()
