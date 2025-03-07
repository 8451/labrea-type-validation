from typing import Any, Type
import builtins

import pydantic


def validate(value: Any, type: Type) -> None:
    """Validate a value against a type using Pydantic."""
    try:
        pydantic.TypeAdapter(type).validate_python(value, strict=True)
    except pydantic.ValidationError as e:
        raise TypeError(f"Expected type {type} but got {builtins.type(value)} ({value!r})") from e
