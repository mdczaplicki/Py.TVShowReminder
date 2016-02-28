from locale import getdefaultlocale
from time import strftime
from functional import *
import configparser


if __name__ == '__main__':
    language = getdefaultlocale()
    today = strftime('%Y-%m-%d')
    series = {}
    config = configparser.ConfigParser()
    with open('series.cfg', 'r') as file:
        config.read_file(file)
        for serie in config.options('series'):
            metadata = get_metadata(serie)
            series[serie] = {RELEASE_DATE: metadata[RELEASE_DATE],
                             TITLE: metadata['show'][TITLE],
                             SEASON: metadata[SEASON],
                             EPISODE: metadata[EPISODE]}
        file.close()
    del config
    delay = days_between(today, series['the100'][RELEASE_DATE])
    data = PluralDict({'title': 'ABC', 'season': '01', 'episode': '03', 'days': 2})
    print(MB_MESSAGE['en_EN'].format_map(data))
    print(MB_MESSAGE['pl_PL'].format_map(data))
