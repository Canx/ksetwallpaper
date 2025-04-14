#!/bin/bash

XCF_FILE="./background/normas.xcf"
OUTPUT_DIR="./background"
RESOLUTIONS=("1920x1080" "1440x900" "1280x1024" "1024x768")
DEFAULT_RES="1920x1080"

mkdir -p "$OUTPUT_DIR"

for RES in "${RESOLUTIONS[@]}"
do
    WIDTH=$(echo $RES | cut -d'x' -f1)
    HEIGHT=$(echo $RES | cut -d'x' -f2)
    OUTPUT_FILE="$OUTPUT_DIR/${RES}.png"

    echo "Exportando a $RES..."
    gimp -i -b - <<EOF
(let* (
    (image (car (gimp-file-load RUN-NONINTERACTIVE "$XCF_FILE" "$XCF_FILE")))
    (drawable (car (gimp-image-merge-visible-layers image CLIP-TO-IMAGE)))
  )
  (gimp-image-scale image $WIDTH $HEIGHT)
  (file-png-save RUN-NONINTERACTIVE image drawable "$OUTPUT_FILE" "$OUTPUT_FILE" 0 9 0 0 0 0 0)
  (gimp-image-delete image)
)
(gimp-quit 0)
EOF
done

# Crear enlace simbólico al default
cd "$OUTPUT_DIR"
ln -sf "${DEFAULT_RES}.png" default.png
echo "Enlace simbólico creado: default.png → ${DEFAULT_RES}.png"

