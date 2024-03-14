import datetime

from typing import List, Dict


__all__ = ["Semester"]


class Semester:
    def __init__(
        self,
        begins_date: datetime.date,
        ends_date: datetime.date,
        classes_begin_date: datetime.date,
        classes_end_date: datetime.date,
        break_begins_date: datetime.date,
        break_ends_date: datetime.date,
        no_classes_dates: List[datetime.date],
        custom_rule_dates: Dict[datetime.date, int],
    ):
        self._classes_begin_date = classes_begin_date
        self._classes_end_date = classes_end_date
        self._break_begins_date = break_begins_date
        self._break_ends_date = break_ends_date
        self._no_classes_dates = no_classes_dates
        self._custom_rule_dates = custom_rule_dates
        self._begins_date = begins_date
        self._ends_date = ends_date

    @property
    def begins_date(self) -> datetime.date:
        return self._begins_date

    @property
    def ends_date(self) -> datetime.date:
        return self._ends_date

    @property
    def classes_begin_date(self) -> datetime.date:
        return self._classes_begin_date

    @property
    def classes_end_date(self) -> datetime.date:
        return self._classes_end_date

    @property
    def break_begins_date(self) -> datetime.date:
        return self._break_begins_date

    @property
    def break_ends_date(self) -> datetime.date:
        return self._break_ends_date

    @property
    def no_classes_dates(self) -> List[datetime.date]:
        return self._no_classes_dates

    @property
    def custom_rule_dates(self) -> Dict[datetime.date, int]:
        return self._custom_rule_dates

    @property
    def break_dates_range(self) -> List[datetime.date]:
        dates = []
        date = self.break_begins_date
        while date <= self.break_ends_date:
            dates.append(date)
            date += datetime.timedelta(days=1)
        return dates

    @property
    def classes_dates_range(self) -> List[datetime.date]:
        dates = []
        date = self.classes_begin_date
        while date <= self.classes_end_date:
            if date not in self.no_classes_dates and date not in self.break_dates_range:
                dates.append(date)
            date += datetime.timedelta(days=1)
        return dates

    @property
    def isoweek_to_semester_week_mapping(self) -> Dict[int, int]:
        iso_week_idx_range = range(self.begins_date.isocalendar().week, self.ends_date.isocalendar().week + 1)
        return {iso_idx: idx + 1 for idx, iso_idx in enumerate(iso_week_idx_range)}
