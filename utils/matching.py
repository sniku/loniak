

def match_regex(match):

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
