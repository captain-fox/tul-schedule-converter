from ics import Calendar
from pandas import DataFrame
from typing import Dict, List, Optional

from converter.events import Event
from converter.factories import EventFactory, IcsEventFactory
from converter.semester import Semester


def handler(
    data_frame: DataFrame, filter_by: str, filter_by_value: str, semester: Semester, calendar: Optional[Calendar] = None
) -> Calendar:

    if not calendar:
        calendar = Calendar()

    data_frame.fillna("", inplace=True)
    subset = data_frame.loc[data_frame[filter_by] == filter_by_value]

    events: List[Event] = [
        EventFactory.create(row.to_dict()) for _, row in subset.iterrows() if row.to_dict()["_Event"] != ""
    ]
    weekday_event_mapping: Dict[int, List[Event]] = {
        i: list(filter(lambda e: e.weekday == i, events)) for i in range(1, 8)
    }

    for day in semester.classes_dates_range:
        if day in semester.custom_rule_dates:
            _events = weekday_event_mapping[semester.custom_rule_dates[day]]
        else:
            _events = weekday_event_mapping[day.isoweekday()]
        if not _events:
            continue

        week_idx = semester.isoweek_to_semester_week_mapping[day.isocalendar().week]
        for e in _events:
            if week_idx in e.week_idxs:
                ics_event = IcsEventFactory.create(event=e, date=day)
                calendar.events.add(ics_event)

    return calendar
