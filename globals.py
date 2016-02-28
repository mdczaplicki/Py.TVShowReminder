class PluralDict(dict):
    def __missing__(self, key):
        if '(' in key and key.endswith(')'):
            key, rest = key.split('(', 1)
            value = super().__getitem__(key)
            suffix = rest.rstrip(')').split(',')
            if len(suffix) == 1:
                suffix.insert(0, '')
            return suffix[0] if value <= 1 else suffix[1]
        raise KeyError(key)


class SeriesNotFoundException(Exception):
    def __init__(self):
        super(SeriesNotFoundException, self).__init__()


RELEASE_DATE = 'release_date'
TITLE = 'title'
SEASON = 'season'
EPISODE = 'number'
URL_PATTERN = 'https://epguides.frecar.no/show/####/last/'

MB_TITLE = {
    'en_EN': 'TV Show reminder',
    'pl_PL': 'Przypomnienie o serialu'
}
MB_MESSAGE = {
    'en_EN': '{title} s{season}e{episode} has been released {days} day{days(s)} ago.\n',
    'pl_PL': 'Serial {title} s{season}e{episode} jest dostępny od {days} {days(dnia,dni)}\n',
}
