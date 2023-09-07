#!/bin/bash

# TODO: Generar las imágenes a partir del xcf

# Copiar las imágenes a sus ubicaciones
cp ./background/5000x2813.png ./debian/usr/share/wallpapers/lliurex-escriptori-normas/contents/images/

dpkg-deb -b debian ksetwallpaper.deb
