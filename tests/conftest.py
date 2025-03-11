import curses
import pytest

import os

import labrea_type_validation._startup
import labrea.runtime


@pytest.fixture
def environment_variable_set():
    os.environ[labrea_type_validation._startup.LABREA_TYPE_VALIDATION_ENABLED] = "TRUE"
    yield
    del os.environ[labrea_type_validation._startup.LABREA_TYPE_VALIDATION_ENABLED]


@pytest.fixture
def fresh_runtime():
    with labrea.runtime.current_runtime():
        yield
