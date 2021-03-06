import urllib2

from loniak_module.sources.base import SourceBase
from loniak_module.tr.torrent import Torrent
try:
    import feedparser
except ImportError:
    from loniak_module.libs import feedparser

try:
    from dateutil import parser
except ImportError:
    from loniak_module.libs.dateutil import parser


class RssSource(SourceBase):

    def __unicode__(self):
        return 'RSS'

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

            torrent_links = set()
            for x in entry['links']:
                if 'type' in x and 'href' in x and x['type'] == 'application/x-bittorrent':
                    torrent_links.add(x['href'])
                elif 'href' in x and x['href'].endswith('.torrent'):
                    torrent_links.add(x['href'])
            if 'link' in entry:
                torrent_links.add(entry['link'])

            if 'magneturi' in entry:
                torrent_links.add(entry['magneturi'])

            try:
                publication_date = parser.parse(entry['published']).replace(tzinfo=None)
            except:
                publication_date = None

            description      = entry['description'] if 'description' in entry else ''
            guid             = entry['id'] if 'id' in entry else torrent_links[0]
            title            = entry['title'] if 'id' in entry else ''

            t = Torrent(torrent_links, title=title, guid=guid, description=description, publication_date=publication_date)
            torrents.append(t)

        return torrents


