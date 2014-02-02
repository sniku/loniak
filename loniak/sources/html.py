from loniak.sources.base import SourceBase


class HtmlSource(SourceBase):
    def __init__(self):
        raise NotImplementedError

    def __unicode__(self):
        return 'HTML'
