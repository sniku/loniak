import os

from loniak_exceptions import URL_MISSING

class Torrent(object):
    """
    This class represents a single torrent object.
    It can be a magnet-link torrent, or URL to .torrent file or an actual .torrent file.
    """

    type = None
    path = None # either URL or filesystem path
    title = ''
    description = ''
    publication_date = ''
    guid = None

    def __init__(self, torrent_location):

        self.path = torrent_location

        if torrent_location.startswith('magnet'):
            self.type = 'MAGNET'
        elif torrent_location.startswith('http'):
            self.type = 'TORRENT'
        elif os.path.exists(torrent_location):
            self.type = 'FILE'
        else:
            raise URL_MISSING(torrent_location)


    def __repr__(self):
        return  self.title or self.path