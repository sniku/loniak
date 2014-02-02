import datetime

'''
These functions are used for filtering the torrent lists.
They are implementing these directives:
match: text
exclude: text
published_days_ago: number
'''

def substring_match(match, exclude):

    def real_match(torrent):
        for e in exclude:
            if e in torrent.title or e in torrent.description:
                return False
            for location in torrent.torrent_locations:
                if e in location:
                    return False

        for m in match:
            if m in torrent.title or m in torrent.description:
                torrent.matched = m
                return True
            for location in torrent.torrent_locations:
                if m in location:
                    torrent.matched = m
                    return True
        if match: # if any match were specified, we are excluding not matched ones.
            return False
        else:    # if no match were specified, we are including all
            return True

    return real_match

def publication_date_match(published_days_ago):

    def real_match(torrent):
        if published_days_ago and torrent.publication_date:
            threshold = datetime.datetime.now() - datetime.timedelta(days=int(published_days_ago))
            if torrent.publication_date > threshold:
                return True
            else:
                return False

        return True # fallback


    return real_match

