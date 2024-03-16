import pytest
import datetime

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

    # replaces "na"s with empty strings for better readability
    schedule_csv_as_dataframe.fillna("", inplace=True)

    # given
    filter_by_column = "_Group"
    filter_by_value = "1AiSR Aut"
    output_path = f"{output_directory}/export-{filter_by_value}-{datetime.datetime.now().isoformat()}.ics"

    # when
    result = handler(
        data_frame=schedule_csv_as_dataframe,
        filter_by=filter_by_column,
        filter_by_value=filter_by_value,
        semester=semester_2024_summer_masters_1,
    )

    # then
    with open(file=output_path, mode="w") as f:
        f.writelines(result.serialize_iter())
