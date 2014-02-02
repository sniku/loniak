try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='loniak',
    version='0.1',
    packages=[
        'loniak', 'loniak.clients', 'loniak.config', 'loniak.libs',  'loniak.libs.dateutil',
        'loniak.loniak_exceptions', 'loniak.services', 'loniak.sources', 'loniak.tr', 'loniak.utils',
              ],
    py_modules=['loniak',],
    scripts=['loniak.py',],
    url='http://suwala.eu/',
    author="Pawel Suwala",
    author_email="pawel.suwala@fsfe.org",
    license='GPLv3',
    long_description="Torrent fetching client.",
    install_requires=['dateutils >= 0.6', 'docopt >= 0.6', 'feedparser >= 5'],

)