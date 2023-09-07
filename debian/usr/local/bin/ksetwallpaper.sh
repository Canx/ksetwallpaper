#!/bin/bash
file="/usr/share/wallpapers/lliurex-escriptori/contents/images/1920x1080.png"

# Esperamos a que plasmashell esté listo
sleep 15

# Para evitar tentaciones...
for i in {1..50}
do
  /usr/local/bin/ksetwallpaper.py $file
  sleep 1m
done
