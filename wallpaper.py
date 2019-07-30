#!/usr/bin/env python3

import datetime
import dbus
from sunlight import *
import argparse
import os
cwd = os.getcwd()

def get_args():
    arg_parser = argparse.ArgumentParser(
        description='''Dynamic Wallpaper for linux''',
        formatter_class=argparse.RawTextHelpFormatter)

    arg_parser.add_argument(
        'city', metavar='city', type=str,
        help='Put your location\n\n')

    arg_parser.add_argument(
        '-t', '--time', metavar='time', type=str,
        help='Put the desired time in hh:mm:ss\n\n',
        required=False)

    return vars(arg_parser.parse_args())

def timeOfDayToSeconds(timeOfDay):
	timeDelta = datetime.timedelta(hours=timeOfDay.hour, minutes=timeOfDay.minute, seconds=timeOfDay.second)
	return timeDelta.total_seconds()

def getTimeOfDay(thres, current_time):
    labels = ['after-midnight', 'pre-dawn', 'dawn', 'sunrise', 'early-morning', 'mid-morning', 'late-morning',
    			'midday', 'early-afternoon', 'mid-afternoon', 'late-afternoon', 'golden-hour',
    			'sunset', 'dusk', 'before-midnight', 'midnight']

    thres.append(current_time)
    thres.sort()
    day_index = thres.index(current_time)
    if (day_index == 0):
    	return labels[len(labels) - 1]
    else:
    	return labels[day_index - 1]

def setwallpaper(filepath, plugin = 'org.kde.image'):
    jscript = """
    var allDesktops = desktops();
    print (allDesktops);
    for (i=0;i<allDesktops.length;i++) {
        d = allDesktops[i];
        d.wallpaperPlugin = "%s";
        d.currentConfigGroup = Array("Wallpaper", "%s", "General");
        d.writeConfig("Image", "file://%s")
    }
    """
    bus = dbus.SessionBus()
    plasma = dbus.Interface(bus.get_object('org.kde.plasmashell', '/PlasmaShell'), dbus_interface='org.kde.PlasmaShell')
    plasma.evaluateScript(jscript % (plugin, plugin, filepath))


if __name__ == '__main__':
	args = get_args()
	city_name = args['city']
	thres = getSunSchedule(city_name)
	if args['time']:
		time = timeOfDayToSeconds(datetime.datetime.strptime(args['time'], '%H:%M:%S'))
	else:
		time = timeOfDayToSeconds(datetime.datetime.now())

	timeOfDay = getTimeOfDay(thres, time)
	print(timeOfDay)
	setwallpaper(cwd + "/mojave/" + timeOfDay + ".jpeg")
