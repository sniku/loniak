
class UrlMissing(Exception):
    pass

    # def __init__(self, path):
    #     self.path = path
    #
    #
    # def __repr__(self):
    #     return u'"%s" is not a correct torrent file. Check the link/path and try again.'%self.path
    #

class ConfigurationError(Exception):
    pass

class SourceNotAvailable(Exception):
    pass