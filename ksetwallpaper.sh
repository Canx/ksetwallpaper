#!/bin/bash
sleep 15
echo "HOLA" > /tmp/ksetwallpaper.log
file="/usr/share/wallpapers/Altai/contents/images/1080x1920.png"
/usr/local/bin/ksetwallpaper.py $file
