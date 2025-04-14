#!/bin/bash

# Esperamos a que plasmashell esté listo
sleep 15

# Detectar resolución de pantalla
resolution=$(xrandr | grep '*' | head -n1 | awk '{print $1}')
wallpaper_dir="/usr/share/wallpapers/reglas_centro/contents/images"
file="$wallpaper_dir/${resolution}.png"

# Verificar que el archivo exista
if [ ! -f "$file" ]; then
  echo "No se encontró un fondo para la resolución $resolution, usando fondo por defecto."
  file="$wallpaper_dir/default.png"
fi

# Cambiar el fondo en bucle por si falla alguna vez
for i in {1..50}
do
  /usr/local/bin/ksetwallpaper.py --image "$file"
  sleep 1m
done
