import os

from loniak_exceptions import UrlMissing

class Torrent(object):
    """
    This class represents a single torrent object.
    It can be a magnet-link torrent, or URL to .torrent file or an actual .torrent file.
    """

    type = None
    torrent_locations = [] # a list of torrent locations [URL, filepath, magnetlink]
    title = ''
    description = ''
    publication_date = ''
    guid = None


    # link = item.link.text
    # title = item.link.title
    # guid = item.link.guid
    # torrent = item.torrent
    # filename = torrent.fileName.text if torrent else None
    # magnetURI = torrent.magnetURI.text if torrent else None

    def __init__(self, torrent_locations, title=None, guid=None):

        self.torrent_locations = torrent_locations
        self.title = title
        self.guid = guid
        #
        # if self.path.startswith('magnet'):
        #     self.type = 'MAGNET'
        # elif self.path.startswith('http'):
        #     self.type = 'TORRENT'
        # elif os.path.exists(self.path):
        #     self.type = 'FILE'
        # else:
        #     raise UrlMissing(self.path)


    def __repr__(self):
        return  self.title