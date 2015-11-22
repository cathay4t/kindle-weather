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

from weather_api import WeatherAPI

weather_obj = WeatherAPI()

# Open SVG to process
output = codecs.open('weather-script-preprocess.svg', 'r',
                     encoding='utf-8').read()

# Update weather condition
output = output.replace('ICON_ONE', weather_obj.condition(0));

output = output.replace('ICON_TWO', weather_obj.condition(1));

output = output.replace('ICON_THREE', weather_obj.condition(2));

output = output.replace('ICON_FOUR', weather_obj.condition(3));

# Update hightest temp
output = output.replace('HIGH_ONE', str(weather_obj.temp_high(0)));

output = output.replace('HIGH_TWO', str(weather_obj.temp_high(1)));

output = output.replace('HIGH_THREE', str(weather_obj.temp_high(2)));

output = output.replace('HIGH_FOUR', str(weather_obj.temp_high(3)));

# Update lowest temp
output = output.replace('LOW_ONE', str(weather_obj.temp_low(0)));

output = output.replace('LOW_TWO', str(weather_obj.temp_low(1)));

output = output.replace('LOW_THREE', str(weather_obj.temp_low(2)));

output = output.replace('LOW_FOUR', str(weather_obj.temp_low(3)));

day_one = datetime.datetime.strptime(weather_obj.today_str(), '%Y-%m-%d')

# Insert days of week
one_day = datetime.timedelta(days=1)
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
                'Saturday', 'Sunday']
output = output.replace('DAY_THREE',
                        days_of_week[(day_one + 2 * one_day).weekday()])
output = output.replace('DAY_FOUR',
                        days_of_week[(day_one + 3 * one_day).weekday()])

# Write output
codecs.open('weather-script-output.svg', 'w', encoding='utf-8').write(output)

os.system("rsvg-convert --background-color=white -o "
          "weather-script-output.png weather-script-output.svg");

os.system("pngcrush -c 0 -ow weather-script-output.png 1>/dev/null 2>&1");
