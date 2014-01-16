

class SourceBase(object):

    # @staticmethod
    def extract_torrent_urls(self, source_url):
        """
        Must be overriden by child class.
        This function must return list of urls.
        """
        raise NotImplementedError



    def fetch_torrents(self):
        pass