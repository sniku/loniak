import ConfigParser
import os
from os.path import expanduser


DEFAULT_SETTINGS = {
    'CONFIG_FILE_PATH': '/etc/loniak/loniak.conf',
    'MAIN_LOG': '/var/log/loniak.log',
    'CLIENT': 'Transmission',
    'DEBUG': True,
    'VERBOSE': True,
}

class SettingsContainer(object):
    pass

class Settings(object):
    def __init__(self):
        if self.check_config_file():
            self.read_config()
            self.validate_settings()
        self.settings_container = SettingsContainer()

    def __getattr__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            pass

        if name in DEFAULT_SETTINGS:
            return DEFAULT_SETTINGS.get(name)

        return None

    def read_config(self):
        booleans = ['verbose', 'debug']
        config = ConfigParser.ConfigParser()
        config.read(DEFAULT_SETTINGS['CONFIG_FILE_PATH'])
        options = config.options('defaults')
        for option in options:
            if option in booleans:
                setattr(self, option.upper(), config.getboolean('defaults', option))
            else:
                setattr(self, option.upper(), config.get('defaults', option))

    def check_config_file(self):
        if not os.path.isfile(DEFAULT_SETTINGS['CONFIG_FILE_PATH']):
            raise Exception(u'Config file %s is missing.'%DEFAULT_SETTINGS['CONFIG_FILE_PATH'])
        return True

    def validate_settings(self):
        pass
        # if not self.get('mediawiki_url', None):
        #     raise Exception(u"Config directive 'mediawiki_url' is empty of missing. You must provide URL to your mediawiki installation")

settings = Settings()