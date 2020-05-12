
# KDE Dynamic Wallpaper

When set to run with crontab, this python script will change the wallpaper according to the time of day. In addition, it needs your location to find when sunset and sunrise are to better match your surroundings.

NOTE: It only works for KDE if the title wasn't clear

## Setup

Install necessary python packages:

```bash
pip install argparse astral
```

## Usage

Clone the repository into any folder

```bash
git clone https://github.com/HoldenA1/KDE-Dynamic-Wallpaper.git
```

cd into the repository

```bash
cd KDE-Dynamic-Wallpaper
```

### One Time Use

```bash
python wallpaper.py '[City You Live In]'
```

### With Crontab

Set crontab to run every 15 minutes and on startup:

```bash
crontab -e
```

Paste this into crontab:

```crontab
*/15 * * * * env DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus /usr/bin/python [Repo Path]/wallpaper.py '[City You Live In]'
@reboot sleep 30 && env DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus /usr/bin/python [Repo Path]/wallpaper.py '[City You Live In]'
```
