from ics import Calendar
from typing import Dict, List, Iterable

from converter.events import Event
from converter.factories import IcsEventFactory
from converter.semester import Semester


__all__ = ["add_events_to_calendar"]


def add_events_to_calendar(calendar: Calendar, events: Iterable[Event], semester: Semester) -> Calendar:

    weekday_event_mapping: Dict[int, List[Event]] = {
        i: list(filter(lambda x: x.weekday == i, events)) for i in range(1, 8)
    }

    for day in semester.classes_dates_range:
        if day in semester.custom_rule_dates:
            _events = weekday_event_mapping[semester.custom_rule_dates[day]]
        else:
            _events = weekday_event_mapping[day.isoweekday()]
        if not _events:
            continue

        week_idx = semester.isoweek_to_semester_week_mapping[day.isocalendar().week]
        for _event in _events:
            if week_idx in _event.week_idxs:
                ics_event = IcsEventFactory.create(event=_event, date=day)
                calendar.events.add(ics_event)

    return calendar
