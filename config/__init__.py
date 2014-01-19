import ConfigParser
import os
from os.path import expanduser
from samba.dcerpc.security import sec_desc_buf


DEFAULT_SETTINGS = {
    'CONFIG_FILE_PATH': '/etc/loniak/loniak.conf',
    'MAIN_LOG': '/var/log/loniak.log',
    'CLIENT': 'Transmission',
    'DEBUG': True,
    'VERBOSE': True,
    'TRANSMISSION_USERNAME': 'transmission',
    'TRANSMISSION_PASSWORD': 'transmission',
}


class RepeatedDict(dict):

    def __init__(self, *args, **kwargs):
        self.repeated_keys = ['match']
        super(RepeatedDict, self).__init__(*args, **kwargs)

    def __setitem__(self, key, value):
        # test if item already exists
        if key in self.repeated_keys:

            if key not in self:
                dict.__setitem__(self, key, [])
            if type(value) is list:
                self[key].append(value[0])
            # else:
            #     self[key].append(value)
        else:
            dict.__setitem__(self, key, value)

class Settings(object):
    def __init__(self):
        if self.check_config_file():
            self.read_config()
            self.validate_settings()

    def __getattr__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            pass

        if name in DEFAULT_SETTINGS:
            return DEFAULT_SETTINGS.get(name)

        if self.DEBUG:
            print '"{0}" is not set in the config file. Are you sure it\'s spelled correctly?'.format(name)

        return None

    def read_config(self):
        booleans = ['verbose', 'debug']
        config = ConfigParser.ConfigParser(dict_type=RepeatedDict)
        config.read(DEFAULT_SETTINGS['CONFIG_FILE_PATH'])
        main = config.options('main')


        for option in main:
            if option in booleans:
                setattr(self, option.upper(), config.getboolean('main', option))
            else:
                setattr(self, option.upper(), config.get('main', option))

        sources = []
        for section_name in config.sections():
            if not section_name.startswith('source'):
                continue

            sources.append(dict([(x, config.get(section_name, x)) for x in config.options(section_name)])) # {'type': config.get(section_name, 'type'), 'url': config.get(section_name, 'url')}

        self.sources = sources




    def check_config_file(self):
        if not os.path.isfile(DEFAULT_SETTINGS['CONFIG_FILE_PATH']):
            raise Exception(u'Config file %s is missing.'%DEFAULT_SETTINGS['CONFIG_FILE_PATH'])
        return True

    def validate_settings(self):
        pass
        # if not self.get('mediawiki_url', None):
        #     raise Exception(u"Config directive 'mediawiki_url' is empty of missing. You must provide URL to your mediawiki installation")

settings = Settings()