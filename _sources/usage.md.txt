# Usage

When creating an `Option` with labrea, specify the expected type using either of the following syntaxes:

```python
from labrea import Option

X = Option("X", type=int)
Y = Option[int]("Y")
```

Either literal types or type hints can be used, such as `List[int]` or `Union[str, List[str]]`.

To enable type validation, simply import `labrea_type_validation` and call the `enable` function:

```python
import labrea_type_validation

X({"X": "1"})  # No error

labrea_type_validation.enable()

X({"X": "1"})
# ...
# TypeError: Expected type <class 'int'> but got <class 'str'> ('1')
#
# The above exception was the direct cause of the following exception:
#
# Traceback (most recent call last):
# ...
# labrea.exceptions.EvaluationError: Originating in Option('X') | Error during evaluation
```

Type validation can also be used in a `with` statement as a context manager using `enabled`.

```python
with labrea_type_validation.enabled():
    X({"X": "1"})
# ...
# TypeError: Expected type <class 'int'> but got <class 'str'> ('1')
#
# The above exception was the direct cause of the following exception:
#
# Traceback (most recent call last):
# ...
# labrea.exceptions.EvaluationError: Originating in Option('X') | Error during evaluation
```

Alternatively, the `LABREA_TYPE_VALIDATION_ENABLED` environment variable can be set to `TRUE`.

## Multithreaded Applications

Type validation is based on the `labrea.runtime` module. For this reason, type validation is
enabled for the current thread and any threads spawned from it. If you are using a multithreaded
application, ensure that type validation is enabled in the main thread before spawning any new
threads.
