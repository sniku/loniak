

class SourceBase(object):

    def extract_torrent_urls(self, source_url):
        """
        Must be overriden by child class.
        This function must return list of urls.
        """
        raise NotImplementedError

