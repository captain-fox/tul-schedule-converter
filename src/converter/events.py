import datetime

from typing import List


__all__ = ["Event"]


class Event:
    def __init__(
        self,
        raw_event: dict,
        category: str,
        module: str,
        room: str,
        staff_surname: str,
        staff_forenames: str,
        group: str,
        description: str,
        weekday: int,
        time_begins: datetime.time,
        time_ends: datetime.time,
        week_idxs: List[int],
    ):
        self._raw_event = raw_event
        self._category = category
        self._module = module
        self._room = room
        self._staff_surname = staff_surname
        self._staff_forenames = staff_forenames
        self._group = group
        self._description = description
        self._weekday = weekday
        self._time_begins = time_begins
        self._time_ends = time_ends
        self._week_idxs = week_idxs

    @property
    def raw_event(self) -> dict:
        return self._raw_event

    @property
    def category(self) -> str:
        return self._category

    @property
    def module(self) -> str:
        return self._module

    @property
    def room(self) -> str:
        return self._room

    @property
    def staff_surname(self) -> str:
        return self._staff_surname

    @property
    def staff_forenames(self) -> str:
        return self._staff_forenames

    @property
    def group(self) -> str:
        return self._group

    @property
    def description(self) -> str:
        return self._description

    @property
    def weekday(self) -> int:
        return self._weekday

    @property
    def time_begins(self) -> datetime.time:
        return self._time_begins

    @property
    def time_ends(self) -> datetime.time:
        return self._time_ends

    @property
    def week_idxs(self) -> List[int]:
        return self._week_idxs

    def __str__(self):
        return f"{self._module}, {self.time_begins} - {self.time_ends}"
