#!/usr/bin/python2
# Copyright (c) 2014 Gris Ge
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
#     The above copyright notice and this permission notice shall be included
#     in all copies or substantial portions of the Software.
#
#     THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#     OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#     MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#     IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
#     CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
#     TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
#     SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
#
# Author: Gris Ge <cnfourt@gmail.com>

# Code was edit based on
# https://github.com/mpetroff/kindle-weather-display.git
# Which is also MIT license.
#
# Kindle Weather Display
# Matthew Petroff (http://mpetroff.net/)
# September 2012

import codecs
import datetime
import os
import sys

from weather_api import WeatherAPI

CODE_FOLDER = os.path.dirname(os.path.realpath(__file__))
OUTPUT="/var/www/html/weather/weather.png"

try:
    _, api_key, latitude, longitude = sys.argv
except IndexError:
    exit("Need 3 argument for API key, latitude, longitude")

weather_obj = WeatherAPI(api_key, latitude, longitude)

# Open SVG to process
output = codecs.open(CODE_FOLDER + "/weather-script-preprocess.svg", "r",
                     encoding="utf-8").read()

for i, x in enumerate("ONE TWO THREE FOUR".split()):
    output = output.replace("ICON_" + x, weather_obj.condition(i))
    output = output.replace("HIGH_" + x, weather_obj.temp_max(i))
    output = output.replace("LOW_" + x, weather_obj.temp_min(i))

# Replace refresh time
output = output.replace("TIME",
                        datetime.datetime.now().strftime("%b %d %A %H:%M"))

day_one = weather_obj.today

# Insert days of week
one_day = datetime.timedelta(days=1)
days_of_week = "Mon Tue Wed Thu Fri Sat Sun".split()
for i, x in "TWO THREE FOUR".split():
    output = output.replace("DAY_" + x,
                        days_of_week[(day_one + (i + 1) * one_day).weekday()])

# Write output
codecs.open(CODE_FOLDER + "/weather-script-output.svg",
            "w", encoding="utf-8").write(output)

os.system("rsvg-convert --background-color=white -o "
          "%s %s/weather-script-output.svg"
          % (OUTPUT, CODE_FOLDER));

os.system("pngcrush -c 0 -ow %s 1>/dev/null 2>&1" %
          OUTPUT);
