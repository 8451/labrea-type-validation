from typing import Optional

import labrea.runtime
from labrea.type_validation import TypeValidationRequest

from . import _validate


def handle_type_validation_request(request: TypeValidationRequest) -> None:
    _validate.validate(request.value, request.type)


def enabled(runtime: Optional[labrea.runtime.Runtime] = None) -> labrea.runtime.Runtime:
    """Add the type validation handler to the given runtime.

    Arguments
    ---------
    runtime : Optional[labrea.runtime.Runtime]
        The runtime to enable type validation on. If None, the current runtime is used.

    Returns
    -------
    labrea.runtime.Runtime
        The runtime with type validation enabled.


    Example Usage
    -------------
    >>> from labrea import Option
    >>> import labrea_type_validation
    >>>
    >>> with labrea_type_validation.enabled():
    ...     Option[int]('A')({'A': 1})
    ...     Option[int]('A')({'A': '1'})  # Raises a TypeError
    """
    runtime = runtime or labrea.runtime.current_runtime()
    return runtime.handle(TypeValidationRequest, handle_type_validation_request)


def enable() -> None:
    """Enable type validation on the current runtime.


    Example Usage
    -------------
    >>> from labrea import Option
    >>> import labrea_type_validation
    >>>
    >>> labrea_type_validation.enable()
    >>> Option[int]('A')({'A': 1})
    >>> Option[int]('A')({'A': '1'})  # Raises a TypeError
    """
    enabled().__enter__()
