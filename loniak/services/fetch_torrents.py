#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
import datetime

from loniak.sources import get_module
from loniak.clients import AVAILABLE_CLIENTS
from loniak.config import settings
from loniak.loniak_exceptions import ConfigurationError
from loniak.utils.json_utils import read_loniak_data_file, write_loniak_data_file
from loniak.utils.matching import publication_date_match, substring_match

def fetch_torrents():

    if settings.CLIENT not in AVAILABLE_CLIENTS:
        raise ConfigurationError(u'"{0}" is not a valid Loniak client. Choose: {1}'.format(settings.CLIENT, ", ".join(AVAILABLE_CLIENTS)))
    client = AVAILABLE_CLIENTS.get(settings.CLIENT)()

    data = read_loniak_data_file(settings.DATA_FILE)
    already_downloaded = data['already_downloaded']

    for source in settings.sources:
        print('\n{0} fetching {1} {2}'.format(datetime.datetime.now(), source['type'], source['source_name']))
        module = get_module(source['type'])


        if module:
            for url in source['url']:
                torrents = module.extract_torrent_urls(url)

                # filter the torrents with the "match" and "exclude" clauses
                torrents = filter(substring_match(source['match'], source['exclude']), torrents)

                # filter the torrents with the publication date
                if 'published_days_ago' in source and source['published_days_ago'].isdigit():
                    torrents = filter(publication_date_match(source['published_days_ago']), torrents)

                for t in torrents:
                    if t.guid not in already_downloaded:
                        client.consume_torrent(t)
                        already_downloaded.append(t.guid)
                    else:
                        print("{0} {1} was already added to download list. Skipping.".format(datetime.datetime.now(), t.guid))


        else:
            print(u"Loniak is not supporting yet. Supported source types: HTML, RSS".format(source['type']))
    write_loniak_data_file(settings.DATA_FILE, data)


if __name__ == "__main__":
    fetch_torrents()
