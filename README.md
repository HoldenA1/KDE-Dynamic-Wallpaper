## KDE Dynamic Wallpaper
When set to run with crontab, this python script will change the wallpaper according to the time of day. In addition, it needs your location to find when sunset and sunrise are to better match your surroundings.

NOTE: It only works for KDE if the title wasn't clear

### Setup
Install necessary python packages:
```
$ pip install argparse astral
```
Set crontab to run every 15 minutes and on startup:
```
$ crontab -e
```
Paste this into crontab:
```
*/15 * * * * cd [Repo Path] & /usr/bin/python3 wallpaper.py
@reboot cd [Repo Path] & /usr/bin/python3 wallpaper.py
```
