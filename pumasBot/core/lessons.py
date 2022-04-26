import os

from datetime import datetime, date, timedelta, timezone
from dateutil.rrule import *

import icalendar


def schedule_message_creator():
    schedule_ = daily_schedule()
    schedule = [lesson for n, lesson in enumerate(schedule_) if lesson not in schedule_[:n]]
    schedule_message = False
    if schedule:  # this can become an exception
        schedule_message = 'Today\'s lessons are:\n\n'
        for lesson in schedule:
            schedule_message = schedule_message + f'<b>{lesson[1]}:</b> {lesson[0]}\n\n'
    return schedule_message


def daily_schedule():
    today = date.today()
    with open(os.path.join(os.path.dirname(__file__), '../..', 'calendar.ics')) as calendar_file:
        lessons_calendar = icalendar.Calendar.from_ical(calendar_file.read())
    schedule = []
    for component in lessons_calendar.walk():
        if component.name == "VEVENT":
            if component.get('dtstart').dt.date() == today:
                start_date = component.get('dtstart').dt.time().isoformat(timespec='minutes')
                end_date = component.get('dtend').dt.time().isoformat(timespec='minutes')
                summary = component.get('summary')
                schedule.append([summary, start_date, end_date])
                # print(start_date)
    return schedule
