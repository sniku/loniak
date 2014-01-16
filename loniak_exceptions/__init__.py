
class URL_MISSING(Exception):

    def __init__(self, path):
        self.path = path


    def __repr__(self):
        return u'"%s" is not a correct torrent file. Check the link/path and try again.'%self.path


class ConfigurationError(Exception):

    def __init__(self, error):
        self.error = error


    def __repr__(self):
        return self.error


