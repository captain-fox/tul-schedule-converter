from pandas import DataFrame
from typing import List

from converter.event_blueprint import EventBlueprint
from converter.factories import EventFactoryWEEIA


__all__ = ["parse_data_frame_to_event_blueprints"]


def parse_data_frame_to_event_blueprints(data_frame: DataFrame) -> List[EventBlueprint]:
    return [EventFactoryWEEIA.create(row.to_dict()) for _, row in data_frame.iterrows()]
