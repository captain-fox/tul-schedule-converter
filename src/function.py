from ics import Calendar
from pandas import DataFrame
from typing import Optional

from converter.calendar import generate_series_of_events
from converter.misc import parse_data_frame_to_event_blueprints
from converter.semester import Semester


def handler(
    data_frame: DataFrame, filter_by: str, filter_by_value: str, semester: Semester, calendar: Optional[Calendar] = None
) -> Calendar:
    """
    Generates custom WEEIiA schedule that matches filter criteria. Calendar is an explicit default parameter
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

    subset = data_frame.loc[data_frame[filter_by].eq(filter_by_value) & data_frame["_Event"].notnull()]
    blueprints = parse_data_frame_to_event_blueprints(subset)

    for evt in generate_series_of_events(event_blueprints=blueprints, semester=semester):
        calendar.events.add(evt)

    return calendar
