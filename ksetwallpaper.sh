#!/bin/bash
file="/usr/share/wallpapers/Altai/contents/images/1080x1920.png"

# Esperamos a que plasmashell esté listo
sleep 15

# Para evitar tentaciones...
for i in {1..50}
do
  /usr/local/bin/ksetwallpaper.py $file
  sleep 1m
done
