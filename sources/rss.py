import urllib2
from BeautifulSoup import BeautifulSoup

from sources.base import SourceBase
from tr.torrent import Torrent


class RssSource(SourceBase):

    def __unicode__(self):
        return 'RSS'

    def extract_torrent_urls(self, source_url):
        """
        TODO: try/except on url fetching
        TODO: try/except on bs parsing
        """
        urls = []
        response = urllib2.urlopen(source_url)
        headers = response.info()
        data = response.read()

        soup = BeautifulSoup(data)

        # we are assuming that torrents are inside the "<item>" elements

        items = soup.findAll("item")

        torrents = []

        for item in items:

            # skip elements without link
            if not item.has_key('link'):
                continue

            t = Torrent(item.link)
            if item.has_key('title'):
                t.title = item.title

            # TODO: add other attributes
            torrents.append(t)

        return torrents











