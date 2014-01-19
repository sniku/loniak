from sources.rss import RssSource
from sources.html import HtmlSource

ALL_MODULES = [RssSource(), HtmlSource()]

def get_module(name):
    modules = dict([(cls.__unicode__(), cls) for cls in get_available_modules()])
    # print modules

    return modules.get(name, None)

def get_available_modules():
    return ALL_MODULES
    #return [cls() for cls in get_available_modules()]

