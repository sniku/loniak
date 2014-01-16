from sources.base import SourceBase


class HtmlSource(SourceBase):
    def __unicode__(self):
        return 'HTML'
