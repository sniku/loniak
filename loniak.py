#!/usr/bin/python
# -*- coding: utf-8 -*-
from sources import get_module
from clients import AVAILABLE_CLIENTS
from config import settings
from loniak_exceptions import ConfigurationError
INTERVAL = 30  # seconds

# WATCH_DIR = '/media/cryptex/www_cryptex/loniak/dump_point'
# INCOMPLEDE_DIR = '/media/cryptex/www_cryptex/loniak/complete'
# COMPLEDE_DIR = '/media/cryptex/www_cryptex/loniak/complete'
# LOG_PATH = '/media/cryptex/www_cryptex/loniak/loniak.log'
# CONFIG = '/etc/loniak.conf'

DOWNLOADED_LOG = '/media/cryptex/www_cryptex/loniak/downloaded.log'

SOURCES = [
    ('RSS',  'http://www.ezrss.it/feed/'),
    # ('HTML', 'http://eztv.it/'),
    # ('RSS',  'http://rss.thepiratebay.sx/205')
]
ALREADY_DOWNLOADED = []



def run():

    if settings.CLIENT not in AVAILABLE_CLIENTS:
        raise ConfigurationError(u'"{0}" is not a valid Loniak client. Choose one of {1}'.format(settings.CLIENT, ", ".join(AVAILABLE_CLIENTS)))
    client = AVAILABLE_CLIENTS.get(settings.CLIENT)()

    for source_type, url in SOURCES:

        module = get_module(source_type)

        if module:

            torrents = module.extract_torrent_urls(url)

            for t in torrents:
                if t.guid not in ALREADY_DOWNLOADED:
                    client.consume_torrent(t)



            # fetch URLs
            print 'Fetching urls'
            pass
        else:
            print u"Loniak is not supporting", source_type, u'yet. '\
                  u"Supported source types: HTML, RSS" #, ", ".join(get_available_modules())



if __name__ == '__main__':
    run()


