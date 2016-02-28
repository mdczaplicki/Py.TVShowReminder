# -*- coding: utf-8 -*-
from locale import getdefaultlocale
from time import strftime
from functional import *
import configparser


if __name__ == '__main__':
    language = getdefaultlocale()[0]
    today = strftime('%Y-%m-%d')
    series = {}
    config = configparser.ConfigParser()
    with open('series.cfg', 'r') as file:
        config.read_file(file)
        for show in config.options('series'):
            metadata = get_metadata(show)
            series[show] = {RELEASE_DATE: metadata[RELEASE_DATE],
                            TITLE: metadata['show'][TITLE],
                            SEASON: str(metadata[SEASON]).rjust(2, '0'),
                            EPISODE: str(metadata[EPISODE]).rjust(2, '0')}
        file.close()
    del config
    message = ''
    for show, data in series.items():
        release_date = data[RELEASE_DATE]
        delay = days_between(today, release_date)
        if delay in [2, 3]:
            temp = PluralDict({'title': data[TITLE], 'season': data[SEASON],
                               'episode': data[EPISODE], 'days': delay})
            temp = MB_MESSAGE[language].format_map(temp)
            message += temp
    message_box(message, MB_TITLE[language])