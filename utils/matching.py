import datetime

def substring_match(match):

    def real_match(torrent):
        for m in match:
            if m in torrent.title or m in torrent.description:
                torrent.matched = m
                return True
            for location in torrent.torrent_locations:
                if m in location:
                    torrent.matched = m
                    return True

        return False


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

