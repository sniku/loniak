


class ClientBase(object):
    '''
    This is the base class/interface that should be implemented for each torrent Client supported by loniak.
    '''

    def consume_torrent(self, torrent):
        pass
