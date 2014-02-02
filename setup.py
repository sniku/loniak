try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import sys
import os
import shutil

setup(
    name='loniak',
    version='0.1',
    packages=[
        'loniak_module', 'loniak_module.clients', 'loniak_module.config', 'loniak_module.libs',  'loniak_module.libs.dateutil',
        'loniak_module.loniak_exceptions', 'loniak_module.services', 'loniak_module.sources', 'loniak_module.tr', 'loniak_module.utils',
              ],
    py_modules=[
        'loniak_module', 'loniak_module.clients', 'loniak_module.config', 'loniak_module.libs',  'loniak_module.libs.dateutil',
        'loniak_module.loniak_exceptions', 'loniak_module.services', 'loniak_module.sources', 'loniak_module.tr', 'loniak_module.utils',
              ],
    scripts=['loniak.py',],
    url='http://suwala.eu/',
    author="Pawel Suwala",
    author_email="pawel.suwala@fsfe.org",
    license='GPLv3',
    long_description="Torrent fetching client.",
    install_requires=['dateutils >= 0.6', 'docopt >= 0.6', 'feedparser >= 5'],
)

if sys.argv[1].lower() == 'install':
    DEFAULT_CONFIG_DIRECTORY = '/etc/loniak/'
    DEFAULT_CONFIG_LOCATION = '/etc/loniak/loniak.conf'
    DEFAULT_DATA_LOCATION = '/etc/loniak/data.json'


    if not os.path.exists(DEFAULT_CONFIG_DIRECTORY):
        os.makedirs(DEFAULT_CONFIG_DIRECTORY)

    if not os.path.exists(DEFAULT_CONFIG_LOCATION):
        shutil.copyfile("example_config.conf", DEFAULT_CONFIG_LOCATION)
        # by default we allow everyone to read/write config file.
        os.chmod(DEFAULT_CONFIG_LOCATION, 0666)

    if not os.path.exists(DEFAULT_DATA_LOCATION):
        open(DEFAULT_DATA_LOCATION, 'w+').close()
        os.chmod(DEFAULT_DATA_LOCATION, 0666)


