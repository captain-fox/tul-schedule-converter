from ics import Calendar
from pandas import DataFrame
from typing import List, Optional

from converter.converter import add_events_to_calendar
from converter.events import Event
from converter.factories import EventFactory
from converter.semester import Semester


def handler(
    data_frame: DataFrame, filter_by: str, filter_by_value: str, semester: Semester, calendar: Optional[Calendar] = None
) -> Calendar:
    """
    Generates custom schedule that matches filter criteria. Calendar is an explicit default parameter
    to allow chaining and passing it to and from other modules that may modify or add events to it.
    :param data_frame: DataFrame
    :param filter_by: str
    :param filter_by_value: str
    :param semester: Semester
    :param calendar: Optional[Calendar]
    :return: Calendar
    """

    if not calendar:
        calendar = Calendar()

    data_frame.fillna("", inplace=True)
    subset = data_frame.loc[data_frame[filter_by] == filter_by_value]

    events: List[Event] = [
        EventFactory.create(row.to_dict()) for _, row in subset.iterrows() if row.to_dict()["_Event"] != ""
    ]

    return add_events_to_calendar(calendar=calendar, events=events, semester=semester)
