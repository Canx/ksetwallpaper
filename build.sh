#!/bin/bash

# TODO: Generar las imágenes a partir del xcf

# Copiar las imágenes a sus ubicaciones
rm -rf ./debian/usr/share/wallpapers
mkdir -p ./debian/usr/share/wallpapers/reglas_centro/contents/images/
cp ./background/*.png ./debian/usr/share/wallpapers/reglas_centro/contents/images/

dpkg-deb -b debian ksetwallpaper.deb
