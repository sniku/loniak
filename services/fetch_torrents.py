#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime

from sources import get_module
from clients import AVAILABLE_CLIENTS
from config import settings
from loniak_exceptions import ConfigurationError
from utils.json_utils import read_loniak_data_file, write_loniak_data_file
from utils.matching import publication_date_match, substring_match

def fetch_torrents():

    if settings.CLIENT not in AVAILABLE_CLIENTS:
        raise ConfigurationError(u'"{0}" is not a valid Loniak client. Choose: {1}'.format(settings.CLIENT, ", ".join(AVAILABLE_CLIENTS)))
    client = AVAILABLE_CLIENTS.get(settings.CLIENT)()

    data = read_loniak_data_file(settings.DATA_FILE)
    already_downloaded = data['already_downloaded']

    for source in settings.sources:
        module = get_module(source['type'])

        if module:
            torrents = module.extract_torrent_urls(source['url'])

            # filter the torrents with the strings
            if 'match' in source and source['match']:
                torrents = filter(substring_match(source['match']), torrents)

            # filter the torrents with the publication date
            if 'published_days_ago' in source and source['published_days_ago'].isdigit():
                torrents = filter(publication_date_match(source['published_days_ago']), torrents)

            for t in torrents:
                if t.guid not in already_downloaded:
                    client.consume_torrent(t)
                    already_downloaded.append(t.guid)
                else:
                    print datetime.datetime.now(), t.guid, "was already added to download list. Skipping."


        else:
            print u"Loniak is not supporting", source['type'], u'yet. '\
                  u"Supported source types: HTML, RSS" #, ", ".join(get_available_modules())
    write_loniak_data_file(settings.DATA_FILE, data)


if __name__ == "__main__":
    fetch_torrents()
