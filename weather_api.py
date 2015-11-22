#!/usr/bin/python2
# Copyright (C) 2015 Red Hat, Inc.
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
# Author: Gris Ge <fge@redhat.com>

class WeatherAPI(object):

    CONDITION_LIGHT_RAIN = "shra"
    CONDITION_LIGHT_CLOUD_SUN = "bkn"

    def __init__(self):
        pass

    def temp_high(self, day):
        """
        Input day as integer, 0 means today, 1 means tomorrow.
        Return
        """
        if (day == 0):
            return 19
        if (day == 1):
            return 19
        if (day == 2):
            return 19
        if (day == 3):
            return 16
        if (day == 4):
            return 16

    def temp_low(self, day):
        if (day == 0):
            return 13
        if (day == 1):
            return 14
        if (day == 2):
            return 14
        if (day == 3):
            return 11
        if (day == 4):
            return 9

    def condition(self, day):
        if (day == 0):
            return WeatherAPI.CONDITION_LIGHT_RAIN
        if (day == 1):
            return WeatherAPI.CONDITION_LIGHT_RAIN
        if (day == 2):
            return WeatherAPI.CONDITION_LIGHT_RAIN
        if (day == 3):
            return WeatherAPI.CONDITION_LIGHT_RAIN
        if (day == 4):
            return WeatherAPI.CONDITION_LIGHT_CLOUD_SUN

    def today_str(self):
        return "2015-11-21"
