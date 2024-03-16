import datetime

from typing import Protocol

from converter.collections import WEEKDAYS_PL_IDX
from converter.events import Event

__all__ = ["BaseEventFactory", "EventFactoryWEEIA"]


class BaseEventFactory(Protocol):

    @staticmethod
    def create(event_as_dict: dict) -> Event: ...  # noqa E704


class EventFactoryWEEIA(BaseEventFactory):

    @staticmethod
    def create(event_as_dict: dict) -> Event:
        weekday_pl, time_window, week_idxs_raw = event_as_dict["_Event"].split(" ")
        time_begins, time_ends = time_window.split("-")
        time_begins_hours, time_begins_minutes = time_begins.split(":")
        time_ends_hours, time_ends_minutes = time_ends.split(":")

        weeks = week_idxs_raw.split(",")
        week_idxs = []
        for i in weeks:
            if "-" in i:
                rg = [int(_) for _ in i.split("-")]
                week_idxs.extend([_ for _ in range(rg[0], rg[1] + 1)])
            else:
                week_idxs.append(i)

        event = Event(
            raw_event=event_as_dict,
            category=event_as_dict["_EventCat"].strip(),
            module=event_as_dict["_Module"].strip(),
            room=event_as_dict["_Room"].strip(),
            staff_surname=event_as_dict["_StaffSurname"].strip(),
            staff_forenames=event_as_dict["_StaffForenames"].strip(),
            group=event_as_dict["_Group"].strip(),
            description=event_as_dict["_Description"].strip(),
            weekday=WEEKDAYS_PL_IDX[weekday_pl],
            time_begins=datetime.time(hour=int(time_begins_hours), minute=int(time_begins_minutes)),
            time_ends=datetime.time(hour=int(time_ends_hours), minute=int(time_ends_minutes)),
            week_idxs=week_idxs,
        )

        return event
