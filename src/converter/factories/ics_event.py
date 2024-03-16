import datetime

from dateutil import tz
from ics import Event as IcsEvent

from converter.events import Event


__all__ = ["IcsEventFactory"]


class IcsEventFactory:
    @staticmethod
    def create(event: Event, date: datetime.date) -> IcsEvent:
        dt_start = datetime.datetime(
            year=date.year,
            month=date.month,
            day=date.day,
            hour=event.time_begins.hour,
            minute=event.time_begins.minute,
            tzinfo=tz.gettz("Europe/Warsaw"),
        )
        dt_end = datetime.datetime(
            year=date.year,
            month=date.month,
            day=date.day,
            hour=event.time_ends.hour,
            minute=event.time_ends.minute,
            tzinfo=tz.gettz("Europe/Warsaw"),
        )

        return IcsEvent(
            name=f"{event.module} {event.category}",
            begin=dt_start,
            end=dt_end,
            description=f"{event.staff_surname} {event.staff_forenames}\n{event.description}",
            location=event.room,
        )
