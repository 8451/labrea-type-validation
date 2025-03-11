import os

from . import _runtime


LABREA_TYPE_VALIDATION_ENABLED = "LABREA_TYPE_VALIDATION_ENABLED"
DEFAULT_SETTING = "FALSE"
FALSE_SETTINGS = ("FALSE", "F", "NO", "N", "0")


def run() -> None:
    if os.environ.get(LABREA_TYPE_VALIDATION_ENABLED, DEFAULT_SETTING).upper() in FALSE_SETTINGS:
        return
    else:
        _runtime.enable()
