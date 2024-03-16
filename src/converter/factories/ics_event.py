import datetime

from dateutil import tz
from ics import Event

from converter.event_blueprint import EventBlueprint


__all__ = ["IcsEventFactory"]


class IcsEventFactory:
    @staticmethod
    def create(event_blueprint: EventBlueprint, date: datetime.date) -> Event:
        dt_start = datetime.datetime(
            year=date.year,
            month=date.month,
            day=date.day,
            hour=event_blueprint.time_begins.hour,
            minute=event_blueprint.time_begins.minute,
            tzinfo=tz.gettz("Europe/Warsaw"),
        )
        dt_end = datetime.datetime(
            year=date.year,
            month=date.month,
            day=date.day,
            hour=event_blueprint.time_ends.hour,
            minute=event_blueprint.time_ends.minute,
            tzinfo=tz.gettz("Europe/Warsaw"),
        )

        return Event(
            name=f"{event_blueprint.module} {event_blueprint.category}",
            begin=dt_start,
            end=dt_end,
            description=f"{event_blueprint.staff_surname} {event_blueprint.staff_forenames}\n{event_blueprint.description}",
            location=event_blueprint.room,
        )
