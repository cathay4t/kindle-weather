#!/bin/sh

FOLDER="/mnt/base-us/weather"
FILE="weather.png"

cd $FOLDER

# Lock and Wake Up
/usr/bin/powerd_test -p >/dev/null

sleep 10

ifconfig wlan0 >/dev/null 2>&1
if [ $? -ne 0 ];then
    exit
fi

rm $FOLDER/$FILE
wget http://cn-vpn.grisge.info/weather/weather.png -O $FOLDER/$FILE

# Lock screen
/usr/bin/powerd_test -h >/dev/null

sleep 10

eips -f -g $FOLDER/$FILE
