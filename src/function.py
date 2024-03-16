from ics import Calendar
from pandas import DataFrame
from typing import Optional

from converter.calendar import add_events_to_calendar
from converter.parsers import parse_data_frame_to_events
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
    subset = data_frame.loc[data_frame[filter_by].eq(filter_by_value) & data_frame["_Event"].notnull()]
    events = parse_data_frame_to_events(subset)

    return add_events_to_calendar(calendar=calendar, events=events, semester=semester)
