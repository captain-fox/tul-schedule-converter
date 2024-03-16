from ics import Event
from typing import Dict, List, Iterable, Generator

from converter.event_blueprint import EventBlueprint

from converter.factories import IcsEventFactory
from converter.semester import Semester


__all__ = ["generate_series_of_events"]


def generate_series_of_events(
    event_blueprints: Iterable[EventBlueprint], semester: Semester
) -> Generator[Event, None, None]:

    weekday_event_mapping: Dict[int, List[EventBlueprint]] = {
        i: list(filter(lambda x: x.weekday == i, event_blueprints)) for i in range(1, 8)
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
                ics_event = IcsEventFactory.create(event_blueprint=_event, date=day)
                yield ics_event
