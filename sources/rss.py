import urllib2

from sources.base import SourceBase
from tr.torrent import Torrent
try:
    import feedparser
except ImportError:
    from libs import feedparser

try:
    from dateutil import parser
except ImportError:
    from libs.dateutil import parser


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
            # for k, v in entry.iteritems():
            #     print k, '\t', v
            # print "\n"

            torrent_links = [x['href'] for x in entry['links'] if 'type' in x and x['type'] == 'application/x-bittorrent']
            if 'magneturi' in entry:
                torrent_links.append(entry['magneturi'])

            publication_date =  parser.parse(entry['published']).replace(tzinfo=None)

            t = Torrent(torrent_links, title=entry['title'], guid=entry['id'], description=entry['description'], publication_date=publication_date)
            torrents.append(t)
        return torrents

'''
summary_detail 	    {'base': u'', 'type': u'text/html', 'value': u'Show Name: Dogs Their Secret Lives Updated 2014; Episode Title: N/A; Season: 1; Episode: 2', 'language': None}
published_parsed 	time.struct_time(tm_year=2014, tm_mon=1, tm_mday=17, tm_hour=20, tm_min=59, tm_sec=40, tm_wday=4, tm_yday=17, tm_isdst=0)
links               [
                    {'href': u'http://re.zoink.it/52d95617', 'type': u'text/html', 'rel': u'alternate'},
                    {'length': u'689046605', 'href': u'http://re.zoink.it/52d95617', 'type': u'application/x-bittorrent', 'rel': u'enclosure'}
                    ]
tags 	            [{'term': u'TV Show / MV Group Documentaries', 'scheme': u'http://eztv.it/shows/187/mv-group-documentaries/', 'label': None}]
contentlength 	    689046605
title 	            Dogs Their Secret Lives Updated 2014 1x2 [PDTV - MVGROUP]
torrent
comments 	        http://eztv.it/forum/discuss/51369/
summary 	        Show Name: Dogs Their Secret Lives Updated 2014; Episode Title: N/A; Season: 1; Episode: 2
guidislink 	        False
title_detail 	    {'base': u'', 'type': u'text/plain', 'value': u'Dogs Their Secret Lives Updated 2014 1x2 [PDTV - MVGROUP]', 'language': None}
link 	            http://re.zoink.it/52d95617
published 	        Fri, 17 Jan 2014 15:59:40 -0500
filename 	        Dogs.Their.Secret.Lives.Updated.2014.2of2.PDTV.x264-MVGroup.[MVGroup.org].torrent
infohash 	        63FBCDF0F0E9C92EDB8F10666030770EC97C87FB
id 	                http://eztv.it/ep/51369/dogs-their-secret-lives-updated-2014-2of2-pdtv-x264-mvgroup/
magneturi 	        magnet:?xt=urn:btih:MP5434HQ5HES5W4PCBTGAMDXB3EXZB73&dn=Dogs.Their.Secret.Lives.Updated.2014.2of2.PDTV.x264-MVGroup
'''











