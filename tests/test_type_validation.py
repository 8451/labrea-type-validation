import pytest
import importlib

from typing import List, Type

import labrea_type_validation
from labrea import Option
from labrea.exceptions import EvaluationError


def test_enabled(fresh_runtime):
    A = Option[List[int]]("A")
    good = {"A": [1, 2, 3]}
    bad = {"A": [1, 2, "3"]}

    A(good)
    A.validate(good)
    A(bad)
    A.validate(bad)

    with labrea_type_validation.enabled():
        A(good)
        A.validate(good)
        with pytest.raises(TypeError):
            A(bad)
        with pytest.raises(TypeError):
            A.validate(bad)

    A(good)
    A.validate(good)
    A(bad)
    A.validate(bad)


def test_enable(fresh_runtime):
    A = Option[List[int]]("A")
    good = {"A": [1, 2, 3]}
    bad = {"A": [1, 2, "3"]}

    A(good)
    A.validate(good)
    A(bad)
    A.validate(bad)

    labrea_type_validation.enable()
    A(good)
    A.validate(good)
    with pytest.raises(TypeError):
        A(bad)
    with pytest.raises(TypeError):
        A.validate(bad)


def test_startup(fresh_runtime, environment_variable_set):
    importlib.reload(labrea_type_validation)

    A = Option[List[int]]("A")
    good = {"A": [1, 2, 3]}
    bad = {"A": [1, 2, "3"]}

    A(good)
    A.validate(good)
    with pytest.raises(TypeError):
        A(bad)
    with pytest.raises(TypeError):
        A.validate(bad)
