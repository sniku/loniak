import urllib2

from loniak_module.sources.base import SourceBase
from loniak_module.sources import HtmlSource
from loniak_module.tr.torrent import Torrent

try:
    import feedparser
except ImportError:
    from loniak_module.libs import feedparser

try:
    from dateutil import parser
except ImportError:
    from loniak_module.libs.dateutil import parser

import re
import urllib


class IMDBSource(SourceBase):
    IMDB_TITLE_REGEX = r"(?P<title>.+?)\((?P<year>\d{4})(?P<type>.*)\)"

    def __unicode__(self):
        return 'IMDB'

    def extract_torrent_urls(self, source_url):
        """
        TODO: try/except on url fetching
        TODO: try/except on bs parsing
        """
        try:
            response = urllib2.urlopen(source_url)
            headers = response.info()
            data = response.read()
        except urllib2.URLError:
            print "{0} is temporarily unavailable. No torrents downloaded.".format(source_url)
            return []


        root = feedparser.parse(data)

        torrents = []
        for entry in root['entries']:
            title = entry['title']
            re.match(r"\(\d{4}.*?\)", title)
            m = re.match(self.IMDB_TITLE_REGEX, title)
            if m:
                m_vars = m.groupdict()
                imdb_title = m_vars.get('title').strip()
                imdb_year  = m_vars.get('year').strip()
                imdb_type  = m_vars.get('type').strip()

                # print imdb_title, imdb_year, imdb_type

                # build ThePiratebayUrl
                TPB_SEARCH_BEST_SEED_URL = "https://thepiratebay.se/search/{0}/0/7/200"
                TPB_SEARCH_LATEST_URL    = "https://thepiratebay.se/search/{0}/0/3/0"

                search_phrase = urllib.quote_plus(u" ".join([imdb_title, imdb_year]).encode('utf8'))
                if 'tv' in imdb_title.lower():
                    tpb_url = TPB_SEARCH_LATEST_URL.format(search_phrase)
                else:
                    tpb_url = TPB_SEARCH_BEST_SEED_URL.format(search_phrase)


                html_source = HtmlSource()
                found_torrents = html_source.extract_torrent_urls(tpb_url)

                # let's just grab the first two from top.
                # We don't need to download all of them.

                torrents.extend(found_torrents[:2])

            else:
                pass

        return torrents









