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
import urllib2

_SCI_URL = 'http://hq.sinajs.cn/list=sh000001'

def _fetch_html(url):
    request = urllib2.Request(url)
    return urllib2.urlopen(request).read()

def sci_get():
    '''
    Return current Shanghai Composite Index and change percentage in list.
    Data is from parsed from sina
    '''
    html_content = _fetch_html(_SCI_URL)
    tmp_ar = html_content.split(',')
    cur = float(tmp_ar[3])
    pre = float(tmp_ar[2])
    sci =  "%.2f" % cur
    sci_chg = "%.2f%%" % float( (cur - pre) / pre * 100)
    return (sci, sci_chg)
