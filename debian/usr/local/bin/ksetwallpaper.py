#!/usr/bin/env python3
import argparse
import requests
import subprocess
import shutil
from pathlib import Path
import tempfile
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
    # Se obtiene el comando qdbus a usar (qdbus6 o qdbus)
    qdbus_cmd = get_qdbus_command()

    # Asegurarse de trabajar con la ruta absoluta
    image_path = image_path.resolve()

    # Se construye el script para cambiar el fondo en todos los escritorios
    script = """
    desktops().forEach(d => {
        d.currentConfigGroup = Array("Wallpaper",
                                     "org.kde.image",
                                     "General");
        d.writeConfig("Image", "file://FILEPATH");
        d.reloadConfig();
    });
    """.replace("FILEPATH", str(image_path))

    # Se invoca el comando qdbus para ejecutar el script en el Plasma Shell
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

def download_image(url: str) -> Path:
    """
    Descarga una imagen desde la URL especificada y la guarda en un archivo temporal.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print("Error descargando la imagen:", e, file=sys.stderr)
        sys.exit(1)

    # Se guarda el contenido en un archivo temporal
    tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
    tmp_file.write(response.content)
    tmp_file.close()
    return Path(tmp_file.name)

def main():
    parser = argparse.ArgumentParser(
        description="Cambia el fondo de pantalla de KDE usando qdbus y un script de Plasma."
    )
    parser.add_argument(
        "--image",
        type=Path,
        help="Ruta al archivo de imagen a establecer como fondo."
    )
    parser.add_argument(
        "--url",
        type=str,
        default="https://pic.re/image",
        help="URL de la imagen a descargar para usar como fondo (por defecto: %(default)s)."
    )
    args = parser.parse_args()

    if args.image:
        if not args.image.exists():
            print(f"El archivo {args.image} no existe.", file=sys.stderr)
            sys.exit(1)
        image_file = args.image
    else:
        image_file = download_image(args.url)

    set_wallpaper(image_file)

if __name__ == "__main__":
    main()
