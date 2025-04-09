#!/bin/bash
file="/usr/share/wallpapers/reglas_centro/contents/images/5000x2813.png"

# Esperamos a que plasmashell esté listo
sleep 15

# Para evitar tentaciones...
for i in {1..50}
do
  /usr/local/bin/ksetwallpaper.py $file
  sleep 1m
done
