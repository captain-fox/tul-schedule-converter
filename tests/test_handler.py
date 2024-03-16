import pytest
import datetime

from ics import Calendar

from converter.semester import Semester
from function import handler


@pytest.fixture(scope="session")
def semester_2024_summer_regular():
    semester = Semester(
        begins_date=datetime.date(2024, 2, 26),
        ends_date=datetime.date(2024, 6, 23),
        classes_begin_date=datetime.date(2024, 2, 26),
        classes_end_date=datetime.date(2024, 6, 23),
        break_begins_date=datetime.date(2024, 3, 29),
        break_ends_date=datetime.date(2024, 4, 2),
        no_classes_dates=[
            datetime.date(2024, 4, 29),
            datetime.date(2024, 4, 30),
            datetime.date(2024, 5, 2),
            datetime.date(2024, 5, 31),
        ],
        custom_rule_dates={datetime.date(2024, 4, 3): 5},
    )

    return semester


@pytest.fixture(scope="session")
def semester_2024_summer_masters_1():
    semester = Semester(
        begins_date=datetime.date(2024, 2, 26),
        ends_date=datetime.date(2024, 6, 23),
        classes_begin_date=datetime.date(2024, 3, 11),
        classes_end_date=datetime.date(2024, 6, 23),
        break_begins_date=datetime.date(2024, 3, 29),
        break_ends_date=datetime.date(2024, 4, 2),
        no_classes_dates=[
            datetime.date(2024, 4, 29),
            datetime.date(2024, 4, 30),
            datetime.date(2024, 5, 2),
            datetime.date(2024, 5, 31),
        ],
        custom_rule_dates={datetime.date(2024, 4, 3): 5},
    )

    return semester


def test_generate_isc(schedule_csv_as_dataframe, semester_2024_summer_masters_1, output_directory):
    """
    Use this test case as field-use example of this tool.
    """

    # given
    filter_by_condition = "_Group"
    group = "1AiSR Aut"
    output_path = f"{output_directory}/export-{group}-{datetime.datetime.now().isoformat()}.ics"
    calendar = Calendar()

    # when
    result = handler(
        data_frame=schedule_csv_as_dataframe,
        filter_by=filter_by_condition,
        filter_by_value=group,
        semester=semester_2024_summer_masters_1,
        calendar=calendar,
    )

    # then
    with open(file=output_path, mode="w") as f:
        f.writelines(result.serialize_iter())
