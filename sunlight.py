import datetime
from astral import Astral

def getSun(city_name):
	a = Astral()
	a.solar_depression = 'civil'
	city = a[city_name]
	return city.sun(date=datetime.date.today(), local=True)

def timeOfDayToSeconds(timeOfDay):
	timeDelta = datetime.timedelta(hours=timeOfDay.hour, minutes=timeOfDay.minute, seconds=timeOfDay.second)
	return timeDelta.total_seconds()

def getSunSchedule(city_name):
	sun = getSun(city_name)

	dawn = timeOfDayToSeconds(sun['dawn'])
	sunrise = timeOfDayToSeconds(sun['sunrise'])
	noon = timeOfDayToSeconds(sun['noon'])
	sunset = timeOfDayToSeconds(sun['sunset'])
	dusk = timeOfDayToSeconds(sun['dusk'])

	# Lengths all expressed in seconds
	half_midnight_length = 60 * 60.0
	dusk_length = 60 * 30
	predawn_length = 60 * 30.0
	morning_section_length = round((noon - sunrise) / 4, 0)
	afternoon_section_length = round((sunset - noon) / 5, 0)

	beforeMidnight = dusk + dusk_length
	midnight = (24 * 60 * 60) - half_midnight_length
	afterMidnight = half_midnight_length

	predawn = dawn - predawn_length

	earlyMorning = sunrise + morning_section_length
	midMorning = earlyMorning + morning_section_length
	lateMorning = midMorning + morning_section_length

	earlyAfternoon = noon + afternoon_section_length
	midAfternoon = earlyAfternoon + afternoon_section_length
	lateAfternoon = midAfternoon + afternoon_section_length
	goldenHour = lateAfternoon + afternoon_section_length

	thres = [afterMidnight, predawn, dawn, sunrise, earlyMorning, midMorning, lateMorning,
			noon, earlyAfternoon, midAfternoon, lateAfternoon, goldenHour, sunset,
			dusk, beforeMidnight, midnight]
	return thres