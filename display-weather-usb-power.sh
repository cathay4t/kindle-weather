#!/bin/sh

FOLDER="/mnt/base-us/weather"
FILE="weather.png"
URL="http://cn-vpn.grisge.info/weather/weather.png"

cd $FOLDER

ifconfig wlan0 >/dev/null 2>&1
if [ $? -ne 0 ];then
    exit
fi

rm $FOLDER/$FILE

wget $URL -O $FOLDER/$FILE

if [ -e $FOLDER/$FILE ];then
    eips -f -g $FOLDER/$FILE
fi
