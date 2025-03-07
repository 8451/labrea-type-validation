# Usage

When creating an `Option` with labrea, specify the expected type using either of the following syntaxes:

```python
from labrea import Option

X = Option("X", type=int)
Y = Option[int]("Y")
```

To enable type validation, simply import `labrea_type_validation` and call the `enable` function:

```python
import labrea_type_validation

X({"X": "1"})  # No error

labrea_type_validation.enable()

X({"X": "1"})  # labrea.type_validation.TypeValidationError: Originating in Option('X') | '1' is not of type <class 'int'>
```

Type validation can also be used in a `with` statement as a context manager using `enabled`.

```python
with labrea_type_validation.enabled():
    X({"X": "1"})  # labrea.type_validation.TypeValidationError: Originating in Option('X') | '1' is not of type <class 'int'>
```

## Multithreaded Applications

Type validation is based on the `labrea.runtime` module. For this reason, type validation is
enabled for the current thread and any threads spawned from it. If you are using a multithreaded
application, ensure that type validation is enabled in the main thread before spawning any new
threads.
