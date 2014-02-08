======
loniak
======

Automatic torrent downloader.

### Installation ###

#### install the dependencies ####

    apt-get install transmission transmission-cli transmission-daemon

### install loniak ####
###### method 1 ######
Assuming that you have git and python-pip

    pip install git+https://github.com/sniku/loniak
###### method 2 ######

    git clone https://github.com/sniku/loniak
    cd loniak
    python setup.py install


### Configuration ###
    
    cat /etc/loniak/loniak.conf
    
    [main]
    DEBUG: true
    TRANSMISSION_USERNAME: transmission
    TRANSMISSION_PASSWORD: transmission
    TRANSMISSION_HOST: 127.0.0.1
    CLIENT: Transmission
    
    # Monitors both eztv.it and thepiratebay.se
    # Downloads House Of Cards, Ambassadors and Helix series (match: Helix)
    # And the pilot episodes of all the new series (match: S01E01) 
    # Excludes all the 720p files. (I don't want them) 
    # Skips the files published later than yesterday (published_days_ago: 1)
    [source thepiratesbay_and_eztv]
    type: RSS
    URL: http://rss.thepiratebay.se/205
    URL: http://www.ezrss.it/feed/
    exclude: 720p
    published_days_ago: 1
    match: House Of Cards
    match: Ambassadors
    match: Helix
    match: S01E01

    # This is downloading all the movies/TV series that I have on my www.imdb.com watchlist
    # Whenever you add something to your watchlist, it will be downloaded automatically by loniak
    [source my_imdb_watchlist]
    type: IMDB
    URL: http://rss.imdb.com/user/urXXXXXX/watchlist

    # Monitors subsection of eztv.it and downloads all the episodes from there
    [source sherlock]
    type: RSS
    URL: http://www.ezrss.it/search/index.php?show_name=Sherlock&show_name_exact=true&mode=rss
    
    # Monitors finalgear.com and downloads all new episodes.
    [source topgear]
    type: RSS
    URL: http://www.finalgear.com/feed/torrents/sd/
    published_days_ago: 1
    
    # If the website you want to monitor doesn't have a RSS feed, you can use the HTML type
    [source topgear]
    type: HTML
    URL: https://thepiratebay.se/search/something+that+is+not+yet+released/0/99/0
    
    
