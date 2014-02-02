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

    def __init__(self, torrent_locations, title='', guid='', publication_date=None, description=''):

        self.torrent_locations = torrent_locations
        self.title = title
        self.guid = guid
        self.description = description
        self.publication_date = publication_date


    def __repr__(self):
        return  self.title