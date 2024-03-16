import pytest

from pandas import read_csv

from tests import TEST_DIR


@pytest.fixture(scope="session")
def schedule_csv_as_dataframe():
    return read_csv(f"{TEST_DIR}/stubs/schedule_2024_summer.csv", encoding="windows-1250", sep=";")


@pytest.fixture(scope="session")
def schedule_csv_as_buffer():
    with open(file=f"{TEST_DIR}/stubs/schedule_2024_summer.csv", mode="r", encoding="windows-1250") as file:
        yield file.readlines()


@pytest.fixture(scope="session")
def output_directory():
    return f"{TEST_DIR}/../output/"
