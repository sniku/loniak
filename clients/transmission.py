from clients.base import ClientBase

class TransmissionClient(ClientBase):

    def consume_torrent(self, torrent):
        print "consuming", torrent
        #/usr/bin/transmission-remote --add "$1"

        pass
