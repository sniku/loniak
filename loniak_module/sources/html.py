import urllib2
from loniak_module.sources.base import SourceBase
from BeautifulSoup import BeautifulSoup
import re
from loniak_module.tr.torrent import Torrent


class HtmlSource(SourceBase):

    def __unicode__(self):
        return 'HTML'


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


        # we are assuming that the HTML webpage contains a table and each torrent link is in its own row.
        # This is true for 90% of the torrent websites.
        soup = BeautifulSoup(data)
        tables = soup.findAll("table")
        torrents = []

        for table in tables:
            rows = table.findAll('tr')
            for row in rows:
                # search for torrent links.
                # we assume that all links that start with "magnet:" or end with ".torrent" are torrent urls
                a_torrents = row.findAll('a', href=re.compile('^magnet|\.torrent$'))
                torrent_urls = []
                title = ''
                description = ''

                for a_torrent in a_torrents:
                    if a_torrent.text:
                        title = a_torrent.text
                    href = guid = a_torrent['href']
                    torrent_urls.append(href)


                if torrent_urls:
                    """
                    So, we don't have a title yet. Let's try to be smart and use some bloody heuristics.
                    """
                    if title == '':
                        all_a = row.findAll('a')
                        for a in all_a:
                            if a.text in a['title']:
                                title = a.text
                                break

                    t = Torrent(torrent_urls, title=title, guid=torrent_urls[0], description=description)
                    torrents.append(t)
                else:
                    # Something went wrong with row parsing and we didn't find any torrents
                    pass


        return torrents
