#!/bin/sh

FOLDER="/mnt/base-us/weather"
FILE="weather.png"
URL="http://cn-vpn.grisge.info/weather/weather.png"

cd $FOLDER

if [ $(gasgauge-info -s 2>/dev/null | sed -ne 's/\([0-9]\+\).*/\1/p') -le 10 ];
then
    eips -f "Low battery, charge please"
    exit;
fi

# Wake Up
lipc-set-prop com.lab126.powerd wakeUp 1

sleep 10

ifconfig wlan0 >/dev/null 2>&1
if [ $? -ne 0 ];then
    exit
fi

rm $FOLDER/$FILE

# Lock screen
/usr/bin/powerd_test -p

sleep 10

wget $URL -O $FOLDER/$FILE

if [ -e $FOLDER/$FILE ];then
    eips -f -g $FOLDER/$FILE
fi
