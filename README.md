# ksetwallpaper
Change KDE wallpaper at startup (lliurex)

# Install
## deb package
Download and install [deb package](https://github.com/Canx/ksetwallpaper/raw/main/ksetwallpaper_0.1_all.deb)

```sudo dpkg -i ksetwallpaperXXXX.deb```

## Manual
Copy `ksetwallpaper.py` and `ksetwallpaper.sh` to `/usr/local/bin/`

Copy `ksetwallpaper.desktop` to `/etc/xdg/autostart/`

# TODO
* Wait for plasmashell instead of sleeping
* Reset wallpaper only when user changes it

# Authors
`ksetwallpaper.py` is borrowed from [Pavel Borisov](https://github.com/pashazz/ksetwallpaper)
