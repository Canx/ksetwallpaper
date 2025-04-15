#!/usr/bin/env python3
import argparse
import subprocess
import shutil
from pathlib import Path
import sys

def get_qdbus_command() -> str:
    """
    Busca y devuelve el comando qdbus6 o qdbus disponible en el sistema.
    """
    for cmd in ["qdbus6", "qdbus"]:
        if shutil.which(cmd) is not None:
            return cmd
    print("No se encontró 'qdbus6' ni 'qdbus' en tu sistema.", file=sys.stderr)
    sys.exit(1)

def set_wallpaper(image_path: Path):
    """
    Cambia el wallpaper en KDE mediante qdbus inyectando código JavaScript en el PlasmaShell.
    """
    qdbus_cmd = get_qdbus_command()
    image_path = image_path.resolve()

    script = """
    desktops().forEach(d => {
        d.wallpaperPlugin = "org.kde.image";
        d.currentConfigGroup = Array("Wallpaper", "org.kde.image", "General");
        d.writeConfig("Image", "file://FILEPATH");
        d.reloadConfig();
        d.reloadWallpaper();
    });
    """.replace("FILEPATH", str(image_path))

    try:
        subprocess.check_call(
            [
                qdbus_cmd,
                "org.kde.plasmashell",
                "/PlasmaShell",
                "org.kde.PlasmaShell.evaluateScript",
                script,
            ],
            stdout=subprocess.DEVNULL
        )
    except subprocess.CalledProcessError as e:
        print("Error al cambiar el fondo de pantalla:", e, file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
        description="Cambia el fondo de pantalla de KDE usando qdbus y un script de Plasma."
    )
    parser.add_argument(
        "image",
        type=Path,
        help="Ruta al archivo de imagen a establecer como fondo."
    )
    args = parser.parse_args()

    if not args.image.exists():
        print(f"El archivo {args.image} no existe.", file=sys.stderr)
        sys.exit(1)

    set_wallpaper(args.image)

if __name__ == "__main__":
    main()

