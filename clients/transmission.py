from clients.base import ClientBase
import os
import subprocess
from config import settings
import datetime

class TransmissionClient(ClientBase):

    def consume_torrent(self, torrent):
        if hasattr(torrent, 'matched'):
            print '{0} consuming {1}, matched: "{2}"'.format(datetime.datetime.now(), torrent, torrent.matched)
        else:
            print "{0} consuming {1}".format(datetime.datetime.now(), torrent)

        transmission_credentials = "{0}:{1}".format(settings.TRANSMISSION_USERNAME, settings.TRANSMISSION_PASSWORD)


        # print torrent, torrent.torrent_locations

        for torrent_link in torrent.torrent_locations:
            proc = subprocess.Popen(["transmission-remote", "-a", torrent_link, '--auth', transmission_credentials],
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            stdout = proc.stdout.read()
            stderr = proc.stderr.read()

            if proc.returncode in [0, None]:
                print datetime.datetime.now(), stdout
            else:
                print datetime.datetime.now(), "Failed to consume the torrent. {0}".format(torrent).strip()
                print datetime.datetime.now(), stdout

