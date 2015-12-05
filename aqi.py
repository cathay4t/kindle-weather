#!/usr/bin/python2
# Copyright (C) 2015 Gris Ge
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 3 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; If not, see <http://www.gnu.org/licenses/>.
#
# Author: Gris Ge <cnfourt@gmail.com>
from urllib2 import urlopen
from HTMLParser import HTMLParser

_AQI_URL = 'http://aqicn.org/city/<CITY>/m'
_AQI_DIV_NAME = 'xatzcaqv'

class _MyHTMLParser(HTMLParser):
    #TODO(Gris Ge): Stop parsing once found.
    def __init__(self):
        HTMLParser.__init__(self)
        self._flag_found_aqi_div = False
        self.aqi = 0

    def handle_starttag(self, tag, attrs):
        if self.aqi != 0:
            return

        if tag != 'div':
            return

        tmp_dict = dict(attrs)

        if tmp_dict.get('id') == _AQI_DIV_NAME:
            self._flag_found_aqi_div = True
            return

    def handle_endtag(self, tag):
        self._flag_found_aqi_div = False

    def handle_data(self, data):
        if self._flag_found_aqi_div:
            self.aqi = data

def _fetch_html(url):
    return urlopen(url).read()

def aqi_get(city_name):
    '''
    Return integer for AQI of given city and raise error if failure.
    Data is from parsed from twitter US account.
    '''
    url = _AQI_URL.replace('<CITY>', city_name)
    html_content = _fetch_html(url)
    parser = _MyHTMLParser()
    parser.feed(html_content)
    return int(parser.aqi)
