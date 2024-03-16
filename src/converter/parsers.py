from pandas import DataFrame
from typing import List

from converter.events import Event
from converter.factories import EventFactory


__all__ = ["parse_data_frame_to_events"]


def parse_data_frame_to_events(data_frame: DataFrame) -> List[Event]:
    return [EventFactory.create(row.to_dict()) for _, row in data_frame.iterrows()]
