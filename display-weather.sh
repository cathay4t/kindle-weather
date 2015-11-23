#!/bin/sh

FOLDER="/mnt/base-us/weather"
FILE="weather.png"
URL="http://cn-vpn.grisge.info/weather/weather.png"

cd $FOLDER

# Wake Up
lipc-set-prop com.lab126.powerd wakeUp 1

sleep 10

ifconfig wlan0 >/dev/null 2>&1
if [ $? -ne 0 ];then
    exit
fi

rm $FOLDER/$FILE
wget $URL -O $FOLDER/$FILE

# Lock screen
/usr/bin/powerd_test -p

sleep 10

eips -f -g $FOLDER/$FILE
