import pytest

from typing import List

import labrea_type_validation
from labrea import Option
from labrea.exceptions import EvaluationError


def test_enabled():
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
        with pytest.raises(EvaluationError):
            A(bad)
        with pytest.raises(EvaluationError):
            A.validate(bad)

    A(good)
    A.validate(good)
    A(bad)
    A.validate(bad)


def test_enable():
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
    with pytest.raises(EvaluationError):
        A(bad)
    with pytest.raises(EvaluationError):
        A.validate(bad)
