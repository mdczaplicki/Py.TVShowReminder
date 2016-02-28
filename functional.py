from urllib import request, error
from datetime import datetime
from globals import *
import win32api
import json


def message_box(message, title) -> win32api.MessageBox:
    return win32api.MessageBox(None, message, title)


def get_www(url_in) -> str:
    try:
        return request.urlopen(url_in).read().decode('utf-8')
    except error.HTTPError:
        raise SeriesNotFoundException


def get_metadata(series_name) -> dict:
    url = URL_PATTERN.replace('####', series_name)
    www = get_www(url)
    data = json.loads(www)
    return data['episode']


def days_between(date1, date2) -> int:
    d1 = datetime.strptime(date1, '%Y-%m-%d')
    d2 = datetime.strptime(date2, '%Y-%m-%d')
    return abs((d2 - d1).days)